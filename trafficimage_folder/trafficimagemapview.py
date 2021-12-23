from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from trafficimage_folder.trafficimagemarker import TrafficImageMarker
import json
import requests
from kivy.uix.carousel import Carousel
from kivy.uix.image import AsyncImage
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class TrafficImageMapView(MapView):
    getting_trafficimage_timer = None
    cameraid = []
 
    def start_getting_trafficimage_in_fov(self):
        # On lon or on lat, it will first try to cancel the timer
        try:
            self.getting_trafficimage_timer.cancel()
        except:
            pass
        # After one second, get the markets in the field of view
        self.getting_trafficimage_timer = Clock.schedule_once(self.get_trafficimage_in_fov, 1)
 
    def get_trafficimage_in_fov(self, *args):
        # Get reference to main app and the database cursor
        self.cameraid = []
 
        traffic_images_path = "ltaodataservice/Traffic-Imagesv2"
        traffic_images_url = uri + traffic_images_path
 
        traffic_images = requests.get(traffic_images_url, headers=headers)
        traffic_images_response = json.loads(traffic_images.content)
 
        trafficimage_backdropfrontlayer = App.get_running_app().trafficimage_backdroplayout.ids.frontlayer
        carousel = Carousel(direction='right')
        try:
            for w in trafficimage_backdropfrontlayer.walk():
                if w.__class__ == Carousel:
                    print("remove carousel widget")
                    trafficimage_backdropfrontlayer.remove_widget(w)
                else:
                    print("No widget to remove")
                    continue
        except:
            print("Something is wrong")
            pass
 
        for trafficimage in traffic_images_response['value']:
            cam_id = trafficimage['CameraID']
            if cam_id in self.cameraid:
                continue
            else:
                self.add_trafficimage(trafficimage)
                src = trafficimage['ImageLink']
                image = AsyncImage(source=src, allow_stretch=True)
                carousel.add_widget(image)
 
        trafficimage_backdropfrontlayer.add_widget(carousel)
 
    def add_trafficimage(self, trafficimage):
        # Create the TrafficImageMarker
        lat, lon = trafficimage['Latitude'], trafficimage['Longitude']
        marker = TrafficImageMarker(lat=lat, lon=lon, source = "icons/cctv.png")
        marker.trafficimage_data = trafficimage
        # Add the TrafficImageMarker to the map
        self.add_widget(marker)
 
        # Keep track of the traffic image camera id
        cam_id = trafficimage['CameraID']
        self.cameraid.append(cam_id)
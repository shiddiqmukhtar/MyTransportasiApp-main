from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from bicycle_folder.bicycleparkingmarker import BicycleParkingMarker
import json
import requests
  
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
  
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
  
class BicycleParkingMapView(MapView):
    getting_bicycleparking_timer = None
    bicycleparking_description = []
  
    def start_getting_bicycleparking_in_fov(self):
        # On lon or on lat, it will first try to cancel the timer
        try:
            self.getting_bicycleparking_timer.cancel()
        except:
            pass
        # After one second, get the markets in the field of view
        self.getting_bicycleparking_timer = Clock.schedule_once(self.get_bicycleparking_in_fov, 1)
  
    def get_bicycleparking_in_fov(self, *args):
        self.bicycleparking_description = []
 
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
 
        bicycle_parking_path = "ltaodataservice/BicycleParkingv2"
        parameter1_md = "?Lat="
        Lat = str((min_lat + max_lat)/2) # This is an example
        parameter2_md = "&Long="
        Long = str((min_lon + max_lon)/2) # This is an example
        parameter3_op = "&Dist=" # Radius in kilometre, Default is 0.5
        bicycle_parking_url = uri + bicycle_parking_path + parameter1_md + Lat + parameter2_md + Long
 
        bicycle_parking = requests.get(bicycle_parking_url, headers=headers)
        bicycle_parking_response = json.loads(bicycle_parking.content)
 
        for bicycleparking in bicycle_parking_response['value']:
            if bicycleparking['Longitude'] > min_lon and bicycleparking['Longitude'] < max_lon and bicycleparking['Latitude'] > min_lat and bicycleparking['Latitude'] < max_lat:
                description = bicycleparking['Description']
                if description in self.bicycleparking_description:
                    continue
                else:
                    self.add_bicycleparking(bicycleparking)
  
    def add_bicycleparking(self, bicycleparking):
        # Create the BicycleParkingMarker
        lat, lon = bicycleparking['Latitude'], bicycleparking['Longitude']
        marker = BicycleParkingMarker(lat=lat, lon=lon, source = "icons/bicycleparking.png")
        marker.bicycleparking_data = bicycleparking
        # Add the Bicycle Parking Marker to the map
        self.add_widget(marker)
  
        # Keep track of the bicycle parking description
        description = bicycleparking['Description']
        self.bicycleparking_description.append(description)
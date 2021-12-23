from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from carpark_folder.carparkmarker import CarParkMarker_C, CarParkMarker_H, CarParkMarker_Y
import json
import requests
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class CarParkMapView(MapView):
    getting_carpark_timer = None
    carpark_id = []
 
    def start_getting_carpark_in_fov(self):
        # On lon or on lat, it will first try to cancel the timer
        try:
            self.getting_carpark_timer.cancel()
        except:
            pass
        # After one second, get the markets in the field of view
        self.getting_carpark_timer = Clock.schedule_once(self.get_carpark_in_fov, 1)
 
    def get_carpark_in_fov(self, *args):
        self.carpark_id = []
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
 
        carpark_availability_path = "ltaodataservice/CarParkAvailabilityv2"
        carpark_availability_url = uri + carpark_availability_path
 
        carpark_availability = requests.get(carpark_availability_url, headers=headers)
        carpark_availability_response = json.loads(carpark_availability.content)
 
        for carpark in carpark_availability_response['value']:
            lat_lon_list = carpark['Location'].split()
            # print(lat_lon_list[0])
            # print(lat_lon_list[1])
            try:
                if float(lat_lon_list[1]) > min_lon and float(lat_lon_list[1]) < max_lon and float(lat_lon_list[0]) > min_lat and float(lat_lon_list[0]) < max_lat:
                    code = carpark['CarParkID']
                    if code in self.carpark_id:
                        continue
                    else:
                        self.add_carpark(carpark, lat_lon_list)
            except Exception as e:
                print(e)
                pass
 
    def add_carpark(self, carpark, lat_lon_list):
        # Create the MarketMarker
        lat, lon = lat_lon_list[0], lat_lon_list[1]
        if carpark['LotType'] == "C":
            marker = CarParkMarker_C(lat=lat, lon=lon, source = "icons/car.png")
            marker.carpark_data_C = carpark
        elif carpark['LotType'] == "H":
            marker = CarParkMarker_H(lat=lat, lon=lon, source = "icons/heavyvehicle.png")
            marker.carpark_data_H = carpark
        else:
            marker = CarParkMarker_Y(lat=lat, lon=lon, source = "icons/motorcycle.png")
            marker.carpark_data_Y = carpark
        # Add the Car Park Marker to the map
        self.add_widget(marker)
 
        # Keep track of the car park id
        code = carpark['CarParkID']
        self.carpark_id.append(code)
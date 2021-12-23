from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from taxi_folder.taximarker import TaxiMarker, TaxiStandMarker
import json
import requests
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class TaxiMapView(MapView):
    getting_taxi_timer = None
    taxi_stand_code = []
 
    def start_getting_taxi_in_fov(self):
        # On lon or on lat, it will first try to cancel the timer
        try:
            self.getting_taxi_timer.cancel()
        except:
            pass
        # After one second, get the taxi in the field of view
        self.getting_taxi_timer = Clock.schedule_once(self.get_taxi_in_fov, 1)
 
    def get_taxi_in_fov(self, *args):
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        # https://stackoverflow.com/questions/2081753/getting-the-bounds-of-an-mkmapview
 
        taxi_availability_path = "ltaodataservice/Taxi-Availability"
        taxi_availability_url = uri + taxi_availability_path
 
        taxi_availability = requests.get(taxi_availability_url, headers=headers)
        taxi_availability_response = json.loads(taxi_availability.content)
   
        for taxi in taxi_availability_response['value']:
            if taxi['Longitude'] > min_lon and taxi['Longitude'] < max_lon and taxi['Latitude'] > min_lat and taxi['Latitude'] < max_lat:
                self.add_taxi(taxi)
 
        taxi_stands_path = "ltaodataservice/TaxiStands"
        taxi_stands_url = uri + taxi_stands_path
 
        taxi_stands = requests.get(taxi_stands_url, headers=headers)
        taxi_stands_response = json.loads(taxi_stands.content)
 
 
        for taxi_stand in taxi_stands_response['value']:
            if taxi_stand['Longitude'] > min_lon and taxi_stand['Longitude'] < max_lon and taxi_stand['Latitude'] > min_lat and taxi_stand['Latitude'] < max_lat:
                code = taxi_stand['TaxiCode']
                if code in self.taxi_stand_code:
                    continue
                else:
                    #print(taxi_stand)
                    self.add_taxi_stand(taxi_stand)
 
    def add_taxi(self, taxi):
        # Create the TaxiMarker
        lat, lon = taxi['Latitude'], taxi['Longitude']
        marker = TaxiMarker(lat=lat, lon=lon, source="icons/taxi.png")
        marker.taxi_data = taxi
        # Add the TaxiMarker to the map
        self.add_widget(marker)
 
    def add_taxi_stand(self, taxi_stand):
        # Create the Taxi Stand Marker
        lat, lon = taxi_stand['Latitude'], taxi_stand['Longitude']
        marker = TaxiStandMarker(lat=lat, lon=lon, source = "icons/taxi-stop.png")
        marker.taxi_stand_data = taxi_stand
        # Add the Taxi Stand Marker to the map
        self.add_widget(marker)
 
        # Keep track of the taxi stand code
        code = taxi_stand['TaxiCode']
        self.taxi_stand_code.append(code)
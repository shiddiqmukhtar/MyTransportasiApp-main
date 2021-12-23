from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from incidents_folder.incidentsmarker import IncidentsMarker_Accident, IncidentsMarker_Road_Works, IncidentsMarker_Vehicle_Breakdown, IncidentsMarker_Weather, IncidentsMarker_Obstacle, IncidentsMarker_Road_Block, IncidentsMarker_Heavy_Traffic, IncidentsMarker_Misc, IncidentsMarker_Diversion, IncidentsMarker_Unattended_Vehicle
import json
import requests
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class IncidentsMapView(MapView):
    getting_incidents_timer = None
    incidents_description = []
 
    def start_getting_incidents_in_fov(self):
        # On lon or on lat, it will first try to cancel the timer
        try:
            self.getting_incidents_timer.cancel()
        except:
            pass
        # After one second, get the incidents in the field of view
        self.getting_incidents_timer = Clock.schedule_once(self.get_incidents_in_fov, 1)
 
    def get_incidents_in_fov(self, *args):
        # Get reference to main app and the database cursor
        self.incidents_description = []
 
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
 
        traffic_incidents_path = "ltaodataservice/TrafficIncidents"
        traffic_incidents_url = uri + traffic_incidents_path
 
        traffic_incidents = requests.get(traffic_incidents_url, headers=headers)
        traffic_incidents_response = json.loads(traffic_incidents.content)
        # {
        # "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadata#IncidentSet",
        # "value": [
        #     {
        #         "Type": "Vehicle breakdown",
        #         "Latitude": 1.3791291006440773,
        #         "Longitude": 103.9143563613163,
        #         "Message": "(14/10)15:44 Vehicle breakdown on KPE (towards ECP) before Buangkok Dr Exit. Avoid lane 1."
        #     },
 
        for incident in traffic_incidents_response['value']:
            if incident['Longitude'] > min_lon and incident['Longitude'] < max_lon and incident['Latitude'] > min_lat and incident['Latitude'] < max_lat:
                description = incident['Type'] + str(incident['Latitude']) + str(incident['Longitude'])
                if description in self.incidents_description:
                    continue
                else:
                    self.add_incident(incident)
 
    def add_incident(self, incident):
        lat, lon = incident['Latitude'], incident['Longitude']
        if incident['Type'] == "Accident":
            marker = IncidentsMarker_Accident(lat=lat, lon=lon, source = "icons/accident.png")
            marker.incident_data_accident = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Roadwork":
            marker = IncidentsMarker_Road_Works(lat=lat, lon=lon, source = "icons/roadworks.png")
            marker.incident_data_road_works = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Vehicle breakdown":
            marker = IncidentsMarker_Vehicle_Breakdown(lat=lat, lon=lon, source = "icons/vehiclebreakdown.png")
            marker.incident_data_vehicle_breakdown = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Weather":
            marker = IncidentsMarker_Weather(lat=lat, lon=lon, source = "icons/weather.png")
            marker.incident_data_weather = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Obstacle":
            marker = IncidentsMarker_Obstacle(lat=lat, lon=lon, source = "icons/obstacle.png")
            marker.incident_data_obstacle = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Road Block":
            marker = IncidentsMarker_Road_Block(lat=lat, lon=lon, source = "icons/roadblock.png")
            marker.incident_data_road_block = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Heavy Traffic":
            marker = IncidentsMarker_Heavy_Traffic(lat=lat, lon=lon, source = "icons/heavytraffic.png")
            marker.incident_data_heavy_traffic = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Diversion":
            marker = IncidentsMarker_Diversion(lat=lat, lon=lon, source = "icons/diversion.png")
            marker.incident_data_diversion = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        elif incident['Type'] == "Unattended Vehicle":
            marker = IncidentsMarker_Unattended_Vehicle(lat=lat, lon=lon, source = "icons/unattendedvehicle.png")
            marker.incident_data_unattended_vehicle = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
        else:
            marker = IncidentsMarker_Misc(lat=lat, lon=lon, source = "icons/misc.png")
            marker.incident_data_misc = incident
            # Add the IncidentsMarker to the map
            self.add_widget(marker)
 
        # Keep track of the incident
        description = incident['Type'] + str(incident['Latitude']) + str(incident['Longitude'])
        self.incidents_description.append(description)
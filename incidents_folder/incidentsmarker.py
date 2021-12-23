from kivy_garden.mapview import MapMarkerPopup
from incidents_folder.incidentspopupmenu import IncidentsPopupMenu
 
class IncidentsMarker_Accident(MapMarkerPopup):
    #source = "icons/accident.png"
    incident_data_accident = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_accident)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Road_Works(MapMarkerPopup):
    #source = "icons/roadworks.png"
    incident_data_road_works = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_road_works)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Vehicle_Breakdown(MapMarkerPopup):
    #source = "icons/vehiclebreakdown.png"
    incident_data_vehicle_breakdown = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_vehicle_breakdown)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Weather(MapMarkerPopup):
    #source = "icons/weather.png"
    incident_data_weather = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_weather)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Obstacle(MapMarkerPopup):
    #source = "icons/obstacle.png"
    incident_data_obstacle = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_obstacle)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Road_Block(MapMarkerPopup):
    #source = "icons/roadblock.png"
    incident_data_road_block = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_road_block)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Heavy_Traffic(MapMarkerPopup):
    #source = "icons/heavytraffic.png"
    incident_data_heavy_traffic = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_heavy_traffic)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Misc(MapMarkerPopup):
    #source = "icons/misc.png"
    incident_data_misc = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_misc)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Diversion(MapMarkerPopup):
    #source = "icons/diversion.png"
    incident_data_diversion = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_diversion)
        menu.size_hint = [.8, .6]
        menu.open()
 
class IncidentsMarker_Unattended_Vehicle(MapMarkerPopup):
    #source = "icons/unattendedvehicle.png"
    incident_data_unattended_vehicle = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = IncidentsPopupMenu(self.incident_data_unattended_vehicle)
        menu.size_hint = [.8, .6]
        menu.open()
from kivy_garden.mapview import MapMarkerPopup
from busservice_folder.busservicepopupmenu import BusServicePopupMenu
 
class BusServiceMarker(MapMarkerPopup):
    #source = "icons/bus.png"
    bus_service_data = []
 
    def on_release(self):
        # Open up the BusServicePopupMenu
        menu = BusServicePopupMenu(self.bus_service_data)
        menu.size_hint = [.8, .6]
        menu.open()
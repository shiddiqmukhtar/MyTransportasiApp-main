from kivy_garden.mapview import MapMarkerPopup
from busstop_folder.busstoppopupmenu import BusStopPopupMenu
 
class BusStopMarker(MapMarkerPopup):
    #source = "icons/bus-stop.png"
    bus_stop_data = []
 
    def on_release(self):
        menu = BusStopPopupMenu(self.bus_stop_data)
        menu.size_hint = [.8, .6]
        menu.open()
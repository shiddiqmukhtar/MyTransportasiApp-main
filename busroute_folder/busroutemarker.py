from kivy_garden.mapview import MapMarkerPopup
from busroute_folder.busroutepopupmenu import BusRoutePopupMenu
 
class BusRouteMarkerAhead(MapMarkerPopup):
    #source = "icons/route_notdone.png"
    bus_route_data = []
    def on_release(self):
        menu = BusRoutePopupMenu(self.bus_route_data)
        menu.size_hint = [.8, .7]
        menu.open()
 
class BusRouteMarkerPassed(MapMarkerPopup):
    #source = "icons/route_done.png"
    bus_route_data = []
    def on_release(self):
        menu = BusRoutePopupMenu(self.bus_route_data)
        menu.size_hint = [.8, .7]
        menu.open()
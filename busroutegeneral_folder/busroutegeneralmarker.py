from kivy_garden.mapview import MapMarkerPopup
from busroutegeneral_folder.busroutegeneralpopupmenu import BusRouteGeneralPopupMenu
 
class ThisBusRouteMarker(MapMarkerPopup):
    #source = "icons/route1.png"
    bus_route_data = []
    def on_release(self):
        menu = BusRouteGeneralPopupMenu(self.bus_route_data)
        menu.size_hint = [.8, .7]
        menu.open()
 
class OppositeBusRouteMarker(MapMarkerPopup):
    #source = "icons/route2.png"
    bus_route_data = []
    def on_release(self):
        menu = BusRouteGeneralPopupMenu(self.bus_route_data)
        menu.size_hint = [.8, .7]
        menu.open()
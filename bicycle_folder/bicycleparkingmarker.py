from kivy_garden.mapview import MapMarkerPopup
from bicycle_folder.bicycleparkingpopupmenu import BicycleParkingPopupMenu
 
class BicycleParkingMarker(MapMarkerPopup):
    #source = "icons/bicycleparking.png"
    bicycleparking_data = []
 
    def on_release(self):
        # Open up the BicycleParkingPopupMenu
        menu = BicycleParkingPopupMenu(self.bicycleparking_data)
        menu.size_hint = [.8, .6]
        menu.open()
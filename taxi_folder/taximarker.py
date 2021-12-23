from kivy_garden.mapview import MapMarkerPopup
from taxi_folder.taxipopupmenu import TaxiPopupMenu, TaxiStandPopupMenu
 
class TaxiMarker(MapMarkerPopup):
    #source = "icons/taxi.png"
    taxi_data = []
 
    def on_release(self):
        # Open up the TaxiPopupMenu
        menu = TaxiPopupMenu(self.taxi_data)
        menu.size_hint = [.8, .3]
        menu.open()
 
class TaxiStandMarker(MapMarkerPopup):
    #source = "icons/taxi-stop.png"
    taxi_stand_data = []
 
    def on_release(self):
        # Open up the TaxiStandPopupMenu
        menu = TaxiStandPopupMenu(self.taxi_stand_data)
        menu.size_hint = [.8, .6]
        menu.open()
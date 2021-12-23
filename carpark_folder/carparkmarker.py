from kivy_garden.mapview import MapMarkerPopup
from carpark_folder.carparkpopupmenu import CarParkPopupMenu
 
class CarParkMarker_C(MapMarkerPopup):
    #source = "icons/car.png"
    carpark_data_C = []
 
    def on_release(self):
        menu = CarParkPopupMenu(self.carpark_data_C)
        menu.size_hint = [.8, .6]
        menu.open()
 
class CarParkMarker_H(MapMarkerPopup):
    #source = "icons/heavyvehicle.png"
    carpark_data_H = []
 
    def on_release(self):
        menu = CarParkPopupMenu(self.carpark_data_H)
        menu.size_hint = [.8, .9]
        menu.open()
 
class CarParkMarker_Y(MapMarkerPopup):
    #source = "icons/motorcycle.png"
    carpark_data_Y = []
 
    def on_release(self):
        menu = CarParkPopupMenu(self.carpark_data_Y)
        menu.size_hint = [.8, .9]
        menu.open()
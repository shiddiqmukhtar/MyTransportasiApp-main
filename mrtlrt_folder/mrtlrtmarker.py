from kivy_garden.mapview import MapMarkerPopup
from mrtlrt_folder.mrtlrtpopupmenu import MrtPopupMenu, LrtPopupMenu
 
class MrtMarker(MapMarkerPopup):
    #source = "icons/MRT.png"
    mrt_data = []
 
    def on_release(self):
        menu = MrtPopupMenu(self.mrt_data)
        menu.size_hint = [.8, .6]
        menu.open()
 
class LrtMarker(MapMarkerPopup):
    #source = "icons/LRT.png"
    lrt_data = []
 
    def on_release(self):
        menu = LrtPopupMenu(self.lrt_data)
        menu.size_hint = [.8, .6]
        menu.open()
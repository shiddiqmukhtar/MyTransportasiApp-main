from kivy_garden.mapview import MapMarkerPopup
from kivy.uix.popup import Popup
from kivy.uix.image import Image, AsyncImage
 
class TrafficImageMarker(MapMarkerPopup):
    #source = "icons/cctv.png"
    trafficimage_data = []
 
    def on_release(self):
        self.image = AsyncImage(source=self.trafficimage_data['ImageLink'], allow_stretch=True, keep_ratio=True)
        self.pop = Popup(title=self.trafficimage_data['CameraID'], content=self.image, size_hint=(1, .5))
        self.pop.open()
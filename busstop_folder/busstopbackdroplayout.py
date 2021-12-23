from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.screenmanager import Screen
import kivy.utils
from kivy.uix.scrollview import ScrollView
 
# Your layouts.
KV = (
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:include busstop_folder/busstopmapview.kv
 
<MyBackdropBackLayer@ScrollView>
 
<MyBackdropFrontLayer@Screen>
 
 
<BusStopBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "Press for List of Bus Stops Nearby"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Bus Stops Nearby:"
 
        MDBackdropBackLayer:
            MyBackdropBackLayer:
                id: container
 
        MDBackdropFrontLayer:
            MyBackdropFrontLayer:
                id: frontlayer
                 
'''
)
 
class BusStopBackdrop(Screen):
    pass
 
class BusStopBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return BusStopBackdrop()
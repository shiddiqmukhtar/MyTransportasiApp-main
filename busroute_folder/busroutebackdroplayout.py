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
#:include busroute_folder/busroutemapview.kv
 
<MyBackdropBackLayerRoute@Screen>
 
<BusRouteBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "Press for Bus Routes"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Bus Routes:"
 
        MDBackdropBackLayer:
            MyBackdropBackLayerRoute:
                id: container
 
        MDBackdropFrontLayer:
            ScrollView:
                MDGridLayout:
                    id: frontlayer
                    cols: 1
                    adaptive_height: True
                    row_default_height: '87dp'
                    #row_force_default: True
                    spacing: 2,2         
'''
)
 
class BusRouteBackdrop(Screen):
    pass
 
class BusRouteBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return BusRouteBackdrop()
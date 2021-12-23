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
#:include busroutegeneral_folder/busroutegeneralmapview.kv
 
<MyBackdropBackLayerRouteGeneral@Screen>
 
<BusRouteGeneralBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "Press for Bus Routes"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Bus Routes:"
 
        MDBackdropBackLayer:
            MyBackdropBackLayerRouteGeneral:
                id: container
 
        MDBackdropFrontLayer:
            ScrollView:
                MDGridLayout:
                    id: frontlayer
                    cols: 1
                    adaptive_height: True
                    row_default_height: '87dp'
                    row_force_default: True
                    spacing: 2,2
                 
'''
)
 
class BusRouteGeneralBackdrop(Screen):
    pass
 
class BusRouteGeneralBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return BusRouteGeneralBackdrop()
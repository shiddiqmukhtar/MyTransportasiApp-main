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
#:include trafficimage_folder/trafficimagemapview.kv
 
<MyBackdropBackLayerTrafficImage@Screen>
 
<MyBackdropFrontLayerTrafficImage@Screen>
 
<TrafficImageBackdrop>
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        title: "Traffic Images"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Traffic Images:"
 
        MDBackdropBackLayer:
            MyBackdropBackLayerTrafficImage:
                id: container
 
        MDBackdropFrontLayer:
            MyBackdropFrontLayerTrafficImage:
                id: frontlayer
                 
'''
)
 
class TrafficImageBackdrop(Screen):
    pass
 
class TrafficImageBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return TrafficImageBackdrop()
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import StringProperty, BooleanProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import Screen
from kivymd.theming import ThemableBehavior
import kivy.utils
 
# Your layouts.
KV = (
    '''
#:import Window kivy.core.window.Window
#:import IconLeftWidget kivymd.uix.list.IconLeftWidget
#:include busservice_folder/busservicemapview.kv
 
<MyBackdropBackLayerService@ScrollView>
 
<MyBackdropFrontLayerService@Screen>
 
<BusServiceBackdrop>
 
    MDBackdrop:
        id: backdrop
        left_action_items: [['transfer-down', lambda x: self.open()]]
        on_open: app.create_busservicelist_widget()
        title: "Press for List of Bus Services Nearby"
        radius_left: "25dp"
        radius_right: "0dp"
        header_text: "Bus Services Nearby:"
 
        MDBackdropBackLayer:
            MyBackdropBackLayerService:
                id: container
 
        MDBackdropFrontLayer:
            MyBackdropFrontLayerService:
                id: frontlayer
                 
'''
)
 
class BusServiceBackdrop(Screen):
    pass
 
class BusServiceBackDropLayout(FloatLayout):
    def run(self):
        Builder.load_string(KV)
        return BusServiceBackdrop()
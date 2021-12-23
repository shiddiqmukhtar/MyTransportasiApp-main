from kivy.lang import Builder
from kivy.uix.floatlayout import FloatLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import Screen
from kivymd.uix.list import ThreeLineListItem
from kivymd.uix.boxlayout import MDBoxLayout
 
KV = '''
BoxLayout:
    orientation: "vertical"
 
    MDTabs:
        id: tabs
        on_tab_switch: app.on_trainfare_tab_switch(*args)
 
<TrainFareTab>:
 
    ScrollView:
        MDGridLayout:
            id: content
            cols: 1
            adaptive_height: True
            row_default_height: '87dp'
            #row_force_default: True
            spacing: 2,2
'''
 
class TrainFareThreeLineListItem(MDBoxLayout):
    def __init__(self, **kwargs):
        super().__init__()
 
        # print(kwargs['train_fare'])
        fare_in_sgd = "SG$ " + str(float(kwargs['train_fare']['fare']) / 100)
 
        try:
            threelinelistitem = ThreeLineListItem(text=kwargs['train_fare']['timing'], secondary_text = kwargs['train_fare']['distance'], tertiary_text=fare_in_sgd)
            self.add_widget(threelinelistitem)
        except Exception as e:
            print(e)
 
class TrainFareTab(FloatLayout, MDTabsBase):
    '''Class implementing content for a tab.'''
 
class TrainFare(Screen):
    def run(self):
        return Builder.load_string(KV)
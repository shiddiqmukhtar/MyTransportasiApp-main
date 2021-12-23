from kivy.lang import Builder
from kivymd.uix.gridlayout import MDGridLayout
from kivy.uix.screenmanager import Screen
 
KV = '''
<RoadOpeningExpansionContent>
    adaptive_height: True
 
ScrollView:
    MDGridLayout:
        id: box
        cols: 1
        adaptive_height: True
'''
 
class RoadOpening(Screen):
    def run(self):
        return Builder.load_string(KV)
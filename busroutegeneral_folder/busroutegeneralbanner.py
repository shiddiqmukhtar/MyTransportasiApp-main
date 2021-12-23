from kivy.uix.gridlayout import GridLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.app import App
import kivy.utils
from functools import partial
from datetime import datetime
import pytz
import math
from kivymd.uix.list import TwoLineAvatarListItem, ThreeLineAvatarListItem, ImageLeftWidget
from kivy.uix.label import Label
from kivy.uix.image import Image
  
class BusRouteGeneralHeader(GridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super().__init__()
  
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("c8fcf7"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
  
        # print(kwargs['thisrouteserviceno'])
        # # 972
        # print(kwargs['originbusstopdata'])
        # # ['972', 'SMRT', 1, 1, '45009', '0', '0530', '2335', '0530', '2335', '0530', '2335', 'BT PANJANG INT', 1.37812611932206, 103.763286611367]
        # print(kwargs['destinationbusstopdata'])
        # # ['972', 'SMRT', 1, 63, '45009', '39.9', '0701', '0042', '0721', '0054', '0720', '0034', 'BT PANJANG INT', 1.37812611932206, 103.763286611367]
  
        # First Header
        firstheader = FloatLayout()
        firstheaderimage = Image(source="icons/bushead.png", pos_hint={"top": 1, "right": 0.7})
        firstheaderlabel = Label(text="[color=000000]" + kwargs['thisrouteserviceno'] + "[/color]", markup = True, font_size='30sp', size_hint=(1, .2), pos_hint={"top": .55, "right": 1})
        firstheader.add_widget(firstheaderimage)
        firstheader.add_widget(firstheaderlabel)
  
        # Second Header
        secondheader = FloatLayout()
        secondheaderimage = Image(source="icons/startfinish.png", pos_hint={"top": 1, "right": 0.45})
        secondheaderlabel1 = Label(text="[color=000000]" + kwargs['originbusstopdata'][12] + "[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .85, "right": 1})
        secondheaderlabel2 = Label(text="[color=000000]" + kwargs['destinationbusstopdata'][12] + "[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .35, "right": 1})
        secondheader.add_widget(secondheaderimage)
        secondheader.add_widget(secondheaderlabel1)
        secondheader.add_widget(secondheaderlabel2)
  
        self.add_widget(firstheader)
        self.add_widget(secondheader)
        # self.add_widget(thirdheader)
  
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
  
class BusRouteGeneralBanner(MDBoxLayout):
    # rows = 1
    def __init__(self, **kwargs):
        super().__init__()
  
        try:
            image = ImageLeftWidget(source="icons/arrowdown.png")
            # Description and BusStopCode
            twolineavataritem = TwoLineAvatarListItem(text = kwargs['busstop'][12], secondary_text=kwargs['busstop'][4], on_release = partial(App.get_running_app().go_to_bus_arrival_banner_general, kwargs))
            twolineavataritem.add_widget(image)
            self.add_widget(twolineavataritem)
        except Exception as e:
            print(e)
  
  
class BusRouteGeneralBannerStartEnd(MDBoxLayout):
    # rows = 1
    def __init__(self, **kwargs):
        super().__init__()
  
        # print(kwargs['busstop'])
        # ['963', 'SMRT', 1, 51, '14009', '29.7', '0629', '0041', '0639', '0038', '0645', '0035', 'HarbourFront Int', 1.26703502614245, 103.81901469907409]
  
        # Stop sequence
        if kwargs['busstop'][3] == 1:
            firstlinetext = "START"
            iconsource = "icons/start.png"
        else:
            firstlinetext = "END"
            iconsource = "icons/finish.png"
  
        try:
            image = ImageLeftWidget(source=iconsource)
            # Description and BusStopCode
            threelineavataritem = ThreeLineAvatarListItem(text=firstlinetext, secondary_text = kwargs['busstop'][12], tertiary_text=kwargs['busstop'][4], on_release = partial(App.get_running_app().go_to_bus_arrival_banner_general, kwargs))
            threelineavataritem.add_widget(image)
            self.add_widget(threelineavataritem)
        except Exception as e:
            print(e)
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
 
class BusRouteHeader(GridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super().__init__()
 
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("c8fcf7"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
 
        # print(kwargs['thisrouteserviceno'])
        # print("originbusstopdata", kwargs['originbusstopdata'])
        # originbusstopdata ['184', 'SMRT', 1, 1, '48009', '0', '0604', '0009', '0604', '0008', '0613', '0014', 'Bt Panjang Temp Bus Pk', 1.38376399998384, 103.75829999999559, 'No']
        # print(kwargs['destinationbusstopdata'])
 
        # First Header
        firstheader = FloatLayout()
        firstheaderimage = Image(source="icons/bushead.png", pos_hint={"top": 1, "right": 0.7})
        firstheaderlabel = Label(text="[color=000000]" + kwargs['thisrouteserviceno'] + "[/color]", markup = True, font_size='30sp', size_hint=(1, .2), pos_hint={"top": .55, "right": 1})
        firstheader.add_widget(firstheaderimage)
        firstheader.add_widget(firstheaderlabel)
 
        # Second Header
        secondheader = FloatLayout()
        secondheaderimage = Image(source="icons/startfinish.png", pos_hint={"top": 1, "right": 0.45})
        # busstop description
        secondheaderlabel1 = Label(text="[color=000000]" + kwargs['originbusstopdata'][12] + "[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .85, "right": 1})
        secondheaderlabel2 = Label(text="[color=000000]" + kwargs['destinationbusstopdata'][12] + "[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .35, "right": 1})
        secondheader.add_widget(secondheaderimage)
        secondheader.add_widget(secondheaderlabel1)
        secondheader.add_widget(secondheaderlabel2)
 
        self.add_widget(firstheader)
        self.add_widget(secondheader)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
 
class BusRouteBanner(MDBoxLayout):
    # rows = 1
    nextbusEstimatedArrival = "NA"
    nextbus_estimated_arr_min = "NA"
    def __init__(self, **kwargs):
        super().__init__()
 
        # print(kwargs['busstop'])
        # ['75', 'SMRT', 1, 1, '48009', '0', '0525', '2330', '0525', '2330', '0525', '2330', 'Bt Panjang Temp Bus Pk', 1.38376399998384, 103.75829999999559, 'No']
 
        # print("busservice", kwargs['bus_route_data'])
        # busservice {'busstopcode': '43139', 'busarrivaldata': {'ServiceNo': '75', 'Operator': 'SMRT', 'NextBus': {'OriginCode': '48009', 'DestinationCode': '02099', 'EstimatedArrival': '2020-11-14T11:46:58+08:00', 'Latitude': '1.3803406666666667', 'Longitude': '103.7622765', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}, 'NextBus2': {'OriginCode': '48009', 'DestinationCode': '02099', 'EstimatedArrival': '2020-11-14T11:59:13+08:00', 'Latitude': '0', 'Longitude': '0', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}, 'NextBus3': {'OriginCode': '48009', 'DestinationCode': '02099', 'EstimatedArrival': '2020-11-14T12:14:11+08:00', 'Latitude': '0', 'Longitude': '0', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}}}
        self.nextbusEstimatedArrival = kwargs['bus_route_data']['busarrivaldata']['NextBus']['EstimatedArrival']
        self.nextbus_estimated_arr_min = self.calculate_time_difference(self.nextbusEstimatedArrival)
        #print("estimated_arr_min", estimated_arr_min)
 
        # Bus arriving
        if kwargs['busstop'][15] == "Yes":
            try:
                image = ImageLeftWidget(source="icons/arrowdown.png")
                # Description and Bus stop code
                threelineavataritem = ThreeLineAvatarListItem(text = "Arriving this stop in " + self.nextbus_estimated_arr_min, secondary_text=kwargs['busstop'][12], tertiary_text=kwargs['busstop'][4], on_release = partial(App.get_running_app().go_to_bus_arrival_banner_general, kwargs))
                threelineavataritem.add_widget(image)
                self.add_widget(threelineavataritem)
            except Exception as e:
                print(e)
        else:
            try:
                image = ImageLeftWidget(source="icons/arrowdown.png")
                # Description and Bus stop code
                twolineavataritem = TwoLineAvatarListItem(text = kwargs['busstop'][12], secondary_text=kwargs['busstop'][4], on_release = partial(App.get_running_app().go_to_bus_arrival_banner_general, kwargs))
                twolineavataritem.add_widget(image)
                self.add_widget(twolineavataritem)
            except Exception as e:
                print(e)
 
    def calculate_time_difference(self, raw_time):
        tz = pytz.timezone('Asia/Singapore')
        now = datetime.now(tz).replace(tzinfo=None)
 
        processed_time = raw_time.replace("T", " ")
        processed_time_2 = processed_time.replace("+08:00", "")
        processed_time_3 = datetime.strptime(processed_time_2, '%Y-%m-%d %X')
 
        time_delta = (processed_time_3 - now)
        total_seconds = time_delta.total_seconds()
        minute = total_seconds/60
        # Round down as per documentation suggestion
        if minute <= 0:
            rounded_minute = "Arrived"
        else:
            rounded_minute = str(math.floor(minute)) + " min"
        return rounded_minute
 
 
class BusRouteBannerStartEnd(MDBoxLayout):
    # rows = 1
    nextbusEstimatedArrival = "NA"
    nextbus_estimated_arr_min = "NA"
    def __init__(self, **kwargs):
        super().__init__()
 
        # print(kwargs['busstop'])
        # ['75', 'SMRT', 1, 1, '48009', '0', '0525', '2330', '0525', '2330', '0525', '2330', 'Bt Panjang Temp Bus Pk', 1.38376399998384, 103.75829999999559, 'No']
 
        # print("busservice", kwargs['bus_route_data'])
        # busservice {'busstopcode': '43139', 'busarrivaldata': {'ServiceNo': '75', 'Operator': 'SMRT', 'NextBus': {'OriginCode': '48009', 'DestinationCode': '02099', 'EstimatedArrival': '2020-11-14T11:46:58+08:00', 'Latitude': '1.3803406666666667', 'Longitude': '103.7622765', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}, 'NextBus2': {'OriginCode': '48009', 'DestinationCode': '02099', 'EstimatedArrival': '2020-11-14T11:59:13+08:00', 'Latitude': '0', 'Longitude': '0', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}, 'NextBus3': {'OriginCode': '48009', 'DestinationCode': '02099', 'EstimatedArrival': '2020-11-14T12:14:11+08:00', 'Latitude': '0', 'Longitude': '0', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}}}
 
        self.nextbusEstimatedArrival = kwargs['bus_route_data']['busarrivaldata']['NextBus']['EstimatedArrival']
        self.nextbus_estimated_arr_min = self.calculate_time_difference(self.nextbusEstimatedArrival)
 
        # Stop sequence
        if kwargs['busstop'][3] == 1:
            firstlinetext = "START"
            iconsource = "icons/start.png"
        else:
            firstlinetext = "END"
            iconsource = "icons/finish.png"
 
        # Bus Arriving
        if kwargs['busstop'][15] == "Yes":
            try:
                image = ImageLeftWidget(source="icons/arrowdown.png")
                # Description and Bus Stop code
                threelineavataritem = ThreeLineAvatarListItem(text = "Arriving this stop in " + self.nextbus_estimated_arr_min, secondary_text=kwargs['busstop'][12], tertiary_text=kwargs['busstop'][4], on_release = partial(App.get_running_app().go_to_bus_arrival_banner_general, kwargs))
                threelineavataritem.add_widget(image)
                self.add_widget(threelineavataritem)
            except Exception as e:
                print(e)
        else:
            try:
                image = ImageLeftWidget(source=iconsource)
                # Description and Bus Stop code
                threelineavataritem = ThreeLineAvatarListItem(text=firstlinetext, secondary_text = kwargs['busstop'][12], tertiary_text=kwargs['busstop'][4], on_release = partial(App.get_running_app().go_to_bus_arrival_banner_general, kwargs))
                threelineavataritem.add_widget(image)
                self.add_widget(threelineavataritem)
            except Exception as e:
                print(e)
 
    def calculate_time_difference(self, raw_time):
        tz = pytz.timezone('Asia/Singapore')
        now = datetime.now(tz).replace(tzinfo=None)
 
        processed_time = raw_time.replace("T", " ")
        processed_time_2 = processed_time.replace("+08:00", "")
        processed_time_3 = datetime.strptime(processed_time_2, '%Y-%m-%d %X')
 
        time_delta = (processed_time_3 - now)
        total_seconds = time_delta.total_seconds()
        minute = total_seconds/60
        # Round down as per documentation suggestion
        if minute <= 0:
            rounded_minute = "Arrived"
        else:
            rounded_minute = str(math.floor(minute)) + " min"
        return rounded_minute
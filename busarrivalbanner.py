from apikey_ import lta_account_key
from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from specialbuttons import ImageButton, LabelButton
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.app import App
import kivy.utils
import requests, json
from functools import partial
from datetime import datetime
import pytz
import math
# For snackbar
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.metrics import dp
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class BusArrivalHeader(GridLayout):
    rows = 1
 
    def __init__(self, **kwargs):
        super().__init__()
 
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("c8fcf7"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
 
        # First Header: Seats Available
        firstheader = FloatLayout()
        firstheaderimage = Image(source="icons/seatsavailable.png", size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1})
        firstheaderlabel = Label(text="[color=000000]Seats\nAvailable[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        firstheader.add_widget(firstheaderimage)
        firstheader.add_widget(firstheaderlabel)
 
        # Second Header: Standing Available
        secondheader = FloatLayout()
        secondheaderimage = Image(source="icons/standingavailable.png", size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1})
        secondheaderlabel = Label(text="[color=000000]Standing\nAvailable[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        secondheader.add_widget(secondheaderimage)
        secondheader.add_widget(secondheaderlabel)
 
        # Third Header: Limited Standing
        thirdheader = FloatLayout()
        thirdheaderimage = Image(source="icons/limitedstanding.png", size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1})
        thirdheaderlabel = Label(text="[color=000000]Limited\nStanding[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        thirdheader.add_widget(thirdheaderimage)
        thirdheader.add_widget(thirdheaderlabel)
 
        # Fourth Header: Wheelchar Accessible
        fourthheader = FloatLayout()
        fourthheaderimage = Image(source="icons/WAB.png", size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1})
        fourthheaderlabel = Label(text="[color=000000]Wheelchair\nAccessible[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        fourthheader.add_widget(fourthheaderimage)
        fourthheader.add_widget(fourthheaderlabel)
 
        self.add_widget(firstheader)
        self.add_widget(secondheader)
        self.add_widget(thirdheader)
        self.add_widget(fourthheader)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
 
class BusArrivalBanner(GridLayout):
    rows = 1
 
    bus_arrival_data = ['NA']
    nextbusOriginCode = "NA"
    nextbusDestinationCode = "NA"
    nextbusEstimatedArrival = "NA"
    nextbusLatitude = "NA"
    nextbusLongitude = "NA"
    nextbusVisitNumber = "NA"
    nextbusLoad = "NA"
    nextbusFeature = "NA"
    nextbusType = "NA"
    nextbus_estimated_arr_min = "NA"
    nextbusLoadicon = "transparent.png"
    nextbusFeatureicon = "transparent.png"
    nextbusTypeicon = "transparent.png"
 
    nextbus2OriginCode = "NA"
    nextbus2DestinationCode = "NA"
    nextbus2EstimatedArrival = "NA"
    nextbus2Latitude = "NA"
    nextbus2Longitude = "NA"
    nextbus2VisitNumber = "NA"
    nextbus2Load = "NA"
    nextbus2Feature = "NA"
    nextbus2Type = "NA"
    nextbus2_estimated_arr_min = "NA"
    nextbus2Loadicon = "transparent.png"
    nextbus2Featureicon = "transparent.png"
    nextbus2Typeicon = "transparent.png"
 
    nextbus3OriginCode = "NA"
    nextbus3DestinationCode = "NA"
    nextbus3EstimatedArrival = "NA"
    nextbus3Latitude = "NA"
    nextbus3Longitude = "NA"
    nextbus3VisitNumber = "NA"
    nextbus3Load = "NA"
    nextbus3Feature = "NA"
    nextbus3Type = "NA"
    nextbus3_estimated_arr_min = "NA"
    nextbus3Loadicon = "transparent.png"
    nextbus3Featureicon = "transparent.png"
    nextbus3Typeicon = "transparent.png"
 
    def __init__(self, **kwargs):
        super().__init__()
 
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("988be5"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
 
        #print(kwargs['busservice'])
        # print(kwargs['busstopdesc'])
 
        self.busstopcode = kwargs['busstop']
        self.busservice = kwargs['busservice']
        bus_arrival_path = "ltaodataservice/BusArrivalv2"
        parameter1_md = "?BusStopCode="
        parameter2_op = "&ServiceNo=" # eg: 15
 
        bus_arrival_url = uri + bus_arrival_path + parameter1_md + self.busstopcode + parameter2_op + self.busservice
 
        try:
            bus_arrival = requests.get(bus_arrival_url, headers=headers)
            bus_arrival_response = json.loads(bus_arrival.content)
            self.bus_arrival_data = bus_arrival_response['Services'][0]
            # print(busservice, bus_arrival_data)
 
            self.nextbusOriginCode = self.bus_arrival_data['NextBus']['OriginCode']
            self.nextbusDestinationCode = self.bus_arrival_data['NextBus']['DestinationCode']
            self.nextbusEstimatedArrival = self.bus_arrival_data['NextBus']['EstimatedArrival']
            self.nextbusLatitude = self.bus_arrival_data['NextBus']['Latitude']
            self.nextbusLongitude = self.bus_arrival_data['NextBus']['Longitude']
            self.nextbusVisitNumber = self.bus_arrival_data['NextBus']['VisitNumber']
            self.nextbusLoad = self.bus_arrival_data['NextBus']['Load']
            self.nextbusFeature = self.bus_arrival_data['NextBus']['Feature']
            self.nextbusType = self.bus_arrival_data['NextBus']['Type']
 
            self.nextbus_estimated_arr_min = self.calculate_time_difference(self.nextbusEstimatedArrival)
            #print("estimated_arr_min", estimated_arr_min)
 
            if self.nextbusLoad == "SEA":
                # SEA (for Seats Available) --> Green
                self.nextbusLoadicon = "seatsavailable.png"
            elif self.nextbusLoad == "SDA":
                # SDA (for Standing Available) --> Yellow
                self.nextbusLoadicon = "standingavailable.png"
            else:
                # LSD (for Limited Standing) --> Red
                self.nextbusLoadicon = "limitedstanding.png"
 
            if self.nextbusFeature == "WAB":
                # WAB
                self.nextbusFeatureicon = "WAB.png"
            else:
                # (empty / blank)
                self.nextbusFeatureicon = "transparent.png"
                 
            if self.nextbusType == "SD":
                # SD (for Single Deck)
                self.nextbusTypeicon= "SD.png"
            elif self.nextbusType == "DD":
                # DD (for Double Deck)
                self.nextbusTypeicon= "DD.png"
            else:
                # BD (for Bendy)
                self.nextbusTypeicon= "BD.png"
 
        except Exception as e:
            print("Arrival data not available for this next bus service", self.busservice, e)
            pass
         
        # Next bus 2
        try:
            # print(busservice, bus_arrival_data)
            self.nextbus2OriginCode = self.bus_arrival_data['NextBus2']['OriginCode']
            self.nextbus2DestinationCode = self.bus_arrival_data['NextBus2']['DestinationCode']
            self.nextbus2EstimatedArrival = self.bus_arrival_data['NextBus2']['EstimatedArrival']
            self.nextbus2Latitude = self.bus_arrival_data['NextBus2']['Latitude']
            self.nextbus2Longitude = self.bus_arrival_data['NextBus2']['Longitude']
            self.nextbus2VisitNumber = self.bus_arrival_data['NextBus2']['VisitNumber']
            self.nextbus2Load = self.bus_arrival_data['NextBus2']['Load']
            self.nextbus2Feature = self.bus_arrival_data['NextBus2']['Feature']
            self.nextbus2Type = self.bus_arrival_data['NextBus2']['Type']
 
            self.nextbus2_estimated_arr_min = self.calculate_time_difference(self.nextbus2EstimatedArrival)
            #print("estimated_arr_min", estimated_arr_min)
 
            if self.nextbus2Load == "SEA":
                # SEA (for Seats Available) --> Green
                self.nextbus2Loadicon = "seatsavailable.png"
            elif self.nextbus2Load == "SDA":
                # SDA (for Standing Available) --> Yellow
                self.nextbus2Loadicon = "standingavailable.png"
            else:
                # LSD (for Limited Standing) --> Red
                self.nextbus2Loadicon = "limitedstanding.png"
 
            if self.nextbus2Feature == "WAB":
                # WAB
                self.nextbus2Featureicon = "WAB.png"
            else:
                # (empty / blank)
                self.nextbus2Featureicon = "transparent.png"
                 
            if self.nextbus2Type == "SD":
                # SD (for Single Deck)
                self.nextbus2Typeicon= "SD.png"
            elif self.nextbus2Type == "DD":
                # DD (for Double Deck)
                self.nextbus2Typeicon= "DD.png"
            else:
                # BD (for Bendy)
                self.nextbus2Typeicon= "BD.png"
                 
        except Exception as e:
            print("Arrival data not available for this next bus 2 service", self.busservice, e)
            pass
 
        # Next bus 3
        try:
            # print(busservice, bus_arrival_data)
            self.nextbus3OriginCode = self.bus_arrival_data['NextBus3']['OriginCode']
            self.nextbus3DestinationCode = self.bus_arrival_data['NextBus3']['DestinationCode']
            self.nextbus3EstimatedArrival = self.bus_arrival_data['NextBus3']['EstimatedArrival']
            self.nextbus3Latitude = self.bus_arrival_data['NextBus3']['Latitude']
            self.nextbus3Longitude = self.bus_arrival_data['NextBus3']['Longitude']
            self.nextbus3VisitNumber = self.bus_arrival_data['NextBus3']['VisitNumber']
            self.nextbus3Load = self.bus_arrival_data['NextBus3']['Load']
            self.nextbus3Feature = self.bus_arrival_data['NextBus3']['Feature']
            self.nextbus3Type = self.bus_arrival_data['NextBus3']['Type']
 
            self.nextbus3_estimated_arr_min = self.calculate_time_difference(self.nextbus3EstimatedArrival) 
            #print("estimated_arr_min", estimated_arr_min)
 
            if self.nextbus3Load == "SEA":
                # SEA (for Seats Available) --> Green
                self.nextbus3Loadicon = "seatsavailable.png"
            elif self.nextbus3Load == "SDA":
                # SDA (for Standing Available) --> Yellow
                self.nextbus3Loadicon = "standingavailable.png"
            else:
                # LSD (for Limited Standing) --> Red
                self.nextbus3Loadicon = "limitedstanding.png"
 
            if self.nextbus3Feature == "WAB":
                # WAB
                self.nextbus3Featureicon = "WAB.png"
            else:
                # (empty / blank)
                self.nextbus3Featureicon = "transparent.png"
                 
            if self.nextbus3Type == "SD":
                # SD (for Single Deck)
                self.nextbus3Typeicon= "SD.png"
            elif self.nextbus3Type == "DD":
                # DD (for Double Deck)
                self.nextbus3Typeicon= "DD.png"
            else:
                # BD (for Bendy)
                self.nextbus3Typeicon= "BD.png"
                 
        except Exception as e:
            print("Arrival data not available for this next bus 3 service", self.busservice, e)
            pass
 
        # #print(nextbusOriginCode, nextbusDestinationCode, type(nextbusEstimatedArrival), nextbusLatitude, nextbusLongitude, nextbusVisitNumber, nextbusLoad, nextbusFeature, nextbusType)
 
        app = App.get_running_app()
        app.cursor.execute("""SELECT * FROM favourite WHERE BusStopCode = ? AND BusService = ? ;""", (self.busstopcode,  self.busservice))
        favourite = app.cursor.fetchall()
        app.connection.commit()
        # print(App.get_running_app().cursor.rowcount, "Record inserted successfully into Laptop table")
        # App.get_running_app().cursor.close()
        # print(favourite)
 
        if len(favourite) == 0:
            favourite_source = 'icons/blackstar.png'
        else:
            favourite_source = 'icons/yellowstar.png'
 
        bus_route_data = {}
        bus_route_data['busstopcode'] = self.busstopcode
        bus_route_data['busarrivaldata'] = self.bus_arrival_data
     
        # First FloatLayout: Bus Service Number
        first = FloatLayout()
        self.first_button_favourite = ImageButton(source=favourite_source, pos_hint={"top": 1, "right": 0.68})
        self.first_button_favourite.bind(on_release=self.change_favourite_data)
 
        first_button_bus_service = Button(text=kwargs['busservice'], size_hint=(0.6, 0.5), font_size='20sp', pos_hint={"top": 0.7, "right": 1}, on_release=partial(app.load_bus_route, bus_route_data))
        first.add_widget(self.first_button_favourite)
        first.add_widget(first_button_bus_service)
         
 
        # Second FloatLayout: Next Bus Arrival Estimated Minute
        second = FloatLayout()
        second_image_bus_load = ImageButton(source="icons/" + self.nextbusLoadicon, size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1}, on_release = partial(app.load_bus_route, bus_route_data))
        second_label = LabelButton(text="[color=000000]"+self.nextbus_estimated_arr_min+"[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .6, "right": 1}, on_release = partial(app.load_bus_route, bus_route_data))
        second_image_bus_type = ImageButton(source="icons/" + self.nextbusTypeicon, size_hint=(1, 0.5), pos_hint={"top": .45, "right": 0.84}, on_release = partial(app.load_bus_route, bus_route_data))
        second_image_wheel_chair = ImageButton(source="icons/" + self.nextbusFeatureicon, size_hint=(0.25, 0.25), pos_hint={"top": .35, "right": 0.84}, on_release = partial(app.load_bus_route, bus_route_data))
        second.add_widget(second_image_bus_load)
        second.add_widget(second_image_bus_type)
        second.add_widget(second_label)
        second.add_widget(second_image_wheel_chair)
 
 
        # # Third FloatLayout: Next Bus 2 Arrival Estimated Minute
        third = FloatLayout()
        third_image_bus_load = ImageButton(source="icons/" + self.nextbus2Loadicon, size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1}, on_release = partial(app.load_bus_route, bus_route_data))
        third_label = LabelButton(text="[color=000000]"+self.nextbus2_estimated_arr_min+"[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .6, "right": 1}, on_release = partial(app.load_bus_route, bus_route_data))
        third_image_bus_type = ImageButton(source="icons/" + self.nextbus2Typeicon, size_hint=(1, 0.5), pos_hint={"top": .45, "right": 0.84}, on_release = partial(app.load_bus_route, bus_route_data))
        third_image_wheel_chair = ImageButton(source="icons/" + self.nextbus2Featureicon, size_hint=(0.25, 0.25), pos_hint={"top": .35, "right": 0.84}, on_release = partial(app.load_bus_route, bus_route_data))
        third.add_widget(third_label)
        third.add_widget(third_image_bus_type)
        third.add_widget(third_image_bus_load)
        third.add_widget(third_image_wheel_chair)
 
        # # Fourth FloatLayout: Next Bus 3 Arrival Estimated Minute
        fourth = FloatLayout()
        fourth_image_bus_load = ImageButton(source="icons/" + self.nextbus3Loadicon, size_hint=(1, 0.5), pos_hint={"top": 1, "right": 1}, on_release = partial(app.load_bus_route, bus_route_data))
        fourth_label = LabelButton(text="[color=000000]"+self.nextbus3_estimated_arr_min+"[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .6, "right": 1}, on_release = partial(app.load_bus_route, bus_route_data))
        fourth_image_bus_type = ImageButton(source="icons/" + self.nextbus3Typeicon, size_hint=(1, 0.5), pos_hint={"top": .45, "right": 0.84}, on_release = partial(app.load_bus_route, bus_route_data))
        fourth_image_wheel_chair = ImageButton(source="icons/" + self.nextbus3Featureicon, size_hint=(0.25, 0.25), pos_hint={"top": .35, "right": 0.84}, on_release = partial(app.load_bus_route, bus_route_data))
        fourth.add_widget(fourth_label)
        fourth.add_widget(fourth_image_bus_type)
        fourth.add_widget(fourth_image_bus_load)
        fourth.add_widget(fourth_image_wheel_chair)
 
        self.add_widget(first)
        self.add_widget(second)
        self.add_widget(third)
        self.add_widget(fourth)
 
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
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
         
        # NA for data not available
 
    def change_favourite_data(self, instance):
        # print(self.busstopcode, self.busservice)
        if self.first_button_favourite.source == 'icons/blackstar.png':
            app = App.get_running_app()
            app.cursor.execute("""INSERT INTO favourite (BusStopCode, BusService) VALUES (?, ?);""", (self.busstopcode, self.busservice))
            app.connection.commit()
            # print("Inserted successfully")
            self.first_button_favourite.source = 'icons/yellowstar.png'
            Snackbar(text="Added to favourite successfully!", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (dp(10) * 2)) / Window.width).open()
        else:
            app = App.get_running_app()
            app.cursor.execute("""DELETE FROM favourite WHERE BusStopCode = ? AND BusService = ? ;""", (self.busstopcode, self.busservice))
            app.connection.commit()
            # print("Deleted successfull")
            self.first_button_favourite.source = 'icons/blackstar.png'
            Snackbar(text="Removed from favourite successfully!", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (dp(10) * 2)) / Window.width).open()
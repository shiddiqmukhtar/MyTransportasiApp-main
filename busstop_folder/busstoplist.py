from kivy.uix.screenmanager import Screen
from kivymd.uix.list import MDList, TwoLineListItem
from kivy.uix.scrollview import ScrollView
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
from kivy.app import App
from functools import partial
 
class BusStopList(FloatLayout):
    master_busservice_of_busstop = []
    #item -> list view -> scroll view -> screen
    def __init__(self, **kwargs):
        super().__init__()
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("988be5"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
 
        self.scroll = ScrollView()
        self.list_view = MDList()
 
        #print("busroute",kwargs['busroutes'])
        #[('28', 'SBST', 1, 17, '75069', '6.8', '0609', '0027', '0605', '0025', '0609', '0027')]
        #print("busroute",kwargs['busroutes'][:1])
        #print("busstop", kwargs['nearbybusstop'])
        #busstop [('43131', 'Cashew Rd', 'Bt Panjang Pr Sch', 1.37331749997168, 103.7700624999975), ('43139', 'Cashew Rd', 'Opp Bt Panjang Pr Sch', 1.37322530507327, 103.77029311221521), ('44211', 'Petir Rd', 'Blk 127', 1.37610015820197, 103.76921822286211)]
        self.master_busservice_of_busstop = []
 
        for busstop in kwargs['nearbybusstop']:
            busservice_of_busstop = []
            busservice_object = {}
            for busroute in kwargs['busroutes']:
                if busstop[0] == busroute[4]:
                    busservice_of_busstop.append(busroute[0])
            busservice_object['BusStopCode'] = busstop[0]
            busservice_object['Description'] = busstop[2]
            busservice_object['BusServiceofBusStopCode'] = busservice_of_busstop
            self.master_busservice_of_busstop.append(busservice_object)
 
        for eachobject in self.master_busservice_of_busstop:
            if len(eachobject['BusServiceofBusStopCode']) > 0:
                busservicestring = " ".join(eachobject['BusServiceofBusStopCode'])
            else:
                busservicestring = "Error"
            twolineitem = TwoLineListItem(text=str(eachobject['BusStopCode']) + " " + str(eachobject['Description']), secondary_text=busservicestring, on_release = partial(App.get_running_app().go_to_bus_arrival_banner, eachobject))
            self.list_view.add_widget(twolineitem)
 
        self.scroll.add_widget(self.list_view)
        self.add_widget(self.scroll)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
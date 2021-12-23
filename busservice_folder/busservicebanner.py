from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.button import Button
from kivy.graphics import Color, RoundedRectangle
from kivy.app import App
import kivy.utils
from functools import partial
from kivymd.uix.list import ThreeLineAvatarListItem, ImageLeftWidget, MDList
from kivy.uix.scrollview import ScrollView
 
class BusServiceBanner(GridLayout):
    rows = 1
    def __init__(self, **kwargs):
        super().__init__()
 
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("988be5"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
 
        # print("nearbybusservices", kwargs['nearbybusservices'])
        # nearbybusservices [('187', 'SMRT', 1, 'TRUNK', '46009', '22009', '07-09', '05-11', '07-13', '09-13', ''), ('190', 'SMRT', 2, 'TRUNK', '10499', '44009', '08-11', '04-07', '04-06', '05-08', ''), ('184', 'SMRT', 1, 'TRUNK', '48009', '48009', '06-08', '06-09', '06-09', '07-11', "C'wealth Ave West"), ('171', 'SMRT', 1, 'TRUNK', '59009', '59009', '10-12', '12-13', '10-12', '11-13', 'Upp Bt Timah Rd'), ('187', 'SMRT', 2, 'TRUNK', '22009', '46009', '06-08', '06-10', '06-09', '07-13', ''), ('190', 'SMRT', 1, 'TRUNK', '44009', '10499', '02-05', '04-07', '06-07', '07-11', ''), ('960', 'SMRT', 1, 'TRUNK', '46009', '02099', '08-09', '08-12', '10-12', '10-11', ''), ('963', 'SMRT', 2, 'TRUNK', '14009', '46009', '08-15', '06-13', '06-08', '08-13', ''), ('184', 'SMRT', 1, 'TRUNK', '48009', '48009', '06-08', '06-09', '06-09', '07-11', "C'wealth Ave West"), ('976', 'SMRT', 2, 'TRUNK', '45009', '44009', '15', '15', '15', '15', ''), ('966', 'SMRT', 1, 'TRUNK', '46009', '46009', '05-07', '05-11', '06-10', '10-13', 'Marine Parade Rd')]
 
        total_bus_stops = App.get_running_app().total_bus_stops_response
        # [('99189', 'Telok Paku Rd', "S'pore Aviation Ac", 1.3884141666958, 103.9897163888532)]
 
        self.scroll = ScrollView()
        self.list_view = MDList()
 
        busservice_list_total = []
        for busservice in kwargs['nearbybusservices']:
            busservice_list = list(busservice)
            for busstop in total_bus_stops:
                if busservice_list[4] == busstop[0]: # Origin code
                    busservice_list.append(busstop[2]) # Description
                if busservice_list[5] == busstop[0]: # Destination code
                    busservice_list.append(busstop[2]) # Description
            busservice_list_total.append(busservice_list)
         
        for busservice in busservice_list_total:           
            try:
                image = ImageLeftWidget(source="icons/SD.png")
                threelineavataritem = ThreeLineAvatarListItem(text=busservice[0], secondary_text = "Start: " + busservice[11], tertiary_text= "End: " + busservice[12], on_release = partial(App.get_running_app().load_bus_route_general, busservice))
                threelineavataritem.add_widget(image)
                self.list_view.add_widget(threelineavataritem)
            except Exception as e:
                print(e)
 
        self.scroll.add_widget(self.list_view)
        self.add_widget(self.scroll)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
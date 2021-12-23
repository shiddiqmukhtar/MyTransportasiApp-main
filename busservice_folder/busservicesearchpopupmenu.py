from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest #can also use requests, see test.py
from kivy.app import App
import certifi
from kivy.clock import Clock
 
class BusServiceSearchPopupMenu(MDInputDialog):
    title = 'Bus Service Number:'
    text_button_ok = 'Search'
    def __init__(self): 
        super().__init__()
        self.size_hint = [.9, .3]
        self.pos_hint = {"center_x": .5, "center_y": .6}
        self.events_callback = self.callback #call the callback function below
 
    def open(self):
        super().open()
        Clock.schedule_once(self.set_field_focus, 0.5)
 
    def callback(self, *args):
        serviceno = self.text_field.text
        self.get_busservice(serviceno)
 
    def get_busservice(self, serviceno):
        service_no = parse.quote(serviceno)
        self.search_bus_service(service_no)
 
    def search_bus_service(self, serviceno):
        app = App.get_running_app()
        total_bus_services = app.total_bus_services_response
        widget = None
        for busservice in total_bus_services:
            # print(busservice)
            # ('118', 'GAS', 1, 'TRUNK', '65009', '97009', '5-08', '8-12', '8-10', '09-14', '')
            if busservice[0] == str(serviceno):
                print("successfully match ServiceNo")
                app.load_bus_route_general(busservice, widget)
                break
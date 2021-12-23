from kivymd.uix.dialog import MDInputDialog
from urllib import parse
from kivy.network.urlrequest import UrlRequest 
#from apikey_ import apikey_
from kivy.app import App
import certifi
from kivy.clock import Clock
# For snackbar
from kivymd.uix.snackbar import Snackbar
from kivy.core.window import Window
from kivy.metrics import dp
 
class BusStopSearchPopupMenu(MDInputDialog):
    title = 'Singapore Area Name:'
    text_button_ok = 'Search'
    def __init__(self):
        super().__init__() 
        self.size_hint = [.9, .3]
        self.pos_hint = {"center_x": .5, "center_y": .6}
        self.events_callback = self.callback #call the callback function below
 
    def open(self):
        super().open() # super() inherits all the methods in MDInputDialog, within the open() function
        Clock.schedule_once(self.set_field_focus, 0.5)
 
    def callback(self, *args):
        address = self.text_field.text
        self.geocode_get_lat_lon(address)
 
    def geocode_get_lat_lon(self, address):
        with open('asset/app_id.txt', 'r') as f:
            app_id = f.read()
        with open('asset/app_code.txt', 'r') as f:
            app_code = f.read()
        address = parse.quote(address)
        url = "https://geocoder.api.here.com/6.2/geocode.json?searchtext=%s&app_id=%s&app_code=%s"%(address, app_id, app_code)
        UrlRequest(url, on_success=self.success, on_failure=self.failure, on_error=self.error, ca_file=certifi.where())
            # pass
            #certifi directs our apps to ssl certificate
 
    def success(self, urlrequest, result):
        print("Success")
        print(result)
        try:
            latitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Latitude']
            longitude = result['Response']['View'][0]['Result'][0]['Location']['NavigationPosition'][0]['Longitude']
            print(latitude, longitude)
            app = App.get_running_app()
            mapview = app.busstopmapview 
            mapview.center_on(latitude, longitude)
        except:
            Snackbar(text="Area not found, please try other keywords.", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (dp(10) * 2)) / Window.width).open()
            pass
 
    def error(self, urlrequest, result):
        print("Error")
        print(result)
 
    def failure(self, urlrequest, result):
        print("Failure")
        print(result)
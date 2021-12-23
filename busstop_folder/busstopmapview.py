from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from busstop_folder.busstopmarker import BusStopMarker
 
class BusStopMapView(MapView):
    getting_busstop_timer = None
    bus_stop_code = []
 
    def start_getting_busstop_in_fov(self):
        try:
            self.getting_busstop_timer.cancel()
        except:
            pass
        self.getting_busstop_timer = Clock.schedule_once(self.get_busstop_in_fov, 1)
 
    def get_busstop_in_fov(self, *args):
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        total_bus_stops = App.get_running_app().total_bus_stops_response
 
        self.bus_stop_code = []
        for busstop in total_bus_stops:
            if busstop[4] > min_lon and busstop[4] < max_lon and busstop[3] > min_lat and busstop[3] < max_lat:
                code = busstop[0]
                if code in self.bus_stop_code:
                    print("code already exist")
                    continue
                else:
                    self.add_bus_stop(busstop)
                    
        App.get_running_app().create_busstoplist_widget()
 
    def add_bus_stop(self, busstop):
        # Create the MarketMarker
        lat, lon = busstop[3], busstop[4]
        marker = BusStopMarker(lat=lat, lon=lon, source = "icons/bus-stop.png")
        marker.bus_stop_data = busstop
        # Add the BusStopMarker to the map
        self.add_widget(marker)
 
        # Send the nearby bus stop data to main
        nearbybusstop = busstop
        App.get_running_app().update_nearby_busstop(nearbybusstop)
 
        # Keep track of the bus stop code
        code = busstop[0]
        self.bus_stop_code.append(code)
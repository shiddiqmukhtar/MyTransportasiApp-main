from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from busservice_folder.busservicemarker import BusServiceMarker
from kivy.network.urlrequest import UrlRequest
from functools import partial
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class BusServiceMapView(MapView):
    getting_busservice_timer = None
    bus_stop_code = []
    bus_service_code = []
    total_bus_arrival_response = []
    total_bus_services = []
 
    def start_getting_busservice_in_fov(self):
        try:
            self.getting_busservice_timer.cancel()
        except:
            pass
        self.getting_busservice_timer = Clock.schedule_once(self.get_busservice_in_fov, 1)
 
    def get_busservice_in_fov(self, *args):
        self.min_lat, self.min_lon, self.max_lat, self.max_lon = self.get_bbox()
        while(len(self.total_bus_services)<1):
            self.total_bus_services = App.get_running_app().total_bus_services_response
            print("getting bus services information")
 
        total_bus_stops = []
        while(len(total_bus_stops) < 1):
            total_bus_stops = App.get_running_app().total_bus_stops_response
            print("getting bus stops information") 
 
        self.bus_stop_code = []
        self.bus_service_code = []
        App.get_running_app().nearby_bus_services = []
 
        try:
            # Remove old marker
            for w in self.walk():
                if w.__class__ == BusServiceMarker:
                    print("remove BusServiceMarker widget")
                    self.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
 
        for busstop in total_bus_stops:
            if busstop[4] > self.min_lon and busstop[4] < self.max_lon and busstop[3] > self.min_lat and busstop[3] < self.max_lat:
                code = busstop[0]
                if code in self.bus_stop_code:
                    continue
                else:
                    self.add_bus_stop(busstop)
 
        #{
            # "odata.metadata": "http://datamall2.mytransport.sg/ltaodataservice/$metadata#BusArrivalv2/@Element",
            # "BusStopCode": "83139",
            # "Services": [
                # {
                # "ServiceNo": "15",
                # "Operator": "GAS",
                # "NextBus": {
                # "OriginCode": "77009",
                # "DestinationCode": "77009",
                # "EstimatedArrival": "2017-06-05T14:46:27+08:00",
                # "Latitude": "1.3143508333333334",
                # "Longitude": "103.906379",
                # "VisitNumber": "1",
                # "Load": "SDA",
                # "Feature": "WAB",
                # "Type": "SD"
                # },
 
    def add_bus_stop(self, busstop):
        bus_arrival_path = "ltaodataservice/BusArrivalv2"
        parameter1_md = "?BusStopCode="
        parameter2_op = "&ServiceNo=" # eg: 15
        bus_arrival_url = uri + bus_arrival_path + parameter1_md + busstop[0]
        bus_arrived = UrlRequest(bus_arrival_url, req_headers=headers, on_success=partial(self.update_busarrival_onebusstop))
 
    def update_busarrival_onebusstop(self, *args):
        bus_arrived_response = args[1]
        code = bus_arrived_response.get("BusStopCode")
        for arrival in bus_arrived_response.get("Services"):
            nextbusServiceNo = arrival['ServiceNo']
            nextbusLatitude = arrival['NextBus']['Latitude']
            nextbusLongitude = arrival['NextBus']['Longitude']
            unique_code = nextbusServiceNo + nextbusLatitude + nextbusLongitude
            if unique_code in self.bus_service_code:
                continue
            else:
                self.add_bus_service(arrival, code)
 
        # Keep track of the Bus stop code
        self.bus_stop_code.append(code)
 
    def add_bus_service(self, arrival, busstopcode):
        # Create the BusService marker
        lat, lon = arrival['NextBus']['Latitude'], arrival['NextBus']['Longitude']
        marker = BusServiceMarker(lat=lat, lon=lon, source = "icons/bus.png")
 
        # # [('98M', 'TTS', 1, 'TRUNK', '28009', '28009', '-', '14-18', '-', '14-18', 'Corporation Rd'), ('990', 'TTS', 1, 'TRUNK', '43009', '43009', '12-12', '12-12', '12-12', '12-13', 'Jurong Gateway Rd')]
        for bus_service in self.total_bus_services:
            if bus_service[0] == arrival['ServiceNo'] and bus_service[4] == arrival['NextBus']['OriginCode'] and bus_service[5] == arrival['NextBus']['DestinationCode']:
                if float(lon) > self.min_lon and float(lon) < self.max_lon and float(lat) > self.min_lat and float(lat) < self.max_lat:
                    marker.bus_service_data = bus_service
                    # For load_bus_route later
                    App.get_running_app().update_nearby_busservice(bus_service)
                    # Add the BusServiceMarker to the map
                    self.add_widget(marker)
 
        # Keep track of the bus service code
        # Different bus stop in nearby will have the same Service No. and Bus Origin
        nextbusServiceNo = arrival['ServiceNo']
        nextbusLatitude = arrival['NextBus']['Latitude']
        nextbusLongitude = arrival['NextBus']['Longitude']
        unique_code = nextbusServiceNo + nextbusLatitude + nextbusLongitude
        self.bus_service_code.append(unique_code)
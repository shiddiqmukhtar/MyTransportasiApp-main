from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.app import App
from busroute_folder.busroutemarker import BusRouteMarkerAhead, BusRouteMarkerPassed
from busservice_folder.busservicemarker import BusServiceMarker
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class BusRouteMapView(MapView):
    def acceptroutedata(self):
        thisroutebusstopdata = App.get_running_app().this_route_busstop_data
        thisroutebusservicedata = App.get_running_app().this_route_busservice_data
        # print("thisroutebusstopdata", thisroutebusstopdata)
        # thisroutebusstopdata [['75', 'SMRT', 1, 1, '48009', '0', '0525', '2330', '0525', '2330', '0525', '2330', 'Bt Panjang Temp Bus Pk', 1.38376399998384, 103.75829999999559, 'No'], ['75', 'SMRT', 1, 2, '44049', '0.5', '0528', '2333', '0528', '2333', '0528', '2333', 'Opp Junction 10', 1.38103523807931, 103.7608578414621, 'No'], ['75', 'SMRT', 1, 3, '44251', '0.7', '0528', '2333', '0528', '2333', '0528', '2333', 'Bt Panjang Stn/Blk 604', 1.38030076722264, 103.76231669235113, 'No']
        # print("thisroutebusservicedata", thisroutebusservicedata)
        # thisroutebusservicedata ['75', 'SMRT', 1, 'TRUNK', '48009', '02099', '04-09', '08-14', '11-14', '13-16', '', '0', '0']
        try:
            for busstop in thisroutebusstopdata:
                # Bus arriving
                if busstop[15] == "Yes":
                    stopsequence = busstop[3]
            for busstop in thisroutebusstopdata:
                if busstop[3] < stopsequence:
                    # Position
                    busstop.append("Passed")
                    self.add_bus_route(busstop)
                else:
                    busstop.append("Ahead")
                    self.add_bus_route(busstop)
        except:
            busstop.append("Ahead")
            self.add_bus_route(busstop)
        #print("mapview",thisroutedata_new)
        self.add_bus_service(thisroutebusservicedata)
 
    def add_bus_route(self, busstop):
        # Create the BusRouteMarker
        # print("busstop", busstop)
        # ['75', 'SMRT', 1, 1, '48009', '0', '0525', '2330', '0525', '2330', '0525', '2330', 'Bt Panjang Temp Bus Pk', 1.38376399998384, 103.75829999999559, 'No']
        try:
            lat, lon = busstop[13], busstop[14]
            # Position
            if busstop[-1] == "Passed":
                route_marker_passed = BusRouteMarkerPassed(lat=lat, lon=lon, source = "icons/route_done.png")
                route_marker_passed.bus_route_data = busstop
                self.add_widget(route_marker_passed)
            else:
                route_marker_ahead = BusRouteMarkerAhead(lat=lat, lon=lon, source = "icons/route_notdone.png")
                route_marker_ahead.bus_route_data = busstop
                self.add_widget(route_marker_ahead)
        except Exception as e:
            print("Error", e)
            pass
 
    def add_bus_service(self, busservice):
        # print(busservice)
        # ['75', 'SMRT', 1, 'TRUNK', '48009', '02099', '04-09', '08-14', '11-14', '13-16', '', '0', '0']
        try:
            lat, lon = busservice[-2], busservice[-1]
            service_marker = BusServiceMarker(lat=lat, lon=lon, source = "icons/bus.png")
            service_marker.bus_service_data = busservice
            self.add_widget(service_marker)
        except Exception as e:
            print("Error: ", e)
            pass
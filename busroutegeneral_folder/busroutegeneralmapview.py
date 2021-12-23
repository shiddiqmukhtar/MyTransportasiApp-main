from apikey_ import lta_account_key
from kivy_garden.mapview import MapView
from kivy.app import App
from busroutegeneral_folder.busroutegeneralmarker import ThisBusRouteMarker, OppositeBusRouteMarker
from busservice_folder.busservicemarker import BusServiceMarker
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
class BusRouteGeneralMapView(MapView):
    def acceptroutedata(self):
        thisroutebusstopdata = App.get_running_app().this_route_busstop_data_general
        oppositeroutebusstopdata = App.get_running_app().opposite_route_busstop_data_general
        # print("thisroutebusstopdata", thisroutebusstopdata)
        # thisroutebusstopdata [['976', 'SMRT', 1, 1, '44009', '0', '0530', '0030', '0530', '0030', '0530', '0030', 'Choa Chu Kang Int', 1.38586897797184, 103.74578895932125], ['976', 'SMRT', 1, 2, '44461', '0.7', '0532', '0033', '0532', '0033', '0532', '0033', 'Blk 352', 1.3825705560115, 103.7430047219692],
        # print("oppositeroutebusstopdata", oppositeroutebusstopdata)
        # oppositeroutebusstopdata [['976', 'SMRT', 2, 1, '45009', '0', '0550', '0050', '0550', '0050', '0550', '0050', 'BT PANJANG INT', 1.37812611932206, 103.763286611367], ['976', 'SMRT', 2, 2, '44201', '0.6', '0552', '0052', '0552', '0052', '0552', '0052', 'Aft Petir Stn', 1.37732275970527, 103.7672668951858], ['976', 'SMRT', 2, 3, '44211', '0.9', '0554', '0054', '0554', '0054', '0554', '0054', 'Blk 127', 1.37610015820197, 103.76921822286211],
 
        try:
            for busstop in thisroutebusstopdata:
                self.add_bus_route_this(busstop)
        except:
            pass
 
        try:
            for busstop in oppositeroutebusstopdata:
                self.add_bus_route_opposite(busstop)
        except:
            pass
 
    def add_bus_route_this(self, busstop):
        # Create the BusRouteMarker
        try:
            lat, lon = busstop[13], busstop[14]
            route_marker = ThisBusRouteMarker(lat=lat, lon=lon, source = "icons/route1.png")
            route_marker.bus_route_data = busstop
            self.add_widget(route_marker)
        except Exception as e:
            print("Error", e)
            pass
 
    def add_bus_route_opposite(self, busstop):
        # Create the BusRouteMarker
        try:
            lat, lon = busstop[13], busstop[14]
            route_marker = OppositeBusRouteMarker(lat=lat, lon=lon, source = "icons/route2.png")
            route_marker.bus_route_data = busstop
            self.add_widget(route_marker)
        except Exception as e:
            print("Error", e)
            pass
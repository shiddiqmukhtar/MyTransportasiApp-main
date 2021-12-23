from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.gridlayout import MDGridLayout
from kivymd.uix.picker import MDThemePicker
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelThreeLine
# For snackbar
from kivymd.uix.snackbar import Snackbar

#from kivy.core.window import Window
from kivy.metrics import dp
from kivy.utils import platform
from kivy.clock import Clock
from kivy.network.urlrequest import UrlRequest
from kivy.properties import ObjectProperty
from kivy.uix.screenmanager import Screen, NoTransition, CardTransition

from homemapview import HomeMapView
from searchpopupmenu import SearchPopupMenu
from homegpshelper import HomeGpsHelper

from taxi_folder.taximapview import TaxiMapView

from busstop_folder.busstopbackdroplayout import BusStopBackDropLayout
from busstop_folder.busstopsearchpopupmenu import BusStopSearchPopupMenu
from busstop_folder.busstopmapview import BusStopMapView
from busstop_folder.busstoplist import BusStopList

from busservice_folder.busservicesearchpopupmenu import BusServiceSearchPopupMenu
from busservice_folder.busservicebackdroplayout import BusServiceBackDropLayout
from busservice_folder.busservicemapview import BusServiceMapView
from busservice_folder.busservicebanner import BusServiceBanner

from busarrivalbanner import BusArrivalHeader, BusArrivalBanner

from busroute_folder.busroutemapview import BusRouteMapView
from busroute_folder.busroutebackdroplayout import BusRouteBackDropLayout
from busroute_folder.busroutebanner import BusRouteBanner, BusRouteBannerStartEnd, BusRouteHeader

from busroutegeneral_folder.busroutegeneralbackdroplayout import BusRouteGeneralBackDropLayout
from busroutegeneral_folder.busroutegeneralmapview import BusRouteGeneralMapView
from busroutegeneral_folder.busroutegeneralbanner import BusRouteGeneralBanner, BusRouteGeneralBannerStartEnd, BusRouteGeneralHeader


from mrtlrt_folder.mrtlrtmapview import MrtLrtMapView

from trainservicealert import TrainServiceAlertMessage, TrainServiceAlertAffectedSegments

from trainfare import TrainFare, TrainFareTab, TrainFareThreeLineListItem

from incidents_folder.incidentsmapview import IncidentsMapView

from roadwork import RoadWork

from trafficimage_folder.trafficimagebackdroplayout import TrafficImageBackDropLayout
from trafficimage_folder.trafficimagemapview import TrafficImageMapView

from carpark_folder.carparkmapview import CarParkMapView
from carpark_folder.carparktypelabel import CarParkTypeLabel

from bicycle_folder.bicycleparkingmapview import BicycleParkingMapView

from roadopening import RoadOpening
from roadopeningexpansioncontent import RoadOpeningExpansionContent

from favouritebusarrivalbanner import FavouriteBusArrivalBannerHeader, FavouriteBusArrivalBanner
from profilephotomanager import ProfilePhotoManager

from specialbuttons import LabelButton, ImageButton

from functools import partial

#from apikey_ import lta_account_key
from apikey_ import lta_account_key, tih_api_key


import os
import sys
import sqlite3

import requests, json

from kivy.core.window import Window
#Window.size = (375, 750)


#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
 
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL


class HomeScreen(Screen):
    pass

class TaxiScreen(Screen):
    pass

class BusStopScreen(Screen):
    pass

class BusServiceScreen(Screen):
    pass

class BusArrivalScreen(Screen):
    pass

class BusRouteScreen(Screen):
    pass

class BusRouteGeneralScreen(Screen):
    pass

#-------------- start mrt-lrt ----------------#

class MrtLrtScreen(Screen):
    pass

#--------------- end mrt-lrt -----------------#

class TrainServiceAlertScreen(Screen):
    pass

class TrainMapScreen(Screen):
    pass

class TrainFareScreen(Screen):
    pass

#---------------- end train ------------------#

class IncidentsScreen(Screen):
    pass

class RoadWorkScreen(Screen):
    pass

class TrafficImageScreen(Screen):
    pass

class RoadOpeningScreen(Screen):
    pass

#------------ end RO start Fav ---------------#

class FavouriteBusServiceScreen(Screen):
    pass

#-------- end Fav start profile  -------------#

class ProfilePhotoScreen(Screen):
    pass

#-------- end pro start carpark  -------------#

class CarParkScreen(Screen):
    pass

#--------- end carpark start c  --------------#

class BicycleParkingScreen(Screen):
    pass

#--------- end bicycle start c  --------------#

 
class MainApp(MDApp):
    
    connection = None
    cursor = None
    search_menu = None
    busstopsearch_menu = None
    bussservicesearch_menu = None

    # For refreshing bus arrival
    refresh_bus_arrival = None
    busservice_of_busstop_backup = None
    path_profile_photo = None

    total_bus_stops_response  = []
    total_bus_services_response = []
    
    nearby_bus_stops = []
    nearby_bus_stops_backup = []
    nearby_bus_services = []
    
    taximapview = ObjectProperty(None)
    
    busstopmapview = ObjectProperty(None)
    
    busservicemapview = ObjectProperty(None)
    
    busroutemapview = ObjectProperty(None)
    busroutegeneralmapview = ObjectProperty(None)

    bus_arrival_header = ObjectProperty(None)
    
    mrtlrtmapview = ObjectProperty(None)
    
    incidentsmapview = ObjectProperty(None)
    
    trafficimagemapview = ObjectProperty(None)
    
    carparkmapview = ObjectProperty(None)
    
    bicycleparkingmapview = ObjectProperty(None)
 
    
    total_bus_routes_response = []
    total_bus_arrived_response = []
    
    this_route_busstop_data = []
    this_route_busservice_data = []
    
    this_route_busstop_data_general = []
    opposite_route_busstop_data_general = []
    
    total_road_works_response = []
    
    total_road_openings_response = []
    
    # For refreshing favourite bus service
    refresh_favourite_bus_service = None
    current_screen_is_favourite_screen = False
     
    current_lat = 1.304833
    current_lon = 103.831833
    
    if os.path.isfile("asset/profile_source.txt"):
        with open("asset/profile_source.txt", "r") as f:
            some_path = f.read()
            if len(some_path) > 0:
                img_source_path = some_path
            else:
                img_source_path = "empty.jpg"
    else:
        img_source_path = "empty.jpg"
        
#    def __init__(self, **kwargs):
#        super().__init__(**kwargs)
#        Window.bind(on_keyboard = self.events)
#        self.manager_open = False

    def show_theme_picker(self):
        theme_dialog = MDThemePicker()
        theme_dialog.open()
        
    def print_theme(self):
        self.cursor.execute("""SELECT * FROM theme ;""")
        current_theme = self.cursor.fetchall()
        self.connection.commit()
     
        if len(current_theme) == 0:
            self.cursor.execute("""INSERT INTO theme (primary_palette, accent_palette, theme_style) VALUES (?, ?, ?);""", (self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style))
            self.connection.commit()
        else:
            self.cursor.execute("""UPDATE theme SET primary_palette = ? , accent_palette = ? , theme_style = ? ;""", (self.theme_cls.primary_palette, self.theme_cls.accent_palette, self.theme_cls.theme_style))
            self.connection.commit()
        
#    def show_theme_picker(self):
#        if self.theme_cls.theme_style == "Light":
#            self.theme_cls.primary_palette = 'BlueGray'
#            self.theme_cls.theme_style = "Dark"
#            self.theme_cls.primary_hue = "700"
            
#        else:
#            self.theme_cls.primary_palette = 'BlueGray'
#            self.theme_cls.theme_style = "Light"
#            self.theme_cls.primary_hue = "500"
 
    def on_start(self):
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.theme_cls.primary_palette = 'BlueGray'
        self.theme_cls.primary_hue = "500"
        self.theme_cls.theme_style = "Light"
        self.theme_cls.accent_palette = "Amber"
        
        
        # Profile photo manager
        profile_photo_grid = self.root.ids.profilephoto_screen.ids.profilephotogrid
        self.profile_photo_manager = ProfilePhotoManager()
        self.profile_photo_manager_screen = self.profile_photo_manager.run()
        profile_photo_grid.add_widget(self.profile_photo_manager_screen)
 
        # Initialize GPS
        HomeGpsHelper().run()
        
        # Connect to database
        self.connection = sqlite3.connect("myapp.db")
        self.cursor = self.connection.cursor()
        
        #https://kivymd.readthedocs.io/en/latest/themes/theming/
        self.cursor.execute("""SELECT * FROM theme ;""")
        current_theme = self.cursor.fetchall()
        self.connection.commit()
         
        # print(current_theme)
        # [('Purple', 'BlueGray', 'Light')]
         
        if len(current_theme) == 0:
            self.theme_cls.primary_palette = 'BlueGray'
            self.theme_cls.accent_palette = "Amber"
            self.theme_cls.primary_hue = "500"
            self.theme_cls.theme_style = "Light"
        else:
            self.theme_cls.primary_palette = current_theme[0][0]
            self.theme_cls.accent_palette = current_theme[0][1]
            self.theme_cls.primary_hue = "500"
            self.theme_cls.theme_style = current_theme[0][2]
 
 
        # Instantiate SearchPopupMenu
        self.search_menu = SearchPopupMenu()

        # Get the total bus stops
        self.busstopsquery()
        # Instantiate the bus stop back drop
        self.busstop_backdroplayout = BusStopBackDropLayout().run()
        # Add bus stop back drop to the bus stop screen
        self.root.ids.bus_stop_screen.ids.busstopbackdrop.add_widget(self.busstop_backdroplayout)
        # Instantiate BusStopSearchPopupMenu
        self.busstopsearch_menu = BusStopSearchPopupMenu()
        
        # Get the total bus services
        self.busservicesquery()
        # Instantiate the bus service back drop
        self.busservice_backdroplayout = BusServiceBackDropLayout().run()
        # Add bus service back drop to the bus service screen
        self.root.ids.bus_service_screen.ids.busservicebackdrop.add_widget(self.busservice_backdroplayout)
        # Instantiate BusServiceSearchPopupMenu
        self.busservicesearch_menu = BusServiceSearchPopupMenu()
        
        # Get the total bus routes
        self.busroutesquery()
        # Instantiate the bus route back drop
        self.busroute_backdroplayout = BusRouteBackDropLayout().run()
        # Add bus route back drop to the bus route screen
        self.root.ids.bus_route_screen.ids.busroutebackdrop.add_widget(self.busroute_backdroplayout)
        
        # Instantiate the bus route back drop general
        self.busroutegeneral_backdroplayout = BusRouteGeneralBackDropLayout().run()
        # Add bus route back drop general to the bus route screen general
        self.root.ids.bus_route_general_screen.ids.busroutegeneralbackdrop.add_widget(self.busroutegeneral_backdroplayout)
        
        bus_arrival_header = self.root.ids.bus_arrival_screen.ids.busarrivalheadercontainer
        # For Bus Arrival Screen header
        #print(type(self.bus_arrival_header))
        newbusarrivalbannerheader = BusArrivalHeader()
        bus_arrival_header.add_widget(newbusarrivalbannerheader)
        #self.root.ids.bus_arrival_screen.ids.busarrivalheadercontainer.add_widget(BusArrivalHeader())
        
        # Train fare layout
        trainfare_layout = self.root.ids.trainfare_screen.ids.trainfarelayout
        self.trainfare = TrainFare().run()
        trainfare_layout.add_widget(self.trainfare)
        
        # Get the total road works
        self.roadworksquery()
        
        # Instantiate the traffic image backdrop
        self.trafficimage_backdroplayout = TrafficImageBackDropLayout().run()
        # Add traffic image backdrop to the traffic image screen
        self.root.ids.trafficimage_screen.ids.trafficimagebackdrop.add_widget(self.trafficimage_backdroplayout)
        
        # Get the total road openings
        self.roadopeningsquery()
        # Instantiate the road opening expansion panel
        self.roadopening_expansionpanel = RoadOpening().run()
        # Add road opening expansion panel to the traffic news screen
        self.root.ids.roadopening_screen.ids.roadopeningexpansionpanel.add_widget(self.roadopening_expansionpanel)
        
        # For Favourite Bus Arrival header
        favouriteheader = self.root.ids.favouritebusservice_screen.ids.favouriteheader
        self.favouritebusarrivalbannerheader = FavouriteBusArrivalBannerHeader()
        favouriteheader.add_widget(self.favouritebusarrivalbannerheader)
        
        # Add car park screen header
        carparkscreen_header = self.root.ids.carpark_screen.ids.carparktype
        self.carparktypeheader = CarParkTypeLabel()
        carparkscreen_header.add_widget(self.carparktypeheader)
                 
    # pass here the bus service of a particular bus stop, from busstoplist.py       
    def go_to_bus_arrival_banner(self, *args):
        # ({'BusStopCode': '43139', 'Description': 'Opp Bt Panjang Pr Sch', 'BusServiceofBusStopCode': ['184', '75', '75A']}, <kivymd.uix.list.TwoLineListItem object at 0x0000021B91A38F98>)
        bus_arrival_list = self.root.ids.bus_arrival_screen.ids.busarrivalscrollcontainer
 
        try:
            # Remove each widget in the bus arrival list
            for w in bus_arrival_list.walk():
                if w.__class__ == BusArrivalBanner:
                    #print("remove busarrival widget")
                    bus_arrival_list.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
 
        if isinstance(args[0], float):
            print("this is float")
            print("Refreshing bus arrival")
            # print(args[0])
            busservice_of_busstop = self.busservice_of_busstop_backup
 
            # For body
            for eachbusservice in busservice_of_busstop['BusServiceofBusStopCode']:
                # print(eachbusservice)
                # Instantiate the bus arrival banner
                newbusarrivalbanner = BusArrivalBanner(busstop = busservice_of_busstop['BusStopCode'], busservice = eachbusservice)
                # Add bus arrival banner to the bus arrival screen
                bus_arrival_list.add_widget(newbusarrivalbanner)
             
            self.root.ids.titlename.title = str(busservice_of_busstop['BusStopCode']) + " Buses Arrival Timing"
 
        else:
            print("this is not float")
            print("First load")
            busservice_of_busstop = args[0]
            self.busservice_of_busstop_backup = busservice_of_busstop
 
            # For body
            for eachbusservice in busservice_of_busstop['BusServiceofBusStopCode']:
                # print(eachbusservice)
                # Instantiate the bus arrival banner
                newbusarrivalbanner = BusArrivalBanner(busstop = busservice_of_busstop['BusStopCode'], busservice = eachbusservice)
                # Add bus arrival banner to the bus arrival screen
                bus_arrival_list.add_widget(newbusarrivalbanner)
             
            self.root.ids.titlename.title = str(busservice_of_busstop['BusStopCode']) + " Buses Arrival Timing"
            self.change_screen("bus_arrival_screen", direction='down', mode='push')
        
    def go_to_bus_arrival_banner_general(self, *args):
        bus_arrival_list = self.root.ids.bus_arrival_screen.ids.busarrivalscrollcontainer
     
        try:
            # Remove each widget in the bus arrival list
            for w in bus_arrival_list.walk():
                if w.__class__ == BusArrivalBanner:
                    #print("remove busarrival widget")
                    bus_arrival_list.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
     
        busdata = args[0]
        # Bus stop code
        code = busdata['busstop'][4]
        # Direction
        direction = busdata['busstop'][2]
        #print("busstop", code)
                 
        # create a new banner. For each bus stop and each bus service,
        busservice_of_busstop = []
        busservice_object = {}
        for busroute in self.total_bus_routes_response:
            # print(busroute)
            # ('167', 'SMRT', 2, 68, '58339', '28.8', '0713', '0105', '0659', '0105', '0713', '0057')
            # Bus stop code and direction
            if code == busroute[4] and direction == busroute[2]:
                busservice_of_busstop.append(busroute[0]) # Service no
        busservice_object['BusStopCode'] = code
        busservice_object['BusServiceofBusStopCode'] = busservice_of_busstop
        self.busservice_of_busstop_backup = busservice_object
     
        # For body
        for eachbusservice in busservice_object['BusServiceofBusStopCode']:
            # Instantiate the bus arrival banner
            newbusarrivalbanner = BusArrivalBanner(busstop = code, busservice = eachbusservice)
            # Add bus arrival banner to the bus arrival screen
        bus_arrival_list.add_widget(newbusarrivalbanner)
     
        self.root.ids.titlename.title = code + " Buses Arrival Timing"
        self.change_screen("bus_arrival_screen", direction='down', mode='push')

        
    def busstopsquery(self):
        self.cursor.execute("""SELECT * FROM busstops ;""")
        self.total_bus_stops_response = self.cursor.fetchall()
        self.connection.commit()
        
    def busservicesquery(self):
        self.cursor.execute("""SELECT * FROM busservices ;""")
        self.total_bus_services_response = self.cursor.fetchall()
        # [('98M', 'TTS', 1, 'TRUNK', '28009', '28009', '-', '14-18', '-', '14-18', 'Corporation Rd'), ('990', 'TTS', 1, 'TRUNK', '43009', '43009', '12-12', '12-12', '12-12', '12-13', 'Jurong Gateway Rd')]
        self.connection.commit()
        
    def busroutesquery(self):
        self.cursor.execute("""SELECT * FROM busroutes ;""")
        self.total_bus_routes_response = self.cursor.fetchall()
        # [('125', 'SBST', 1, 39, '60099', '13.4', '0612', '2343', '0611', '2339', '0611', '2339')]
        self.connection.commit()
                                
    # Call by clicking on on_open on bus service back drop front layer
    def create_busservicelist_widget(self):
        bus_service_list = self.busservice_backdroplayout.ids.container
             
        try:
            # Remove busservicemapview widget
            for w in bus_service_list.walk():
                if w.__class__ == BusServiceBanner:
                    #print("remove bus service banner widget")
                    bus_service_list.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
                     
        busservicebanner = BusServiceBanner(nearbybusservices = self.nearby_bus_services)
        bus_service_list.add_widget(busservicebanner)
                               
    def create_busstoplist_widget(self):
        bus_stop_list = self.busstop_backdroplayout.ids.container
        try:
            # Remove each widget in the bus stop list
            for w in bus_stop_list.walk():
                if w.__class__ == BusStopList:
                    #print("remove busstoplist widget")
                    bus_stop_list.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
      
        # Instantiate the bus stop list
        newbusstoplist = BusStopList(busroutes = self.total_bus_routes_response, nearbybusstop = self.nearby_bus_stops)
        # Add bus stop list to the bus stop back drop
        bus_stop_list.add_widget(newbusstoplist)
 
        self.nearby_bus_stops = []
 
    def update_total_busarrival_main(self, *args):
        #access second member of tuple
        bus_arrived_response = args[1]
        self.total_bus_arrived_response += bus_arrived_response.get("Services")
        
    # call from bus service screen
    def load_bus_route_general(self, bus_service_data, widget):
        # print("bus_route_general_data", bus_service_data)
        # bus_route_general_data ('184', 'SMRT', 1, 'TRUNK', '48009', '48009', '06-08', '06-09', '06-09', '07-11', "C'wealth Ave West")
        total_bus_stops = []
        total_route_data = []
        while(len(total_bus_stops) < 1):
            total_bus_stops = self.total_bus_stops_response
     
        while(len(total_route_data) < 1):
            total_route_data = self.total_bus_routes_response
     
        thisrouteserviceno = bus_service_data[0]
        thisrouteorigin = bus_service_data[4]
     
        thisroutedirection = 1
        thisservicebothwayroutedata = []
        for routedata in total_route_data:
            # Service No
            if routedata[0] == thisrouteserviceno:
                thisservicebothwayroutedata.append(routedata)
             
        for routedata in thisservicebothwayroutedata:
            # Bus stop code and Stop sequence
            if routedata[4] == thisrouteorigin and routedata[3] == 1:
                thisroutedirection = routedata[2] # Direction
                print("thisroutedirection", thisroutedirection)
                print("thissrouteserviceno", thisrouteserviceno)
                break
             
        thisroutebusstopdata = []
        oppositeroutebusstopdata = []
        for routedata in thisservicebothwayroutedata:
            if routedata[2] == thisroutedirection: # Direction
                thisroutebusstopdata.append(routedata)
            else:
                oppositeroutebusstopdata.append(routedata)
     
        # This Route
        thisroutebusstopdata_new = []
        for data in thisroutebusstopdata:
            data_this_list = list(data)
            for busstop in total_bus_stops:
                if data_this_list[4] == busstop[0]: # Bus stop code
                    data_this_list.append(busstop[2]) # Description
                    data_this_list.append(busstop[3]) # Latitude
                    data_this_list.append(busstop[4]) # Longitude
            thisroutebusstopdata_new.append(data_this_list)
     
        # Opposite Route
        oppositeroutebusstopdata_new = []
        for data in oppositeroutebusstopdata:
            data_opposite_list = list(data)
            for busstop in total_bus_stops:
                if data_opposite_list[4] == busstop[0]: # Bus stop code
                    data_opposite_list.append(busstop[2]) # Description
                    data_opposite_list.append(busstop[3]) # Latitude
                    data_opposite_list.append(busstop[4]) # Longitude
            oppositeroutebusstopdata_new.append(data_opposite_list)
         
        # print("thisroutedata_new", thisroutedata_new)
        self.this_route_busstop_data_general = thisroutebusstopdata_new
        self.opposite_route_busstop_data_general = oppositeroutebusstopdata_new
     
        self.change_screen("bus_route_general_screen", direction='down', mode='push')
        
        bus_route_general_backdropfrontlayer = self.busroutegeneral_backdroplayout.ids.frontlayer
 
        try:
            # Remove each widget in the bus route back drop frontlayer
            for w in bus_route_general_backdropfrontlayer.walk():
                if w.__class__ == BusRouteGeneralHeader or w.__class__ == BusRouteGeneralBannerStartEnd or w.__class__ == BusRouteGeneralBanner:
                    #print("remove busroutebanner general widget")
                    bus_route_general_backdropfrontlayer.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
         
        # Create busroutebanner header
        try:
            busroutebannerheader = BusRouteGeneralHeader(thisrouteserviceno = thisrouteserviceno, originbusstopdata = thisroutebusstopdata_new[0], destinationbusstopdata = thisroutebusstopdata_new[-1])
            bus_route_general_backdropfrontlayer.add_widget(busroutebannerheader)
        except Exception as e:
            print(e)
            pass
         
        # This route
        # Create busroutebanner body
        for busstop in thisroutebusstopdata_new[:-1]:
            # Stop sequence
            if busstop[3] == 1:
                busroutebannerstart = BusRouteGeneralBannerStartEnd(busstop = busstop)
                bus_route_general_backdropfrontlayer.add_widget(busroutebannerstart)
            else:
                busroutebanner = BusRouteGeneralBanner(busstop = busstop)
                bus_route_general_backdropfrontlayer.add_widget(busroutebanner)
        try:
            busroutebannerend = BusRouteGeneralBannerStartEnd(busstop = thisroutebusstopdata_new[-1])
            bus_route_general_backdropfrontlayer.add_widget(busroutebannerend)
        except Exception as e:
            print(e)
            pass
         
        # Opposite route
        # Create busroutebanner header
        if len(oppositeroutebusstopdata_new) > 0:
            try:
                busroutebannerheader2 = BusRouteGeneralHeader(thisrouteserviceno = thisrouteserviceno, originbusstopdata = oppositeroutebusstopdata_new[0], destinationbusstopdata = oppositeroutebusstopdata_new[-1])
                bus_route_general_backdropfrontlayer.add_widget(busroutebannerheader2)
            except Exception as e:
                print(e)
                pass
         
            # Create busroutebanner body
            for busstop in oppositeroutebusstopdata_new[:-1]:
                # Stop sequence
                if busstop[3] == 1:
                    busroutebannerstart2 = BusRouteGeneralBannerStartEnd(busstop = busstop)
                    bus_route_general_backdropfrontlayer.add_widget(busroutebannerstart2)
                else:
                    busroutebanner2 = BusRouteGeneralBanner(busstop = busstop)
                    bus_route_general_backdropfrontlayer.add_widget(busroutebanner2)
            try:
                busroutebannerend2 = BusRouteGeneralBannerStartEnd(busstop = oppositeroutebusstopdata_new[-1])
                bus_route_general_backdropfrontlayer.add_widget(busroutebannerend2)
            except Exception as e:
                print(e)
                pass
         
        self.root.ids.titlename.title = "Routes of " + thisrouteserviceno
            
    def update_nearby_busstop(self, *args):
        # pass here from busstopmapview.py
        self.nearby_bus_stops.append(args[0])
        
    def update_nearby_busservice(self, *args):
        # pass here from busservicemapview.py
        self.nearby_bus_services.append(args[0])
        # print(args)
        # (('184', 'SMRT', 1, 'TRUNK', '48009', '48009', '06-08', '06-09', '06-09', '07-11', "C'wealth Ave West"),)
        
    # call from bus arrival screen
    def load_bus_route(self, bus_route_data, widget):
        # print(bus_route_data)
        # {'busstopcode': '44211', 'busarrivaldata': {'ServiceNo': '171', 'Operator': 'SMRT', 'NextBus': {'OriginCode': '59009', 'DestinationCode': '59009', 'EstimatedArrival': '2020-11-07T12:55:12+08:00', 'Latitude': '1.379011', 'Longitude': '103.76429316666666', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}, 'NextBus2': {'OriginCode': '59009', 'DestinationCode': '59009', 'EstimatedArrival': '2020-11-07T13:04:56+08:00', 'Latitude': '1.3769101666666668', 'Longitude': '103.77689583333333', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}, 'NextBus3': {'OriginCode': '59009', 'DestinationCode': '59009', 'EstimatedArrival': '2020-11-07T13:19:16+08:00', 'Latitude': '1.4139145', 'Longitude': '103.82324483333333', 'VisitNumber': '1', 'Load': 'SEA', 'Feature': 'WAB', 'Type': 'SD'}}}
        # {'busstopcode': '43139', 'busarrivaldata': ['NA']}
     
        if bus_route_data['busarrivaldata'] == ['NA']:
            print("No route data")
        else:
            total_bus_stops = self.total_bus_stops_response
            total_route_data = self.total_bus_routes_response
            total_bus_services = self.total_bus_services_response
     
            thisrouteserviceno = bus_route_data['busarrivaldata']['ServiceNo']
            thisrouteorigin = bus_route_data['busarrivaldata']['NextBus']['OriginCode']
     
            # Make sure the direction and service no.
            thisroutedirection = 1
            for routedata in total_route_data:
                if routedata[0] == thisrouteserviceno and routedata[4] == thisrouteorigin and routedata[3] == 1:
                    thisroutedirection = routedata[2]
                    # print("thisroutedirection", thisroutedirection)
                    # print("thissrouteserviceno", thisrouteserviceno)
                    break
                     
            thisroutebusstopdata = []
            for routedata in total_route_data:
                if routedata[0] == thisrouteserviceno and routedata[2] == thisroutedirection:
                    thisroutebusstopdata.append(routedata)
     
            #print(thisroutedata)
            thisroutebusstopdata_new = []
            for data in thisroutebusstopdata:
                data_list = list(data)
                for busstop in total_bus_stops:
                    if data_list[4] == busstop[0]: # Bus stop code
                        data_list.append(busstop[2]) # Description
                        data_list.append(busstop[3]) # Latitude
                        data_list.append(busstop[4]) # Longitude
                        # Arriving bus stop
                        if data_list[4] == bus_route_data['busstopcode']:
                            data_list.append("Yes")
                        # Other bus stop
                        else:
                            data_list.append("No")
                thisroutebusstopdata_new.append(data_list)
     
            # To get bus service data
            for busservice in total_bus_services:
                busservice_list = list(busservice)
                if busservice[0] == thisrouteserviceno and busservice[2] == thisroutedirection:
                    busservice_list.append(bus_route_data['busarrivaldata']['NextBus']['Latitude'])
                    busservice_list.append(bus_route_data['busarrivaldata']['NextBus']['Longitude'])
                    thisroutebusservicedata = busservice_list
     
            # print("thisroutedata_new", thisroutedata_new)
            self.this_route_busstop_data = thisroutebusstopdata_new
            self.this_route_busservice_data = thisroutebusservicedata
            # print("thisroutebusstopdata_new", thisroutebusstopdata_new)
            # thisroutebusstopdata_new [['75', 'SMRT', 1, 1, '48009', '0', '0525', '2330', '0525', '2330', '0525', '2330', 'Bt Panjang Temp Bus Pk', 1.38376399998384, 103.75829999999559, 'No'], ['75', 'SMRT', 1, 2, '44049', '0.5', '0528', '2333', '0528', '2333', '0528', '2333', 'Opp Junction 10', 1.38103523807931, 103.7608578414621, 'No'], ['75', 'SMRT', 1, 3, '44251', '0.7', '0528', '2333', '0528', '2333', '0528', '2333', 'Bt Panjang Stn/Blk 604', 1.38030076722264, 103.76231669235113, 'No'], ['75', 'SMRT', 1, 4, '44739', '1.1', '0530', '2335', '0530', '2334', '0530', '2334', 'Blk 180', 1.37876549999936, 103.76459849996492, 'No'], ['75', 'SMRT', 1, 5, '44201', '1.5', '0532', '2337', '0532', '2336', '0532', '2336', 'Aft Petir Stn', 1.37732275970527, 103.7672668951858, 'No'], ['75', 'SMRT', 1, 6, '44211', '1.8', '0532', '2337', '0532', '2336', '0532', '2336', 'Blk 127', 1.37610015820197, 103.76921822286211, 'No']]
            self.root.ids.titlename.title = "Routes of " + thisrouteserviceno + " Arriving " + bus_route_data['busstopcode']
            self.change_screen("bus_route_screen", direction='down', mode='push')
            
            
            
            bus_route_backdropfrontlayer = self.busroute_backdroplayout.ids.frontlayer
 
            try:
                # Remove each widget in the bus route back drop frontlayer
                for w in bus_route_backdropfrontlayer.walk():
                    if w.__class__ == BusRouteHeader or w.__class__ == BusRouteBannerStartEnd or w.__class__ == BusRouteBanner:
                        #print("remove busroutebanner widget")
                        bus_route_backdropfrontlayer.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            # Create busroutebanner header
            busroutebannerheader = BusRouteHeader(thisrouteserviceno = thisrouteserviceno, originbusstopdata = thisroutebusstopdata_new[0], destinationbusstopdata = thisroutebusstopdata_new[-1])
            bus_route_backdropfrontlayer.add_widget(busroutebannerheader)
             
            # Create busroutebanner body
            for busstop in thisroutebusstopdata_new[:-1]:
                # Stop sequence
                if busstop[3] == 1:
                    self.busroutebannerstart = BusRouteBannerStartEnd(busstop = busstop, bus_route_data = bus_route_data)
                    bus_route_backdropfrontlayer.add_widget(self.busroutebannerstart)
                else:
                    self.busroutebanner = BusRouteBanner(busstop = busstop, bus_route_data = bus_route_data)
                    bus_route_backdropfrontlayer.add_widget(self.busroutebanner)
            self.busroutebannerend = BusRouteBannerStartEnd(busstop = thisroutebusstopdata_new[-1], bus_route_data = bus_route_data)
            bus_route_backdropfrontlayer.add_widget(self.busroutebannerend)
            
    def on_trainfare_tab_switch(self, instance_tabs, instance_tab, instance_tab_label, tab_text):
        '''Called when switching tabs.
     
        :type instance_tabs: <kivymd.uix.tab.MDTabs object>;
        :param instance_tab: <__main__.Tab object>;
        :param instance_tab_label: <kivymd.uix.tab.MDTabsLabel object>;
        :param tab_text: text or name icon of tab;
        '''
     
        trainfareurl = f"https://tih-api.stb.gov.sg/transport/v1/fare/mrt-lrt/type/{tab_text}?apikey="
        train_fare = requests.get(trainfareurl + tih_api_key )
        train_fare_response = json.loads(train_fare.content)
        #print(train_fare_response['data'])
     
        instance_tab_content = instance_tab.ids.content
     
        try:
            # Remove instance tab scroll view widget
            for w in instance_tab_content.walk():
                if w.__class__ == TrainFareThreeLineListItem:
                    #print("remove instance_tab_content widget")
                    instance_tab_content.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
     
        for train_fare in train_fare_response['data']:
            instance_tab_content.add_widget(TrainFareThreeLineListItem(train_fare = train_fare))
            
    def roadworksquery(self):
        road_works_path = "ltaodataservice/RoadWorks"
        road_works_skip = '?$skip='
         
        if len(self.total_road_works_response) == 0:
            for i in range(0, 14):
                if i == 0:
                    road_works_url = uri + road_works_path
                    road_works = UrlRequest(road_works_url, req_headers=headers, on_success=partial(self.update_total_roadworks))
                else:
                    road_works_url = uri + road_works_path + road_works_skip + str(i*500)
                    road_works = UrlRequest(road_works_url, req_headers=headers, on_success=partial(self.update_total_roadworks))
     
    def update_total_roadworks(self, *args):
        #access second member of tuple
        road_works_response = args[1]
        self.total_road_works_response += road_works_response.get("value")
        
    def roadopeningsquery(self):
        road_openings_path = "ltaodataservice/RoadOpenings"
        road_openings_skip = '?$skip='
         
        if len(self.total_road_openings_response) == 0:
            for i in range(0, 3):
                if i == 0:
                    road_openings_url = uri + road_openings_path
                    road_openings = UrlRequest(road_openings_url, req_headers=headers, on_success=partial(self.update_total_roadopenings))
                else:
                    road_openings_url = uri + road_openings_path + road_openings_skip + str(i*500)
                    road_openings = UrlRequest(road_openings_url, req_headers=headers, on_success=partial(self.update_total_roadopenings))
     
    def update_total_roadopenings(self, *args):
        #access second member of tuple
        road_openings_response = args[1]
        self.total_road_openings_response += road_openings_response.get("value")
        
    def go_to_favourite_bus(self, *args):
        favouritebody = self.root.ids.favouritebusservice_screen.ids.favouritebody
        try:
            for w in favouritebody.walk():
                if w.__class__ == FavouriteBusArrivalBanner:
                    favouritebody.remove_widget(w)
                else:
                    continue
        except:
            print("Something is wrong")
            pass
     
        # For body
        self.cursor.execute("""SELECT * FROM favourite ;""")
        favourites = self.cursor.fetchall()
        self.connection.commit()
     
        for favourite in favourites:
            newbusarrivalbanner = FavouriteBusArrivalBanner(busstop = favourite[0], busservice = favourite[1])
            favouritebody.add_widget(newbusarrivalbanner)
     
        if self.current_screen_is_favourite_screen == False:
            # print("First load")
            self.root.ids.titlename.title = "Favourite Bus Service"
            self.current_screen_is_favourite_screen = True
            self.change_screen("favouritebusservice_screen", direction='down', mode='push')
        else:
            #print(args[0])
            print("Refreshing")
            
    def remove_item(self, instance, *args):
        # print(instance)
        # {'busstop': '44219', 'busservice': '960'}
        # print(args)
        # (<specialbuttons.LabelButton object at 0x0000019BD7613AC8>,)
     
        favouritebody = self.root.ids.favouritebusservice_screen.ids.favouritebody
        try:
            for w in favouritebody.walk():
                if w.__class__ == FavouriteBusArrivalBanner:
                    if w.busstopcode == instance['busstop'] and w.busservice == instance['busservice']:
                        #print("remove favouritebusarrivalbanner widget")
                        favouritebody.remove_widget(w)
                else:
                    continue
                    #print("No widget to remove")
        except:
            print("Something is wrong")
            pass
     
        self.cursor.execute("""DELETE FROM favourite WHERE BusStopCode = ? AND BusService = ? ;""", (instance['busstop'], instance['busservice']))
        self.connection.commit()
     
        Snackbar(text="Removed from favourite successfully!", snackbar_x="10dp", snackbar_y="10dp", size_hint_x=(Window.width - (dp(10) * 2)) / Window.width).open()
        
    def change_profile_source(self, path):
        #self.root.ids.profile.source = "C:"+path # For computer
        self.root.ids.profile.source = path # For mobile phone
        self.root.ids.nav_drawer.toggle_nav_drawer()
        with open("asset/profile_source.txt", "w") as f:
            f.write(path) # For mobile phone
            #f.write("C:"+path) # For computer
        
    def navigation_draw(self, args):
        print("Navigation")
        

#    def events(self, instance, keyboard, keycode, text, modifiers):
#        '''Called when buttons are pressed on the mobile device.'''
#        print(keycode)
#        if keyboard in (1001, 27):
#            toast("Press two times to quit..!")
#        return True

    def touch_event(self, touch):
        # Override Scatter's `on_touch_down` behavior for mouse scroll
        scatter_ = self.root.ids.trainmap_screen.ids.scatter
        if touch.is_mouse_scrolling:
            if touch.button == 'scrolldown':
                if scatter_.scale < 20:
                    scatter_.scale = scatter_.scale * 1.1
            elif touch.button == 'scrollup':
                if scatter_.scale > 1:
                    scatter_.scale = scatter_.scale * 0.8
        # If some other kind of "touch": Fall back on Scatter's behavior
        else:
            print("nothing happen")
 
    def change_screen(self, screen_name, direction='forward', mode = ""):
        # Get the screen manager from the kv file.
        screen_manager = self.root.ids.screen_manager
 
        if direction == "None":
            screen_manager.transition = NoTransition()
            screen_manager.current = screen_name
            return
 
        screen_manager.transition = CardTransition(direction=direction, mode=mode)
        screen_manager.current = screen_name
 
        if screen_name == "home_screen":
            self.root.ids.titlename.title = "Sg Transport"
            
            
        if screen_name == "taxi_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Nearby Taxi"
            taxiscreen_mapview = self.root.ids.taxi_screen.ids.taximapview
 
            try:
                # Remove taximapview widget
                for w in taxiscreen_mapview.walk():
                    if w.__class__ == TaxiMapView:
                        #print("remove busroutemapview widget")
                        taxiscreen_mapview.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass

            self.taximapview = TaxiMapView()
            taxiscreen_mapview.add_widget(self.taximapview)

            from taxi_folder.taxigpshelper import TaxiGpsHelper
            TaxiGpsHelper().run()

            self.taximapview.center_on(self.current_lat, self.current_lon)
            
            
        if screen_name == "bus_stop_screen":
            
            self.create_busstoplist_widget()
            
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Bus Stops"
            self.root.ids.bus_stop_screen.ids.busstoptoolbar.ids.label_title.font_size = '13sp'

            bus_stop_backdropfrontlayer = self.busstop_backdroplayout.ids.frontlayer
            
            try:
                # Remove busstopmapview widget
                for w in bus_stop_backdropfrontlayer.walk():
                    if w.__class__ == BusStopMapView:
                        #print("remove busstopmapview widget")
                        bus_stop_backdropfrontlayer.remove_widget(w)
                    else:
                        continue
            except:
                print("Something is wrong")
                pass
 
            self.busstopmapview = BusStopMapView()
            bus_stop_backdropfrontlayer.add_widget(self.busstopmapview)
             
            self.busstopmapview.center_on(self.current_lat, self.current_lon)
            
            from busstop_folder.busstopgpshelper import BusStopGpsHelper
            BusStopGpsHelper().run()
            
            
        if screen_name == "bus_service_screen":
            print("Screen name is ", screen_name)
            self.manager_open = True
            self.root.ids.titlename.title = "Bus Services"
            self.root.ids.bus_service_screen.ids.busservicetoolbar.ids.label_title.font_size = '13sp'
    
            bus_service_backdropfrontlayer = self.busservice_backdroplayout.ids.frontlayer

            try:
                # Remove busservicemapview widget
                for w in bus_service_backdropfrontlayer.walk():
                    if w.__class__ == BusServiceMapView:
                        #print("remove busservicemapview widget")
                        bus_service_backdropfrontlayer.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
 
            self.busservicemapview = BusServiceMapView()
            bus_service_backdropfrontlayer.add_widget(self.busservicemapview)
            self.busservicemapview.center_on(self.current_lat, self.current_lon)
            
            from busservice_folder.busservicegpshelper import BusServiceGpsHelper
            BusServiceGpsHelper().run()
            
        if screen_name == "bus_arrival_screen":
            print("Screen name is ", screen_name)
            self.refresh_bus_arrival = Clock.schedule_interval(self.go_to_bus_arrival_banner, 60)
            
        if screen_name !=  "bus_arrival_screen" and self.refresh_bus_arrival != None:
            self.refresh_bus_arrival.cancel()
            
            
        if screen_name == "bus_route_screen":
            print("Screen name is ", screen_name)
            self.busroute_backdroplayout.ids.backdrop.open(-Window.height / 3.3)
            
            bus_route_backdropbacklayer = self.busroute_backdroplayout.ids.container
            try:
                # Remove busroutemapview widget
                for w in bus_route_backdropbacklayer.walk():
                    if w.__class__ == BusRouteMapView:
                        #print("remove busroutemapview widget")
                        bus_route_backdropbacklayer.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            self.busroutemapview = BusRouteMapView()
            bus_route_backdropbacklayer.add_widget(self.busroutemapview)
             
            self.busroutemapview.center_on(self.current_lat, self.current_lon)
            
            from busroute_folder.busroutegpshelper import BusRouteGpsHelper
            BusRouteGpsHelper().run()
            
        if screen_name !=  "bus_route_screen":
            self.this_route_busservice_data = []
            self.this_route_busstop_data = []
            
            
        if screen_name == "bus_route_general_screen":
            print("Screen name is ", screen_name)
            self.busroutegeneral_backdroplayout.ids.backdrop.open(-Window.height / 3.3)
            
            bus_route_general_backdropbacklayer = self.busroutegeneral_backdroplayout.ids.container
            
            try:
                # Remove busroutegeneralmapview widget
                for w in bus_route_general_backdropbacklayer.walk():
                    if w.__class__ == BusRouteGeneralMapView:
                        #print("remove busroutegeneralmapview widget")
                        bus_route_general_backdropbacklayer.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            self.busroutegeneralmapview = BusRouteGeneralMapView()
            bus_route_general_backdropbacklayer.add_widget(self.busroutegeneralmapview)
             
            self.busroutegeneralmapview.center_on(self.current_lat, self.current_lon)
            
            from busroutegeneral_folder.busroutegeneralgpshelper import BusRouteGeneralGpsHelper
            BusRouteGeneralGpsHelper().run()
            
        if screen_name !=  "bus_route_general_screen":
            self.this_route_busstop_data_general  = []
            self.opposite_route_busstop_data_general = []
            
            
        if screen_name == "profile_photo_screen":
            print("Screen name is ", screen_name)
            
#------------------ mrt-lrt ------------------#
          
        if screen_name == "mrtlrt_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "MRT LRT"
            mrtlrtscreen_mapview = self.root.ids.mrtlrt_screen.ids.mrtlrtmapview
            
            try:
                # Remove mrtlrtmapview widget
                for w in mrtlrtscreen_mapview.walk():
                    if w.__class__ == MrtLrtMapView:
                        #print("remove mrt lrt mapviiew widget")
                        mrtlrtscreen_mapview.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            self.mrtlrtmapview = MrtLrtMapView()
            mrtlrtscreen_mapview.add_widget(self.mrtlrtmapview)
            
            from mrtlrt_folder.mrtlrtgpshelper import MrtLrtGpsHelper
            MrtLrtGpsHelper().run()
             
            self.mrtlrtmapview.center_on(self.current_lat, self.current_lon)
            
        if screen_name == "trainservicealert_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Train Service Alert"
            trainservicealert_grid = self.root.ids.trainservicealert_screen.ids.trainservicealertgrid
          
            train_service_alerts_path = "ltaodataservice/TrainServiceAlerts"
            train_service_alerts_url = uri + train_service_alerts_path
            train_service_alerts = requests.get(train_service_alerts_url, headers=headers)
            train_service_alerts_response = json.loads(train_service_alerts.content)
         
            sample_data = {
                "value": 
                    {
                        "Status": 2,
                        "AffectedSegments": [
                            {
                                "Line": "NEL",
                                "Direction": "Punggol",
                                "Stations": "NE1,NE3,NE4,NE5,NE6",
                                "FreePublicBus": "NE1,NE3,NE4,NE5,NE6",
                                "FreeMRTShuttle": "NE1,NE3,NE4,NE5,NE6",
                                "MRTShuttleDirection": "Punggol"
                            },
                            {
                                "Line": "NEL",
                                "Direction": "Punggol",
                                "Stations": "NE1,NE3,NE4,NE5,NE6",
                                "FreePublicBus": "NE1,NE3,NE4,NE5,NE6",
                                "FreeMRTShuttle": "NE1,NE3,NE4,NE5,NE6",
                                "MRTShuttleDirection": "Punggol"
                            }
                        ],
                        "Message": [
                            {
                                "Content": "1710hrs: NEL – No train service between Harbourfront to Dhoby Ghaut stations towards Punggol station due to a signalling fault. Free bus rides are available at designated bus stops.",
                                "CreatedDate": "2017-12-01 17:54:21"
                            },
                            {
                                "Content": "1710hrs: NEL – No train service between Harbourfront to Dhoby Ghaut stations towards Punggol station due to a signalling fault. Free bus rides are available at designated bus stops.",
                                "CreatedDate": "2017-12-01 17:54:21"
                            }
                        ]
                    }
                }
         
            affectedsegment_na_data = {
                                "Line": "NA",
                                "Direction": "NA",
                                "Stations": "NA",
                                "FreePublicBus": "NA",
                                "FreeMRTShuttle": "NA",
                                "MRTShuttleDirection": "NA"
                            }
         
            message_na_data = {
                                "Content": "NA",
                                "CreatedDate": "NA"
                            }
         
            try:
                # Remove trainservicealert widget
                for w in trainservicealert_grid.walk():
                    if w.__class__ == TrainServiceAlertAffectedSegments or w.__class__ == TrainServiceAlertMessage:
                        #print("remove train service alert widget")
                        trainservicealert_grid.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            if len(train_service_alerts_response['value']['AffectedSegments']) > 0:
                for affectedsegment in train_service_alerts_response['value']['AffectedSegments']:
                    trainservicealertaffectedsegment = TrainServiceAlertAffectedSegments(affectedsegment = affectedsegment)
                    trainservicealert_grid.add_widget(trainservicealertaffectedsegment)
            else:
                trainservicealertaffectedsegment = TrainServiceAlertAffectedSegments(affectedsegment = affectedsegment_na_data)
                trainservicealert_grid.add_widget(trainservicealertaffectedsegment)
         
            if len(train_service_alerts_response['value']['Message']) > 0:
                for message in train_service_alerts_response['value']['Message']:
                    trainservicealertmessage = TrainServiceAlertMessage(message = message)
                    trainservicealert_grid.add_widget(trainservicealertmessage)
            else:
                trainservicealertmessage = TrainServiceAlertMessage(message = message_na_data)
                trainservicealert_grid.add_widget(trainservicealertmessage)
                
        if screen_name == "trainmap_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Train Map"
            
        if screen_name == "trainfare_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Train Fare"
         
            trainfaretypesurl = "https://tih-api.stb.gov.sg/transport/v1/fare/mrt-lrt/types?apikey="
            train_fare_types = requests.get(trainfaretypesurl + tih_api_key )
            train_fare_types_response = json.loads(train_fare_types.content)
            # print(train_fare_types_response['data'])
            # ['Senior citizen card fare', 'Student card fare', 'Workfare transport concession card fare', 'Single trip', 'Adult card fare', 'Persons with diabilities card fare']
         
            trainfaretab = self.trainfare.ids.tabs
         
            try:
                # Remove train fare tab widget
                for w in trainfaretab.walk():
                    if w.__class__ == TrainFareTab:
                        #print("remove train fare tab widget")
                        trainfaretab.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            for train_fare_type in train_fare_types_response['data']:
                trainfaretab.add_widget(TrainFareTab(text=train_fare_type))
                
        if screen_name == "incidents_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Traffic Incidents"
            incidentsscreen_mapview = self.root.ids.incidents_screen.ids.incidentsmapview
         
            try:
                # Remove taximapview widget
                for w in incidentsscreen_mapview.walk():
                    if w.__class__ == IncidentsMapView:
                        print("remove incidentmapview widget")
                        incidentsscreen_mapview.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
         
            self.incidentsmapview = IncidentsMapView()
            incidentsscreen_mapview.add_widget(self.incidentsmapview)
         
            self.incidentsmapview.center_on(self.current_lat, self.current_lon)
            
            from incidents_folder.incidentsgpshelper import IncidentsGpsHelper
            IncidentsGpsHelper().run()
            
        if screen_name == "roadwork_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Road Works"
            roadwork_datatable_page = self.root.ids.roadwork_screen.ids.roadworkdatatable
            
            try:
                for w in roadwork_datatable_page.walk():
                    if w.__class__ == RoadWork:
                        print("remove MD Data Table widget")
                        roadwork_datatable_page.remove_widget(w)
                    else:
                        print("No widget to remove")
                        continue
            except:
                print("Something is wrong")
                pass
             
            # Instantiate the road work data table
            self.roadwork_datatable = RoadWork(totalroadworks = self.total_road_works_response)
            # Add road work data table to the road work screen
            roadwork_datatable_page.add_widget(self.roadwork_datatable)
            
        if screen_name == "trafficimage_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Traffic Images"
            self.trafficimage_backdroplayout.ids.backdrop.open(-Window.height / 3.3)
            trafficimage_backdropbacklayer = self.trafficimage_backdroplayout.ids.container
            
            try:
                # Remove trafficimagemapview widget
                for w in trafficimage_backdropbacklayer.walk():
                    if w.__class__ == TrafficImageMapView:
                        #print("remove trafficimagemapview widget")
                        trafficimage_backdropbacklayer.remove_widget(w)
                    else:
                        continue
                        #print("No widget to remove")
            except:
                print("Something is wrong")
                pass
             
            self.trafficimagemapview = TrafficImageMapView()
            trafficimage_backdropbacklayer.add_widget(self.trafficimagemapview)
             
            self.trafficimagemapview.center_on(self.current_lat, self.current_lon)
            
            from trafficimage_folder.trafficimagegpshelper import TrafficImageGpsHelper
            TrafficImageGpsHelper().run()
            
        if screen_name == "roadopening_screen":
            self.root.ids.titlename.title = "Road Openings"
            print("Screen name is ", screen_name)
            roadopeningexpansionpanelgridlayout = self.roadopening_expansionpanel.ids.box
            
            try:
                for w in roadopeningexpansionpanelgridlayout.walk():
                    if w.__class__ == MDExpansionPanel:
                        print("remove MDExpansionPanel widget")
                        roadopeningexpansionpanelgridlayout.remove_widget(w)
                    else:
                        print("No widget to remove")
                        continue
            except:
                print("Something is wrong")
                pass
             
            from datetime import datetime, timedelta
            import pytz
            tz = pytz.timezone('Asia/Singapore')
            # create datetime object, convert to string for formatting
            onedaylater = (datetime.now(tz) + timedelta(2)).strftime('%Y-%m-%d')
            # convert the date string back to datetime object
            onedaylaterdatetimeobject = datetime.strptime(onedaylater, '%Y-%m-%d')
            # print("onedaylater", onedaylaterdatetimeobject)
            # print(type(onedaylaterdatetimeobject))
             
            for road_opening in self.total_road_openings_response:
                roadopeningdatetimeobject = datetime.strptime(road_opening['StartDate'], '%Y-%m-%d')
                #print("roadopeningdatetimeobject", roadopeningdatetimeobject)
                if onedaylaterdatetimeobject > roadopeningdatetimeobject:
                    roadopeningexpansionpanelgridlayout.add_widget(
                        MDExpansionPanel(
                            icon="icons/roadopening.png",
                            content=RoadOpeningExpansionContent(road_opening = road_opening),
                            panel_cls=MDExpansionPanelThreeLine(
                                text=road_opening['StartDate'],
                                secondary_text=road_opening['EndDate'],
                                tertiary_text=road_opening['RoadName'],
                            )
                        )
                    )
                    
        if screen_name == "favouritebusservice_screen":
            print("Screen name is ", screen_name)
            self.refresh_favourite_bus_service = Clock.schedule_interval(self.go_to_favourite_bus, 60)
            
        if screen_name !=  "favouritebusservice_screen" and self.refresh_favourite_bus_service != None:
            self.refresh_favourite_bus_service.cancel()
            self.current_screen_is_favourite_screen = False

        if screen_name == "profilephoto_screen":
            print("Screen name is ", screen_name)
            #if platform == 'android':
                #from android.permissions import request_permissions, Permission
                #request_permissions([Permission.WRITE_EXTERNAL_STORAGE, Permission.READ_EXTERNAL_STORAGE])
                
        if screen_name == "carpark_screen":
            print("Screen name is ", screen_name)
            self.root.ids.titlename.title = "Nearby Car Park"
            carparkscreen_mapview = self.root.ids.carpark_screen.ids.carparkmapview
         
            try:
                for w in carparkscreen_mapview.walk():
                    if w.__class__ == CarParkMapView:
                        carparkscreen_mapview.remove_widget(w)
                    else:
                        continue
            except:
                pass
         
            self.carparkmapview = CarParkMapView()
            carparkscreen_mapview.add_widget(self.carparkmapview)
         
            self.carparkmapview.center_on(self.current_lat, self.current_lon)
            
            from carpark_folder.carparkgpshelper import CarParkGpsHelper
            CarParkGpsHelper().run()
            
        if screen_name == "bicycleparking_screen":
            self.root.ids.titlename.title = "Bicycle Parking"
            bicycleparkingscreen_mapview = self.root.ids.bicycleparking_screen.ids.bicycleparkingmapview
         
            try:
                for w in bicycleparkingscreen_mapview.walk():
                    if w.__class__ == BicycleParkingMapView:
                        bicycleparkingscreen_mapview.remove_widget(w)
                    else:
                        continue
            except:
                pass
         
            self.bicycleparkingmapview = BicycleParkingMapView()
            bicycleparkingscreen_mapview.add_widget(self.bicycleparkingmapview)
         
            self.bicycleparkingmapview.center_on(self.current_lat, self.current_lon)
            
            from bicycle_folder.bicycleparkinggpshelper import BicycleParkingGpsHelper
            BicycleParkingGpsHelper().run()
                    
 
MainApp().run()
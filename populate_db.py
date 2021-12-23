import sqlite3
import requests, json
from apikey_ import lta_account_key
 
#Authentication parameters
headers = {'AccountKey' : lta_account_key, 'accept' : 'application/json'} #this is by default
#API parameters
uri = 'http://datamall2.mytransport.sg/' #Resource URL
 
connection = sqlite3.connect("myapp.db")
cursor = connection.cursor()
 
#bus_stops_path = "ltaodataservice/BusStops"
#bus_stops_skip = '?$skip='
#for i in range(0, 11):
    #if i == 0:
        #bus_stops_url = uri + bus_stops_path
        #bus_stops = requests.get(bus_stops_url, headers=headers)
        #bus_stops_response = json.loads(bus_stops.content)
        #for bus_stop in bus_stops_response['value']:
            #try:
                #cursor.execute("""INSERT INTO busstops (BusStopCode, RoadName, Description, Latitude, Longitude) VALUES (?, ?, ?, ?, ?);""", (bus_stop['BusStopCode'], bus_stop['RoadName'], bus_stop['Description'], bus_stop['Latitude'], bus_stop['Longitude']))
                #print(f"Added a new bus stop {bus_stop['BusStopCode']} {bus_stop['Description']}")
            #except Exception as e:
                #print(bus_stop['BusStopCode'])
                #print(e)
 
    #else:
        #bus_stops_url = uri + bus_stops_path + bus_stops_skip + str(i*500)
        #bus_stops = requests.get(bus_stops_url, headers=headers)
        #bus_stops_response = json.loads(bus_stops.content)
        #for bus_stop in bus_stops_response['value']:
            #try:
                #print(f"Added a new bus stop {bus_stop['BusStopCode']} {bus_stop['Description']}")
                #cursor.execute("""INSERT INTO busstops (BusStopCode, RoadName, Description, Latitude, Longitude) VALUES (?, ?, ?, ?, ?);""", (bus_stop['BusStopCode'], bus_stop['RoadName'], bus_stop['Description'], bus_stop['Latitude'], bus_stop['Longitude']))
            #except Exception as e:
                #print(bus_stop['BusStopCode'])
                #print(e)
 
#connection.commit()

#bus_routes_path = "ltaodataservice/BusRoutes"
#bus_routes_skip = '?$skip='
#for i in range(0, 53):
    #if i == 0:
        #bus_routes_url = uri + bus_routes_path
        #bus_routes = requests.get(bus_routes_url, headers=headers)
        #bus_routes_response = json.loads(bus_routes.content)
        #for bus_route in bus_routes_response['value']:
            #try:
                #cursor.execute("""INSERT INTO busroutes (ServiceNo, Operator, Direction, StopSequence, BusStopCode, Distance, WD_FirstBus, WD_LastBus, SAT_FirstBus, SAT_LastBus, SUN_FirstBus, SUN_LastBus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (bus_route['ServiceNo'], bus_route['Operator'], bus_route['Direction'], bus_route['StopSequence'], bus_route['BusStopCode'], bus_route['Distance'], bus_route['WD_FirstBus'], bus_route['WD_LastBus'], bus_route['SAT_FirstBus'], bus_route['SAT_LastBus'], bus_route['SUN_FirstBus'], bus_route['SUN_LastBus']))
                #print(f"Added a new bus route {bus_route['ServiceNo']}")
            #except Exception as e:
                #print(bus_route['ServiceNo'])
                #print(e)
    #else:
        #bus_routes_url = uri + bus_routes_path + bus_routes_skip + str(i*500)
        #bus_routes = requests.get(bus_routes_url, headers=headers)
        #bus_routes_response = json.loads(bus_routes.content)
        #for bus_route in bus_routes_response['value']:
            #try:
                #cursor.execute("""INSERT INTO busroutes (ServiceNo, Operator, Direction, StopSequence, BusStopCode, Distance, WD_FirstBus, WD_LastBus, SAT_FirstBus, SAT_LastBus, SUN_FirstBus, SUN_LastBus) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (bus_route['ServiceNo'], bus_route['Operator'], bus_route['Direction'], bus_route['StopSequence'], bus_route['BusStopCode'], bus_route['Distance'], bus_route['WD_FirstBus'], bus_route['WD_LastBus'], bus_route['SAT_FirstBus'], bus_route['SAT_LastBus'], bus_route['SUN_FirstBus'], bus_route['SUN_LastBus']))
                #print(f"Added a new bus route {bus_route['ServiceNo']}")
            #except Exception as e:
                #print(bus_route['ServiceNo'])
                #print(e)
 
#connection.commit()

bus_services_path = "ltaodataservice/BusServices"
bus_services_skip = '?$skip='
for i in range(0, 2):
    if i == 0:
        bus_services_url = uri + bus_services_path
        bus_services = requests.get(bus_services_url, headers=headers)
        bus_services_response = json.loads(bus_services.content)
        for bus_service in bus_services_response['value']:
            try:
                cursor.execute("""INSERT INTO busservices (ServiceNo, Operator, Direction, Category, OriginCode, DestinationCode, AM_Peak_Freq, AM_Offpeak_Freq, PM_Peak_Freq, PM_Offpeak_Freq, LoopDesc) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (bus_service['ServiceNo'], bus_service['Operator'], bus_service['Direction'], bus_service['Category'], bus_service['OriginCode'], bus_service['DestinationCode'], bus_service['AM_Peak_Freq'], bus_service['AM_Offpeak_Freq'], bus_service['PM_Peak_Freq'], bus_service['PM_Offpeak_Freq'], bus_service['LoopDesc']))
                print(f"Added a new bus service {bus_service['ServiceNo']}")
            except Exception as e:
                print(bus_service['ServiceNo'])
                print(e)
    else:
        bus_services_url = uri + bus_services_path + bus_services_skip + str(i*500)
        bus_services = requests.get(bus_services_url, headers=headers)
        bus_services_response = json.loads(bus_services.content)
        for bus_service in bus_services_response['value']:
            try:
                cursor.execute("""INSERT INTO busservices (ServiceNo, Operator, Direction, Category, OriginCode, DestinationCode, AM_Peak_Freq, AM_Offpeak_Freq, PM_Peak_Freq, PM_Offpeak_Freq, LoopDesc) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);""", (bus_service['ServiceNo'], bus_service['Operator'], bus_service['Direction'], bus_service['Category'], bus_service['OriginCode'], bus_service['DestinationCode'], bus_service['AM_Peak_Freq'], bus_service['AM_Offpeak_Freq'], bus_service['PM_Peak_Freq'], bus_service['PM_Offpeak_Freq'], bus_service['LoopDesc']))
                print(f"Added a new bus service {bus_service['ServiceNo']}")
            except Exception as e:
                print(bus_service['ServiceNo'])
                print(e)
 
connection.commit()
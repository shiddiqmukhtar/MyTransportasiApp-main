from kivymd.uix.dialog import BusRouteMDDialog
 
class BusRouteGeneralPopupMenu(BusRouteMDDialog):
    def __init__(self, bus_route_data):
        super().__init__()
 
        headers = "ServiceNo,Operator,Direction,StopSequence,BusStopCode,Distance,WD_FirstBus,WD_LastBus,SAT_FirstBus,SAT_LastBus,SUN_FirstBus,SUN_LastBus,BusStopDescription,Latitude,Longitude"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(bus_route_data[i])
            setattr(self, attribute_name, attribute_value)
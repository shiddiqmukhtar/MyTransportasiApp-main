from kivymd.uix.dialog import BusStopMDDialog
 
class BusStopPopupMenu(BusStopMDDialog):
    def __init__(self, bus_stop_data):
        super().__init__()
 
        # Set all of the fields of market data
        headers = "BusStopCode,RoadName,Description,Latitude,Longitude"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(bus_stop_data[i])
            setattr(self, attribute_name, attribute_value)
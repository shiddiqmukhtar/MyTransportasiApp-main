from kivymd.uix.dialog import BusServiceMDDialog
 
class BusServicePopupMenu(BusServiceMDDialog):
    def __init__(self, bus_service_data):
        super().__init__()
 
        headers = "ServiceNo,Operator,Direction,Category,OriginCode,DestinationCode,AM_Peak_Freq,AM_Offpeak_Freq,PM_Peak_Freq,PM_Offpeak_Freq,LoopDesc"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(bus_service_data[i])
            setattr(self, attribute_name, attribute_value)
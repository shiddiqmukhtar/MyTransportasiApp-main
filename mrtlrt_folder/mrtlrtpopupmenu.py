from kivymd.uix.dialog import MrtMDDialog, LrtMDDialog
 
class MrtPopupMenu(MrtMDDialog):
    def __init__(self, mrt_data):
        super().__init__()
 
        # Set all of the fields of mrt data
        headers = "MRT,Latitude,Longitude,Road_name,Building,Address,Postal"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(mrt_data[i])
            setattr(self, attribute_name, attribute_value)
 
class LrtPopupMenu(LrtMDDialog):
    def __init__(self, lrt_data):
        super().__init__()
 
        # Set all of the fields of lrt data
        headers = "LRT,Latitude,Longitude,Road_name,Building,Address,Postal"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(lrt_data[i])
            setattr(self, attribute_name, attribute_value)
from kivymd.uix.dialog import BicycleParkingMDDialog
 
class BicycleParkingPopupMenu(BicycleParkingMDDialog):
    def __init__(self, bicycleparking_data):
        super().__init__()
 
        headers = "Description,Latitude,Longitude,RackType,RackCount,ShelterIndicator"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(bicycleparking_data[attribute_name])
            setattr(self, attribute_name, attribute_value)
from kivymd.uix.dialog import CarParkMDDialog
 
class CarParkPopupMenu(CarParkMDDialog):
    def __init__(self, carpark_data):
        super().__init__()
 
        headers = "CarParkID,Area,Development,Location,AvailableLots,LotType,Agency"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(carpark_data[attribute_name])
            setattr(self, attribute_name, attribute_value)
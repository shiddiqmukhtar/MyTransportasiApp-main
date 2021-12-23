from kivymd.uix.dialog import TaxiMDDialog, TaxiStandMDDialog
 
class TaxiPopupMenu(TaxiMDDialog):
    def __init__(self, taxi_data):
        super().__init__()
 
        # Set all of the fields of market data
        headers = "Latitude,Longitude"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(taxi_data[attribute_name])
            setattr(self, attribute_name, attribute_value)
 
class TaxiStandPopupMenu(TaxiStandMDDialog):
    def __init__(self, taxi_stand_data):
        super().__init__()
 
        # Set all of the fields of market data
        headers = "TaxiCode,Latitude,Longitude,Bfa,Ownership,Type,Name"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(taxi_stand_data[attribute_name])
            setattr(self, attribute_name, attribute_value)
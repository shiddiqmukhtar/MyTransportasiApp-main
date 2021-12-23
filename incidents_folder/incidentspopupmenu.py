from kivymd.uix.dialog import IncidentsMDDialog
 
class IncidentsPopupMenu(IncidentsMDDialog):
    def __init__(self, incident_data):
        super().__init__()
 
        headers = "Type,Latitude,Longitude,Message"
        headers = headers.split(',')
 
        for i in range(len(headers)):
            attribute_name = headers[i]
            attribute_value = str(incident_data[attribute_name])
            setattr(self, attribute_name, attribute_value)
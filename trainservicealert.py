from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen
from kivy.uix.label import Label
 
class TrainServiceAlertAffectedSegments(Screen):
    def __init__(self, **kwargs):
        super().__init__()
 
        # print(kwargs['affectedsegment'])
        # {'Line': 'NEL', 'Direction': 'Punggol', 'Stations': 'NE1,NE3,NE4,NE5,NE6', 'FreePublicBus': 'NE1,NE3,NE4,NE5,NE6', 'FreeMRTShuttle': 'NE1,NE3,NE4,NE5,NE6', 'MRTShuttleDirection': 'Punggol'}
 
        if len(kwargs['affectedsegment']['Stations']) == 0:
            kwargs['affectedsegment']['Stations'] = "NA"
        if len(kwargs['affectedsegment']['FreePublicBus']) == 0:
            kwargs['affectedsegment']['FreePublicBus'] = "NA"
        if len(kwargs['affectedsegment']['FreeMRTShuttle']) == 0:
            kwargs['affectedsegment']['FreeMRTShuttle'] = "NA"
        if len(kwargs['affectedsegment']['MRTShuttleDirection']) == 0:
            kwargs['affectedsegment']['MRTShuttleDirection'] = "NA"
         
        # When deploy to mobile phone, need to change the size to 50
        app = App.get_running_app()
        if app.theme_cls.theme_style == "Light":
            label = Label(text="[size=32][color=000000]" + "Line: " + kwargs['affectedsegment']['Line'] + "\n" + "Direction: " + kwargs['affectedsegment']['Direction'] + "\n" + "Stations: " + kwargs['affectedsegment']['Stations'] + "\n" + "FreePublicBus: " + kwargs['affectedsegment']['FreePublicBus'] + "\n" + "FreeMRTShuttle: " + kwargs['affectedsegment']['FreeMRTShuttle'] + "\n" + "MRTShuttleDirection: " + kwargs['affectedsegment']['MRTShuttleDirection'] + "[/color][/size]", markup = True, pos_hint={"top": 0.9, "right": 1}, valign = 'middle')
        else:
            label = Label(text="[size=32][color=ffffff]" + "Line: " + kwargs['affectedsegment']['Line'] + "\n" + "Direction: " + kwargs['affectedsegment']['Direction'] + "\n" + "Stations: " + kwargs['affectedsegment']['Stations'] + "\n" + "FreePublicBus: " + kwargs['affectedsegment']['FreePublicBus'] + "\n" + "FreeMRTShuttle: " + kwargs['affectedsegment']['FreeMRTShuttle'] + "\n" + "MRTShuttleDirection: " + kwargs['affectedsegment']['MRTShuttleDirection'] + "[/color][/size]", markup = True, pos_hint={"top": 0.9, "right": 1}, valign = 'middle')
        
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width, None)), texture_size=lambda *x: label.setter('height')(label, label.texture_size[1]))
        self.add_widget(label)
 
class TrainServiceAlertMessage(Screen):
    def __init__(self, **kwargs):
        super().__init__()
 
        # print(kwargs['message'])
        # {'Content': '1710hrs: NEL – No train service between Harbourfront to Dhoby Ghaut stations towards Punggol station due to a signalling fault. Free bus rides are available at designated bus stops.', 'CreatedDate': '2017-12-01 17:54:21'}
 
        if len(kwargs['message']['Content']) == 0:
            kwargs['message']['Content'] = "NA"
        if len(kwargs['message']['CreatedDate']) == 0:
            kwargs['message']['CreatedDate'] = "NA"
 
        # When deploy to mobile phone, need to change the size to 50
        app = App.get_running_app()
        if app.theme_cls.theme_style == "Light":
            label = Label(text="[size=32][color=000000]" + "Content: " + kwargs['message']['Content'] + "\n" + "CreatedDate: " + kwargs['message']['CreatedDate'] + "[/color][/size]", markup = True, pos_hint={"top": 1, "right": 1}, valign = 'middle')
        else:
            label = Label(text="[size=32][color=ffffff]" + "Content: " + kwargs['message']['Content'] + "\n" + "CreatedDate: " + kwargs['message']['CreatedDate'] + "[/color][/size]", markup = True, pos_hint={"top": 1, "right": 1}, valign = 'middle')
        label.bind(width=lambda *x: label.setter('text_size')(label, (label.width, None)), texture_size=lambda *x: label.setter('height')(label, label.texture_size[1]))
        self.add_widget(label)
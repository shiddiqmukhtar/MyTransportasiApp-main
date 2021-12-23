from kivymd.uix.boxlayout import MDBoxLayout
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
from kivymd.uix.list import TwoLineAvatarListItem, ImageLeftWidget
 
class RoadOpeningExpansionContent(MDBoxLayout):
    def __init__(self, **kwargs):
        # print(kwargs)
        # {'road_opening': {'EventID': 'RMAPP-202011-0728', 'StartDate': '2020-11-19', 'EndDate': '2020-12-30', 'SvcDept': 'PRIVATE', 'RoadName': 'LORONG K TELOK KURAU', 'Other': 'For details, please call 63052362'}}
        super().__init__()
        image = ImageLeftWidget(source="icons/arrowup.png")
        twolineavataritem = TwoLineAvatarListItem(text = kwargs['road_opening']['SvcDept'], secondary_text=kwargs['road_opening']['Other'])
        twolineavataritem.add_widget(image)
        self.add_widget(twolineavataritem)
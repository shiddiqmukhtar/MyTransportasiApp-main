from kivy.uix.gridlayout import GridLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.uix.label import Label
from kivy.uix.image import Image
from kivy.graphics import Color, RoundedRectangle
import kivy.utils
 
class CarParkTypeLabel(GridLayout):
    rows = 1
 
    def __init__(self, **kwargs):
        super().__init__()
 
        with self.canvas.before:
            self.canvas_color = Color(rgb=kivy.utils.get_color_from_hex("c8fcf7"))
            self.rect = RoundedRectangle(size=self.size, pos=self.pos)
        self.bind(pos=self.update_rect, size=self.update_rect)
 
        # First Header: Car Park Type
        firstheader = FloatLayout()
        firstheaderlabel = Label(text="[color=000000]Car Park\nType[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .65, "right": 1})
        firstheader.add_widget(firstheaderlabel)
 
        # Second Header: Cars
        secondheader = FloatLayout()
        secondheaderimage = Image(source="icons/car_label.png", size_hint=(1, 0.5), pos_hint={"top": 0.95, "right": 1})
        secondheaderlabel = Label(text="[color=000000]Cars[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        secondheader.add_widget(secondheaderimage)
        secondheader.add_widget(secondheaderlabel)
 
        # Third Header: Heavy Vehicles
        thirdheader = FloatLayout()
        thirdheaderimage = Image(source="icons/heavyvehicle_label.png", size_hint=(1, 0.5), pos_hint={"top": 0.95, "right": 1})
        thirdheaderlabel = Label(text="[color=000000]Heavy\nVehicles[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        thirdheader.add_widget(thirdheaderimage)
        thirdheader.add_widget(thirdheaderlabel)
 
        # Fourth Header: Motorcycles
        fourthheader = FloatLayout()
        fourthheaderimage = Image(source="icons/motorcycle_label.png", size_hint=(1, 0.5), pos_hint={"top": 0.95, "right": 1})
        fourthheaderlabel = Label(text="[color=000000]Motorcycles[/color]", markup = True, size_hint=(1, .2), pos_hint={"top": .4, "right": 1})
        fourthheader.add_widget(fourthheaderimage)
        fourthheader.add_widget(fourthheaderlabel)
 
        self.add_widget(firstheader)
        self.add_widget(secondheader)
        self.add_widget(thirdheader)
        self.add_widget(fourthheader)
 
    def update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
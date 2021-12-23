from kivymd.uix.screen import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
from kivy.app import App
from datetime import datetime, timedelta
import pytz
 
class RoadWork(Screen):
    def __init__(self, **kwargs):
        super().__init__()
 
        # print(len(kwargs['totalroadworks']))
        # 5405
        # print(kwargs['totalroadworks'][:5])
        # [{'EventID': 'RMAPP-202011-0214', 'StartDate': '2020-11-18', 'EndDate': '2021-06-30', 'SvcDept': 'PRIVATE', 'RoadName': 'ADAM ROAD', 'Other': 'For details'}, {'EventID': 'RMAPP-202011-0260', 'StartDate': '2020-11-17', 'EndDate': '2020-12-31', 'SvcDept': 'PUB - CATCHMENT AND WATERWAYS', 'RoadName': 'ADAM ROAD', 'Other': 'For details'}, {'EventID': 'RMINRM-202011-0302', 'StartDate': '2020-11-08', 'EndDate': '2020-11-29', 'SvcDept': 'LAND TRANSPORT AUTHORITY', 'RoadName': 'ADAM ROAD', 'Other': 'For details'}, {'EventID': 'RMINRM-202011-0423', 'StartDate': '2020-11-07', 'EndDate': '2020-11-21', 'SvcDept': 'PUB - WATER RECLAMATION (NETWORK) DEPT', 'RoadName': 'ADAM ROAD', 'Other': 'For details'}, {'EventID': 'RMINRM-202009-0386', 'StartDate': '2020-09-11', 'EndDate': '2020-11-30', 'SvcDept': 'NETLINK TRUST', 'RoadName': 'ADAM ROAD', 'Other': 'For details'}]
 
        tz = pytz.timezone('Asia/Singapore')
        # create datetime object, convert to string for formatting
        onedaylater = (datetime.now(tz) + timedelta(2)).strftime('%Y-%m-%d')
        # convert the date string back to datetime object
        onedaylaterdatetimeobject = datetime.strptime(onedaylater, '%Y-%m-%d')
        # print("onedaylater", onedaylaterdatetimeobject)
        # print(type(onedaylaterdatetimeobject))
 
        displayroadworklist = []
        for road_work in kwargs['totalroadworks']:
            roadworkdatetimeobject = datetime.strptime(road_work['StartDate'], '%Y-%m-%d')
            #print("roadopeningdatetimeobject", roadopeningdatetimeobject)
            if onedaylaterdatetimeobject > roadworkdatetimeobject:
                displayroadworklist.append((road_work['StartDate'], road_work['EndDate'], road_work['RoadName']))
 
        # print("displayroadworklist", displayroadworklist)
        # print(len(displayroadworklist))
 
        # Density-independent Pixels - An abstract unit that is based on the physical density of the screen. With a density of 1, 1dp is equal to 1px. When running on a higher density screen, the number of pixels used to draw 1dp is scaled up a factor appropriate to the screen’s dpi, and the inverse for a lower dpi. The ratio of dp-to-pixels will change with the screen density, but not necessarily in direct proportion. Using the dp unit is a simple solution to making the view dimensions in your layout resize properly for different screen densities. In others words, it provides consistency for the real-world size of your UI across different devices.
        table = MDDataTable(
            size_hint = (0.9, 0.85),
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            # check = True,
            use_pagination=True,
            #how many rows to display on screen
            rows_num = 20,
            column_data = [
                ("StartDate", dp(20)),
                ("EndDate", dp(20)),
                ("RoadName", dp(20))
        ],
            row_data = displayroadworklist,
            sorted_on = "RoadName",
            sorted_order="ASC"
        )
 
        table.bind(on_row_press=self.row_press)
        self.add_widget(table)
 
    def row_press(self, instance_table, instance_row):
        print(instance_table, instance_row)
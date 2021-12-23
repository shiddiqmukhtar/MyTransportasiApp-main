from kivy_garden.mapview import MapView
from kivy.clock import Clock
from kivy.app import App
from mrtlrt_folder.mrtlrtmarker import MrtMarker, LrtMarker
 
class MrtLrtMapView(MapView):
    getting_mrtlrt_timer = None
    mrt_names = []
    lrt_names = []
 
    def start_getting_mrtlrt_in_fov(self):
        # On lon or on lat, it will first try to cancel the timer
        try:
            self.getting_mrtlrt_timer.cancel()
        except:
            pass
        # After one second, get the markets in the field of view
        self.getting_mrtlrt_timer = Clock.schedule_once(self.get_mrtlrt_in_fov, 1)
 
    def get_mrtlrt_in_fov(self, *args):
        self.mrt_names = []
        self.lrt_names = []
         
        # Get reference to main app and the database cursor
        min_lat, min_lon, max_lat, max_lon = self.get_bbox()
        app = App.get_running_app()
 
        mrt_sql_statement = "SELECT * FROM mrt WHERE Longitude > %s AND Longitude < %s AND Latitude > %s AND Latitude < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(mrt_sql_statement)
        mrts = app.cursor.fetchall()
 
        lrt_sql_statement = "SELECT * FROM lrt WHERE Longitude > %s AND Longitude < %s AND Latitude > %s AND Latitude < %s "%(min_lon, max_lon, min_lat, max_lat)
        app.cursor.execute(lrt_sql_statement)
        lrts = app.cursor.fetchall()
 
        for mrt in mrts:
            name = mrt[0]
            if name in self.mrt_names:
                continue
            else:
                self.add_mrt(mrt)
 
        for lrt in lrts:
            name = lrt[0]
            if name in self.lrt_names:
                continue
            else:
                self.add_lrt(lrt)
 
    def add_mrt(self, mrt):
        lat, lon = mrt[1], mrt[2]
        marker = MrtMarker(lat=lat, lon=lon, source = "icons/MRT.png")
        marker.mrt_data = mrt
        # Add the MrtMarker to the map
        self.add_widget(marker)
 
        # Keep track of the mrt's name
        name = mrt[0]
        self.mrt_names.append(name)
 
    def add_lrt(self, lrt):
        lat, lon = lrt[1], lrt[2]
        marker = LrtMarker(lat=lat, lon=lon, source = "icons/LRT.png")
        marker.lrt_data = lrt
        # Add the LrtMarker to the map
        self.add_widget(marker)
 
        # Keep track of the lrt's name
        name = lrt[0]
        self.lrt_names.append(name)
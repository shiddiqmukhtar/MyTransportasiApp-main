import sqlite3
#mode csv
#import MRT_noheader.csv mrt
 
connection = sqlite3.connect('myapp.db')
 
cursor = connection.cursor()
 
#cursor.execute("""
    #CREATE TABLE IF NOT EXISTS busstops (
    #BusStopCode TEXT NOT NULL,
    #RoadName TEXT NOT NULL,
    #Description TEXT NOT NULL,
    #Latitude REAL NOT NULL,
    #Longitude REAL NOT NULL
#)
#""")

#cursor.execute("""
    #CREATE TABLE IF NOT EXISTS busroutes (
    #ServiceNo TEXT NOT NULL,
    #Operator TEXT NOT NULL,
    #Direction INTEGER NOT NULL,
    #StopSequence INTEGER NOT NULL,
    #BusStopCode TEXT NOT NULL,
    #Distance TEXT NOT NULL,
    #WD_FirstBus TEXT NOT NULL,
    #WD_LastBus TEXT NOT NULL,
    #SAT_FirstBus TEXT NOT NULL,
    #SAT_LastBus TEXT NOT NULL,
    #SUN_FirstBus TEXT NOT NULL,
    #SUN_LastBus TEXT NOT NULL
    #)
#""")

#cursor.execute("""
    #CREATE TABLE IF NOT EXISTS busservices (
    #ServiceNo TEXT NOT NULL,
    #Operator TEXT NOT NULL,
    #Direction INTEGER NOT NULL,
    #Category TEXT NOT NULL,
    #OriginCode TEXT NOT NULL,
    #DestinationCode TEXT NOT NULL,
    #AM_Peak_Freq TEXT NOT NULL,
    #AM_Offpeak_Freq TEXT NOT NULL,
    #PM_Peak_Freq TEXT NOT NULL,
    #PM_Offpeak_Freq TEXT NOT NULL,
    #LoopDesc TEXT NOT NULL
    #)
#""")

#cursor.execute("""
    #CREATE TABLE IF NOT EXISTS favourite (
    #BusStopCode TEXT NOT NULL,
    #BusService TEXT NOT NULL
    #)
#""")

#cursor.execute("""
    #CREATE TABLE IF NOT EXISTS lrt (
    #LRT TEXT NOT NULL,
    #Latitude REAL NOT NULL,
    #Longitude REAL NOT NULL,
    #Road_name TEXT NOT NULL,
    #Building TEXT NOT NULL,
    #Address TEXT NOT NULL,
    #Postal INTEGER NOT NULL
    #)
#""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS mrt (
    MRT TEXT NOT NULL,
    Latitude REAL NOT NULL,
    Longitude REAL NOT NULL,
    Road_name TEXT NOT NULL,
    Building TEXT NOT NULL,
    Address TEXT NOT NULL,
    Postal INTEGER NOT NULL
    )
""")
 
connection.commit()
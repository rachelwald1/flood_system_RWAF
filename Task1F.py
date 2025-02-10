from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def run():

    stations_list = build_station_list()

    inconsistent_stations_list = inconsistent_typical_range_stations(stations_list)

    sorted_list = []

    for i in inconsistent_stations_list:
        sorted_list.append(i)

    result = sorted(sorted_list)

    print(result)

if __name__ == "__main__":
    print("*** Task 1F: CUED Part IA Flood Warning System ***")
    run()
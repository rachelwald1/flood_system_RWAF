from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance
from floodsystem.geo import stations_within_radius

def run():
    # create a list of the stations
    stations = build_station_list()

    cambridge_centre = (52.2053, 0.1218)

    result = stations_within_radius(stations, cambridge_centre, 10)
    
    sorted_list = []

    for i in result:
        sorted_list.append(i.name)
        
    result = sorted(sorted_list)
    
    print(result)

    
    
if __name__ == "__main__":
    print("*** Task 1C: CUED Part IA Flood Warning System ***")
    run()
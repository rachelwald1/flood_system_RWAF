from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import stations_by_distance

def run():
    
    # Build list of stations
    stations_list = build_station_list()

    cambridge_centre = (52.2053, 0.1218)

    distance_list = stations_by_distance(stations_list, cambridge_centre)
    print(distance_list[0][0].town)
    print("10 closest stations to Cambridge:")
    for station, distance in distance_list[:10]:
        print(f"{station.name}, {station.town}, {distance: .2f} km")
    
    print("10 furthest stations from Cambridge:")
    for station, distance in distance_list[-10:]:
        print(f"{station.name}, {station.town}, {distance: .2f} km")
        
if __name__ == "__main__":
    print("*** Task B: CUED Part IA Flood Warning System ***")
    run()
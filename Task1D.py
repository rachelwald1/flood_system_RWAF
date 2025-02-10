from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_with_stations
from floodsystem.geo import stations_by_river

def run():

    stations_list = build_station_list()

    rivers_monitored = rivers_with_stations(stations_list)
    
    print(f"{len(rivers_monitored)} rivers have at least one monitoring station.")
    
    first_10_rivers = ((rivers_monitored)[:10])
    
    first_10_rivers.sort()
    
    print("First 10 -", first_10_rivers)
    
    stations_dict = stations_by_river(stations_list)
    
    river_wanted = ["River Aire", "River Thames", "River Cam"]
              
    for river in river_wanted:
        print(f"\n{river}:")
        if river in stations_dict:
            station_names = sorted([station.name for station in stations_dict[river][:10]])
            print(station_names)
        else:
            print("No stations found.")

        
if __name__ == "__main__":
    print("*** Task 1D: CUED Part IA Flood Warning System ***")
    run()
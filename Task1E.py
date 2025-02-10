from floodsystem.stationdata import build_station_list
from floodsystem.geo import rivers_by_station_number

def run():
    
    # create a list of the stations
    stations = build_station_list()
    
    N = 10    
    
    result = rivers_by_station_number(stations, N)
    
    print(result)
    
if __name__ == "__main__":
    print("*** Task 1E: CUED Part IA Flood Warning System ***")
    run()
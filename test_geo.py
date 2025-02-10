from floodsystem.station import MonitoringStation
from floodsystem.stationdata import build_station_list
from floodsystem.geo import *

def test_stations_by_distance():

    test_station=[]
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (55.0, 37.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "Moscow"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station.append(s)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (51.0, 0.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "London"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station.append(s)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (-37.0, 144.0)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "Melbourne"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station.append(s)
    
    cambridge_centre = (52.2053, 0.1218)

    #print(stations_by_distance(test_station,cambridge_centre))
    sorted_stations=(stations_by_distance(test_station,cambridge_centre))
    #print(sorted_stations[0])
    #first_object=sorted_stations[0]
    #assert first_object.town == "London"
    count=0
    for station, distance in sorted_stations[:3]:
        if count==0:
            output= (f"{station.name}, {station.town}")
            assert "some station, London"
        elif count==1:
            output= (f"{station.name}, {station.town}")
            assert output== "some station, Moscow"
        elif count==2:
            output= (f"{station.name}, {station.town}")
            assert output== "some station, Melbourne"
        count=count+1  
        
test_stations_by_distance()


def test_stations_within_radius():

    test_station2=[]
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.2330, 0.0830)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "Girton"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station2.append(s)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (52.5703, 0.2408)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "Peterborough"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station2.append(s)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (48.8566, 2.3522)
    trange = (-2.3, 3.4445)
    river = "River X"
    town = "Paris"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station2.append(s)
    
    cambridge_centre = (52.2053, 0.1218)
    
    within_rad_stations=(stations_within_radius(test_station2,cambridge_centre, 10))
    assert len(within_rad_stations) == 1
    assert within_rad_stations[0].town == "Girton"
    
test_stations_within_radius()


def test_rivers_with_stations():
    
    test_station3=[]
    # Create a station
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (0.0, 0.0)
    trange = (-2.3, 3.4445)
    river = "Thames"
    town = "London"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station3.append(s)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (0.0, 0.0)
    trange = (-2.3, 3.4445)
    river = "Severn"
    town = "Gloucester"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station3.append(s)
    
    s_id = "test-s-id"
    m_id = "test-m-id"
    label = "some station"
    coord = (0.0, 0.0)
    trange = (-2.3, 3.4445)
    river = "Nile"
    town = "Cairo"
    s = MonitoringStation(s_id, m_id, label, coord, trange, river, town)
    test_station3.append(s)
    
    cambridge_centre = (52.2053, 0.1218)
    
    rivers_mon_list = list(rivers_with_stations(test_station3))
    
    assert "Thames" in rivers_mon_list and "Severn" in rivers_mon_list and "Nile" in rivers_mon_list 
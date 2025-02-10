# Copyright (C) 2018 Garth N. Wells
#
# SPDX-License-Identifier: MIT
"""This module contains a collection of functions related to
geographical data.

"""

from floodsystem.utils import sorted_by_key  # noqa
# import numpy to create haversine formula
import numpy as np

from . import datafetcher
from .station import MonitoringStation

# create a function to find the difference between two geographic coordinates
def haversine_distance(coord1,coord2):
    # radius of the earth 
    R = 6371.0
    
    #convert longitude and latitude from degrees to radians
    lat1, lon1 = np.radians(coord1[0]), np.radians(coord1[1])
    lat2, lon2 = np.radians(coord2[0]), np.radians(coord2[1])
    
    #difference in coordinates
    dlat = lat2 - lat1
    dlon = lon2 - lon1
    
    #haversine formula
    h = np.sin(dlat/2)**2 + np.cos(lat1) * np.cos(lat2) * np.sin(dlon/2)**2
    d = 2 * R * np.arcsin(np.sqrt(h))
    
    distance = d
    
    return distance

# function that returns each station in order of its distance from the monitoring station
def stations_by_distance(stations, p):
    #calculate the distances for each station
    distances = [(station, haversine_distance((station.coord), p)) for station in stations]
    
    #print(distances)
     
    #sort the list by distance
    sorted_distances = sorted(distances, key=lambda x: x[1])
    print(sorted_distances[0])
    return sorted_distances 

# function that returns all stations within a given radius
def stations_within_radius(stations, p, r):
    within_radius = []
    
    for station in stations:
        distance = haversine_distance((station.coord), p)
        if distance <= r:
            within_radius.append(station)
        
    return within_radius

def rivers_with_stations(stations):
    rivers_monitored = set()
   
    for station in stations:
        rivers_monitored.add(station.river)
         
    return  list(rivers_monitored)

def stations_by_river(stations):
   
    stations_dict = {}
   
    for station in stations:
        if station.river in stations_dict:
            stations_dict[station.river].append(station)
        else:
            stations_dict[station.river] = [station]
    return stations_dict

def rivers_by_station_number(stations, N):
    
    # create a dictionary to count the stations for each river
    station_count_by_river = {}
    
    for station in stations:
        river = station.river
        
        if river in station_count_by_river:
            station_count_by_river[river] += 1
        else:
            station_count_by_river[river] = 1
        
    sorted_rivers = sorted(station_count_by_river.items(), key=lambda x: x[1], reverse=True)
    
    top_N_rivers = sorted_rivers[:N]
    
    top_N_rivers = []
    i = 0
    
    while len(top_N_rivers) < N:
        top_N_rivers.append(sorted_rivers[i])
        i += 1
        
        while i < len(sorted_rivers) and sorted_rivers[i][1] == sorted_rivers[i - 1][1]:
            top_N_rivers.append(sorted_rivers[i])
            i += 1
            
    return top_N_rivers
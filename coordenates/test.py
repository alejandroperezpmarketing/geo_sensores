# This code snippet is performing the following tasks:
import numpy as np
import json
import degrees_operations as do

iframe_coordinates = {'REC2':[[39,28,53.133637],[-0,20,7.650964]],
                      'REC3':[[39,28,53.109885],[-0,20,7.663129]],
                      'REC4':[[39,28,53.143535],[-0,20,7.680928]],
                      'REC5':[[39,28,53.119474],[-0,20,7.693816]]}


decimal_lat_list = []
decimal_long_list = []
decimal_lat_long_list = []

iframe_keys = list(iframe_coordinates.keys())

for keys in iframe_coordinates:
    
    degrees_lat = iframe_coordinates[keys][0][0]
    degrees_long = iframe_coordinates[keys][1][0]

    minutes_lat = iframe_coordinates[keys][0][1]
    minutes_long = iframe_coordinates[keys][1][1]
    
    seconds_lat = iframe_coordinates[keys][0][2]
    seconds_long = iframe_coordinates[keys][1][2]
    
    decimal_lat = do.dms_to_decimal(degrees_lat,minutes_lat,seconds_lat)
    decimal_long =  do.dms_to_decimal(degrees_long,minutes_long,seconds_long)
    
    decimal_lat_long = [decimal_lat,decimal_long*-1]
    #print(decimal_lat_long)
    decimal_lat_long_list.append(decimal_lat_long)
    
    #decimal_lat_list.append([decimal_lat])
    #decimal_long_list.append([decimal_long])
    
#print(decimal_long_list)
#print(decimal_lat_list)

decimal_iframe_matrix = np.array(decimal_lat_long_list)
print(iframe_keys)
decimal_iframe_matrix = np.vstack([iframe_keys,decimal_iframe_matrix.T])
#print(decimal_bframe_matrix)
print(decimal_iframe_matrix)
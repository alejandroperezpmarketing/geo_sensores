# This code snippet is performing the following tasks:

import numpy as np
import numpy as np
import json
from coordenates import degrees_operations as do
from coordenates import geodesicas_to_cartecianas as gtc
from matrices import h_elip_coordinates
import elipsoide_grs80 as eg

#The functions in this documents allows us to transform the coordinates dictionaries datasets into arrays, the bframe and iframe
coordinates = {}
n = 3


iframe_coordinates = {'REC2':[[39,28,53.133637],[-0,20,7.650964]],
                      'REC3':[[39,28,53.109885],[-0,20,7.663129]],
                      'REC4':[[39,28,53.143535],[-0,20,7.680928]],
                      'REC5':[[39,28,53.119474],[-0,20,7.693816]]}

bframe_coordinates = {'REC2':[0.4,-0.4,-0.015],
                   'REC3': [0.4,0.4,-0.015],
                   'REC4': [-0.4,-0.4,-0.015], 
                   'REC5': [-0.4,0.4,-0.015]
                   }

h_elip_coordinates = [[55.867], [55.829], [55.883], [55.866]]

# create a entry in a dictionary with a new dictionary with the a specific key + a number i of the range iteration
def sensors_definition(n=n):
    n = 1 + int(input("Please enter a number: "))
    if n != "":
        # check if n is not empty
        global sensors
        sensors = {}
        for i in range(1, n):  # `n` should be defined before this loop
            # Initialize sensor dictionary
            sensors[f"Sensor_{i}"] = {
                "coordinates": {
                    f"x{i}": float(input(f"Insert x{i} coordinate: ")),
                    f"y{i}": float(input(f"Insert y{i} coordinate: ")),
                    f"z{i}": float(input(f"Insert z{i} coordinate: ")),
                }
            }

        # Now, `sensors` will contain all sensor data

        return sensors
    else:
        return ""
    

def manual_bframe_coordinates_definition(bframe_coordinates=bframe_coordinates):
    #this function create the bframe array using the bframe coordinates dectionary
    #this allow us to do matrix opeartions
    
    #1.- Arrays definitions 
    
    ############BODY FRAME ###############
    """ 
    coordinates = {'x':[0.4,0.4,-0.4,-0.4],
                   'y': [-0.4,0.4,-0.4,0.4],
                   'z': [-0.015,-0.015,-0.015,-0.015]
                   } """
                   
    # x y z coordinates               
    
    
    bframe_keys = list(bframe_coordinates.keys())
    bframe_values = np.array(list(bframe_coordinates.values()))
    bframe_matrix = bframe_values
    # Adding keys as a separate row (with the help of np.vstack)
    #bframe_matrix = np.vstack([bframe_keys, bframe_values.T])
    #bframe_matrix = bframe_matrix.transpose()
    #bframe_titles = ["Receptor","x1","x2","x3"]
    #bframe_matrix = np.vstack([bframe_titles, bframe_matrix.T])
   
    #print(bframe_matrix)
    
    """ THIS IS WHEN WE ASK FOR THE COORDINATES USING A INTERFACE
    coordinates_list = []
    
    for i in range(1, n, 1):
        sensors[f"x{i}"] = float(input(f"Insert x{i} coordinate"))
        sensors[f"y{i}"] = float(input(f'Insert y{i}" coordinate'))
        sensors[f"z{i}"] = float(input(f'Insert z{i}" coordinate')) 
        
        coordinates_list.append(f"x{i}", f"y{i}", f"z{i}")
        
    """
    
    return bframe_matrix

def manual_iframe_definition(iframe_coordinates=iframe_coordinates):
    #this function use the coordinate transformation functions to format the iframe coordinates from dms to decimal to be able to make operations
    #this allow us to do matrix opeartions 

 #########################
    #iframe_Matrix in decimal
    
        
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
    #print(iframe_keys)
    #decimal_iframe_matrix = np.vstack([iframe_keys,decimal_iframe_matrix.T])
    #decimal_iframe_matrix = decimal_iframe_matrix.transpose()
    #iframe_titles = ["Receptor","Latitude","longitude"]
    #decimal_iframe_matrix = np.vstack([iframe_titles,decimal_iframe_matrix])
    #print(decimal_bframe_matrix)
    #print(decimal_iframe_matrix)

    return decimal_iframe_matrix
    
    

def manual_h_elipsoid_array_definition(h_elip_coordinates=h_elip_coordinates):

    # h_elip_keys = list(h_elip_coordinates.keys())
    # h_elip_values = np.array(list(h_elip_coordinates.values()))

    # Adding keys as a separate row (with the help of np.vstack)
    # h_elip_matrix = np.vstack([h_elip_keys, h_elip_values.T])
    #h_elip_title = ["Receptor","h_ellipsoidal"]
    h_elip_matrix = np.array(h_elip_coordinates)
    h_elip_keys = list(list(iframe_coordinates.keys()))
    #print(h_elip_matrix[:, 0:1])
    #h_elip_matrix_transposed = np.vstack([h_elip_keys,h_elip_matrix.T])
    #h_elip_matrix_transposed = h_elip_matrix_transposed.transpose()
    #print(h_elip_matrix_transposed)
    #print(h_elip_matrix)

    return h_elip_matrix

def manual_N_coordiantes():
    
    latitude= manual_iframe_definition()[:, 0:1]
    #print(latitude)
    #This fuction allow us to define the radius of curvature in the prime vertical of the ellipsoid N matrix
    N_list= []
    semi_major_axis, semi_minor_axis, flattening, inverse_flattening,e,e_cuadrado= eg.get_ref_elipsoid_parameters()
    for i, value in enumerate(latitude):
        N_value = semi_major_axis/np.sqrt(((1)-((e_cuadrado)*(np.sin**2(value)))))
        N_list.append(N_value)    
    N_matrix = np.array(N_list)
    return N_matrix

manual_N_coordiantes()

def manual_H_coordinates_array_definition():
    N_matix = manual_H_coordinates_array_definition()
    h_elip_matrix = manual_h_elipsoid_array_definition()
    
    



manual_bframe_coordinates_definition()
manual_iframe_definition()
manual_h_elipsoid_array_definition()




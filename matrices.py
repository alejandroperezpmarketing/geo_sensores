import numpy as np

coordinates = {}
n = 3


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
    

def manual_sensors_coordinates_definition():
    
    #1.- Arrays definitions 
    
    ############BODY FRAME ###############
    """ 
    coordinates = {'x':[0.4,0.4,-0.4,-0.4],
                   'y': [-0.4,0.4,-0.4,0.4],
                   'z': [-0.015,-0.015,-0.015,-0.015]
                   } """
                   
    # x y z coordinates               
    bframe_coordinates = {'REC2':[0.4,-0.4,-0.015],
                   'REC3': [0.4,0.4,-0.015],
                   'REC4': [-0.4,-0.4,-0.015], 
                   'REC5': [-0.4,0.4,-0.015]
                   }
    
    bframe_keys = list(bframe_coordinates.keys())
    bframe_values = np.array(list(bframe_coordinates.values()))

    # Adding keys as a separate row (with the help of np.vstack)
    bframe_matrix = np.vstack([bframe_keys, bframe_values.T])
    print(bframe_matrix)
    
    ############i FRAME ###############

    # latitude longitude helipsoidal coordinates               
    iframe_coordinates = {'REC2':[[39,28,53.133637],[-0,20,7.650964],[55.867]],
                          'REC3': [[],[],[]],
                          'REC4': [[],[],[]],
                          'REC5': [[],[],[]]}
    
    iframe_keys = list(iframe_coordinates.keys())
    iframe_values = np.array(list(iframe_coordinates.values()))

    # Adding keys as a separate row (with the help of np.vstack)
    iframe_matrix = np.vstack([iframe_keys, iframe_values.T])
    print(iframe_matrix)
    
    
    
    
    
    """ THIS IS WHEN WE ASK FOR THE COORDINATES USING A INTERFACE
    coordinates_list = []
    
    for i in range(1, n, 1):
        sensors[f"x{i}"] = float(input(f"Insert x{i} coordinate"))
        sensors[f"y{i}"] = float(input(f'Insert y{i}" coordinate'))
        sensors[f"z{i}"] = float(input(f'Insert z{i}" coordinate')) 
        
        coordinates_list.append(f"x{i}", f"y{i}", f"z{i}")
        
    """
    
    

def main():

    manual_sensors_coordinates_definition()

main()


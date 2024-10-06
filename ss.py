import numpy as np
import json
from coordenates import degrees_operations as do
# h_elipsoideal
 


############ i FRAME ###############

# latitude longitude helipsoidal coordinates [gedrees, minutes and seconds]
""" 
 """
 
"""
iframe_coordinates = {'REC2':[[],[]],
                      'REC3':[[],[]],
                      'REC4':[[],[]],
                      'REC5':[[],[]]}
lat_test = 39º28'53.133637"

"""


iframe_coordinates_dms = {
    
    
}

iframe_keys = list(iframe_coordinates.keys())
iframe_values = np.array(list(iframe_coordinates.values()))
print(iframe_values)
print(iframe_keys)
print(json.dumps(iframe_values,indent=4))

# Adding keys as a separate row (with the help of np.vstack)
iframe_matrix = np.vstack([iframe_keys, iframe_values.T])
print(iframe_matrix)

""" 
This function allow you to calculate the transformatio of geodetic coordinates to Cartesian coordinates

ϕ = latitude 
λ = longitude

X = (ν + h) cos ϕ cos λ
Y = (ν + h) cos ϕ sen λ

Z = [ν*(1 − e2 )+ h] sen ϕ

h = H + N

numpy operations -------------------
np.sin(x) — Sine of angles in radians
np.cos(x) — Cosine of angles in radians
np.tan(x) — Tangent of angles in radians
np.arcsin(x) — Inverse sine (arcsine), returns angle in radians
np.arccos(x) — Inverse cosine (arccosine), returns angle in radians
np.arctan(x) — Inverse tangent (arctangent), returns angle in radians
np.degrees(x) — Converts radians to degrees
np.radians(x) — Converts degrees to radians
"""

import numpy as np


def hight_operations(N, h=0, H=0, ter=True):

    while N:
        try:
            if ter != True:
                
                if h==0:
                    print('ERROR: No geodesic height H available, enter a H value and try again')
                    exit
                
                else:

                    H = h - N
                    return H

            else:

                if H == 0:

                    print('ERROR: No orthometric height H available, enter a H value and try again')
                    exit

                else:
                    
                    h = H + N
                    return h
        
        except:
            
            print("ERROR: No N available")
            exit
                
def _geodetic_to_Cartesian(e,v,h,latitude,longitude):
    
    # lat long and h to X Y Z
    grs80
    X = (v + h)*np.cos(latitude)*np.cos(longitude) #sin and cos in radians
    Y = (v + h)*np.cos(latitude)*np.sin(longitude) #sin and cos in radians
    Z = [v*[1-((e)**2)] + h]*np.sin(latitude) #sin and cos in radians
    
    #Z = ν 1 − e2 + h sen ϕ
    
    return X, Y, Z

def extract_latitude_longitude():
    
    
    return
    
    

def geodetic_to_Cartesian(v,h,latitude, longitude):
    hight_operations()
    _geodetic_to_Cartesian()



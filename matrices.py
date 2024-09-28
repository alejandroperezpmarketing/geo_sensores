import numpy as np

coordinates = {}
n = 3

#create a entry in a dictionary with a new dictionary with the a specific key + a number i of the range iteration
def sensors_definition(n=n):
    if n != "":
    #check if n is not empty
        global sensors
        sensors = {}
        for i in range(1,n,1):
            sensors[f'Sensor_{i}'] = {f'x{i}':'',f'y{i}':'',f'z{i}':''}
        print(sensors)
    else:
        return
    
    
def update_sensors_coordinates(n):
    coordinates = []
    for i in range(1,n,1):
        sensors[f'x{i}'] = float(input(f'Insert x{i} coordinate'))
        sensors[f'y{i}'] = float(input(f'Insert y{i}" coordinate'))
        sensors[f'z{i}'] = float(input(f'Insert z{i}" coordinate'))
        coordinates.append(f'x{i}', f'y{i}',f'z{i}')
        
    #update the value of xn yn and zn in the dictionary
    

#function that colect the coordinates from each sensor and update the dictionary

def main():
    n = int(input("Please enter a number: ")) + 1
    sensors_definition(n)

#main()
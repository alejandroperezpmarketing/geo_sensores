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


def update_sensors_coordinates(n=n):
    coordinates = []
    for i in range(1, n, 1):
        sensors[f"x{i}"] = float(input(f"Insert x{i} coordinate"))
        sensors[f"y{i}"] = float(input(f'Insert y{i}" coordinate'))
        sensors[f"z{i}"] = float(input(f'Insert z{i}" coordinate'))
        coordinates.append(f"x{i}", f"y{i}", f"z{i}")

    # update the value of xn yn and zn in the dictionary


# function that colect the coordinates from each sensor and update the dictionary


def main():

    sensors_definition()

    return sensors

main()


import numpy as np

"""
1 radian=π/180​ degrees
1 degree=180/π​ radians

"""
    
def degrees_to_radians(latitude,longitude):
    
    latitude_rad = np.radians(latitude)
    longitude_rad = np.radians(latitude)
    degrees = [latitude, longitude]
    radians = [latitude_rad,longitude_rad]
    
    print(f"{degrees} degrees is equal to {radians} radians")
    
    return latitude_rad, longitude_rad

def radians_to_degrees(latitude_rad,longitude_rad):
    
    latitude = np.degrees(latitude_rad)
    longitude = np.degrees(longitude_rad)
    
    degrees = [latitude, longitude]
    radians = [latitude_rad,longitude_rad]
    
    print(f"latitude and longitude {radians} radians is equal to {degrees} degrees")

    return latitude, longitude

    
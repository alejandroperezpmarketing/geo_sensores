from pyproj import CRS
import numpy as np

def get_ref_elipsoid_parameters(epsg="GRS80",latitude=0):
    # Define the CRS (Coordinate Reference System) that uses the GRS 80 ellipsoid
    # EPSG:7019 corresponds to the GRS 80 ellipsoid

    # Define the GRS 80 ellipsoid using its name
    grs80 = CRS.from_string("GRS80")

    # Extract the ellipsoid parameters
    semi_major_axis = grs80.ellipsoid.semi_major_metre  # Semi-major axis (a)
    inverse_flattening = grs80.ellipsoid.inverse_flattening  # Inverse flattening (1/f)

    # Calculate the semi-minor axis and flattening manually
    flattening = 1 / inverse_flattening
    semi_minor_axis = semi_major_axis * (1 - flattening)

    # Print the parameters
    print(f"Semi-major axis (a): {semi_major_axis} meters")
    print(f"Semi-minor axis (b): {semi_minor_axis} meters")
    print(f"Flattening (f): {flattening}")
    print(f"Inverse Flattening (1/f): {inverse_flattening}")
    
    ######Calculation of r, N, e, e² and M
    
    e= np.sqrt((2*flattening-(flattening**2)))
    e_cuadrado  = ((2*flattening)-(flattening**2))
    return semi_major_axis, semi_minor_axis, flattening, inverse_flattening


get_ref_elipsoid_parameters()

def r_M_N_calculation(semi_minor_axis,semi_major_axis,latitude,longitude,e_cuadrado):
    #M = (semi_major_axis**(1-e_cuadrado))/(1-((e_cuadrado*np.sin(longitude))))
    r = (semi_minor_axis)/(np.sqrt(1-(np.cos(latitude))))
    #N = 
    return r


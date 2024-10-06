import numpy as np
import json

# Heliosoidal coordinates [degrees, minutes and seconds]
iframe_coordinates = {
    'REC2': [[39, 28, 53.133637], [-0, 20, 7.650964]],
    'REC3': [[39, 28, 53.109885], [-0, 20, 7.663129]],
    'REC4': [[39, 28, 53.143535], [-0, 20, 7.680928]],
    'REC5': [[39, 28, 53.119474], [-0, 20, 7.693816]]
}

iframe_keys = list(iframe_coordinates.keys())
iframe_values = np.array(list(iframe_coordinates.values()))

# Print the values and keys
print("Iframe Values:")
print(iframe_values)
print("\nIframe Keys:")
print(iframe_keys)

# Print the values as JSON
print("\nIframe Values in JSON format:")
print(json.dumps(iframe_values.tolist(), indent=4))  # Use .tolist() to convert numpy array to list

# Adding keys as a separate row (with the help of np.column_stack)
iframe_matrix = np.column_stack((iframe_keys, iframe_values.reshape(iframe_values.shape[0], -1)))
print("\nIframe Matrix:")
print(iframe_matrix)


from PIL import Image
import numpy as np

filename = input("Enter image path: ")

image = Image.open(filename)

array = np.array(image)

print("\nIMAGE INFORMATION")
print("----------------------")
print("Shape:", array.shape)
print("Data type:", array.dtype)


if len(array.shape) == 2:

    unique_values = np.unique(array)

    print("Number of channels: 1")
    print("Number of unique pixel values:", len(unique_values))

    if len(unique_values) == 2:
        print("\nClassification: BINARY IMAGE")
        print("Reason: The image contains only two pixel values.")

    else:
        print("\nClassification: GRAYSCALE IMAGE")
        print("Reason: The image has one channel and more than two intensity values.")
elif len(array.shape) == 3:

    channels = array.shape[2]

    print("Number of channels:", channels)

    if channels >= 3:
        print("\nClassification: COLOR IMAGE")
        print("Reason: The image has multiple color channels.")

    else:
        print("\nClassification: GRAYSCALE IMAGE")

else:
    print("\nClassification: UNKNOWN IMAGE FORMAT")

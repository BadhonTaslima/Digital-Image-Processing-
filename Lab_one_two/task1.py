from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

color_image = Image.open("images/color.jpg")
color_array = np.array(color_image)

height, width = color_array.shape[:2]

if len(color_array.shape) == 3:
    channels = color_array.shape[2]
else:
    channels = 1

print("COLOR IMAGE")
print("----------------------")
print("Width:", width)
print("Height:", height)
print("Channels:", channels)
print("Data type:", color_array.dtype)

plt.imshow(color_image)
plt.title("Color Image")
plt.axis("off")
plt.show()

print("\nTrying to open grayscale image...")

gray_image = Image.open("images/grayscale.png")
print("Grayscale image opened successfully!")

gray_image = gray_image.convert("L")
gray_array = np.array(gray_image)

height, width = gray_array.shape

print("\nGRAYSCALE IMAGE")
print("----------------------")
print("Width:", width)
print("Height:", height)
print("Channels:", 1)
print("Data type:", gray_array.dtype)

plt.imshow(gray_image, cmap="gray")
plt.title("Grayscale Image")
plt.axis("off")
plt.show()

print("Grayscale image displayed successfully!")
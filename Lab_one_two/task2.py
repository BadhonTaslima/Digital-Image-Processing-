
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

color_image = Image.open("images/color.jpg").convert("RGB")

gray_image = color_image.convert("L")

color_array = np.array(color_image)
gray_array = np.array(gray_image)
plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(color_image)
plt.title("Original Color Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(gray_image, cmap="gray")
plt.title("Converted Grayscale Image")
plt.axis("off")

plt.tight_layout()
plt.show()

print("ORIGINAL COLOR IMAGE")
print("----------------------")
print("Shape:", color_array.shape)
print("Width:", color_array.shape[1])
print("Height:", color_array.shape[0])
print("Channels:", color_array.shape[2])
print("Data type:", color_array.dtype)
print("Data size:", color_array.nbytes, "bytes")

print("\nCONVERTED GRAYSCALE IMAGE")
print("----------------------")
print("Shape:", gray_array.shape)
print("Width:", gray_array.shape[1])
print("Height:", gray_array.shape[0])
print("Channels:", 1)
print("Data type:", gray_array.dtype)
print("Data size:", gray_array.nbytes, "bytes")
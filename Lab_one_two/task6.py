
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("images/grayscale.png").convert("L")

sizes = [128, 64, 32, 16]

plt.figure(figsize=(12, 10))

plt.subplot(2, 3, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

for i, size in enumerate(sizes):

    resized = image.resize((size, size), Image.Resampling.NEAREST)

    plt.subplot(2, 3, i + 2)
    plt.imshow(resized, cmap="gray")
    plt.title(str(size) + " × " + str(size))
    plt.axis("off")

plt.tight_layout()
plt.show()

print("SPATIAL RESOLUTION")
print("----------------------")
print("Original image size:", image.size)

for size in sizes:
    print("Resampled image:", size, "×", size)

print("\nIntensity resolution is fixed at 8 bits")
print("Number of gray levels = 256")


from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("images/grayscale.png").convert("L")

gray = np.array(image)

levels = [256, 128, 64, 32, 16, 8, 4, 2]


plt.figure(figsize=(16, 10))

for i, level in enumerate(levels):

    step = 256 // level

    reduced = (gray // step) * step

    reduced = np.clip(reduced, 0, 255).astype(np.uint8)

    plt.subplot(2, 4, i + 1)
    plt.imshow(reduced, cmap="gray")
    plt.title(str(level) + " Gray Levels")
    plt.axis("off")

plt.tight_layout()
plt.show()

print("INTENSITY RESOLUTION")
print("----------------------")

for level in levels:
    print("Gray levels:", level)

print("\nOriginal intensity resolution: 8 bits")
print("Original number of gray levels: 256")

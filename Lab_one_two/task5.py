
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("images/grayscale.png").convert("L")

gray = np.array(image)

thresholds = [50, 128, 200]

plt.figure(figsize=(12, 8))

plt.subplot(2, 2, 1)
plt.imshow(gray, cmap="gray")
plt.title("Original Grayscale Image")
plt.axis("off")

for i, threshold in enumerate(thresholds):

    binary = np.where(gray >= threshold, 255, 0).astype(np.uint8)

    plt.subplot(2, 2, i + 2)
    plt.imshow(binary, cmap="gray")
    plt.title("Threshold = " + str(threshold))
    plt.axis("off")


plt.tight_layout()
plt.show()


print("THRESHOLDING RESULTS")
print("----------------------")

for threshold in thresholds:
    print("Threshold value:", threshold)
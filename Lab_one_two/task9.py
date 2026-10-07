
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt

image = Image.open("images/grayscale.png").convert("L")
gray = np.array(image)

dark_image = np.clip(gray * 0.4, 0, 255).astype(np.uint8)

bright_image = np.clip(gray * 1.5, 0, 255).astype(np.uint8)

low_contrast_image = np.clip(100 + (gray - 128) * 0.3, 0, 255).astype(np.uint8)


# FUNCTION TO DISPLAY IMAGE AND HISTOGRAM

def show_histogram(image, title):

    histogram = np.bincount(image.ravel(), minlength=256)

    plt.figure(figsize=(10, 5))
               
    plt.subplot(1, 2, 1)
    plt.imshow(image, cmap="gray")
    plt.title(title)
    plt.axis("off")

    plt.subplot(1, 2, 2)
    plt.bar(range(256), histogram)
    plt.title(title + " Histogram")
    plt.xlabel("Intensity Level")
    plt.ylabel("Pixel Count")
    plt.xlim(0, 255)

    plt.tight_layout()
    plt.show()


show_histogram(dark_image, "Dark Image")

show_histogram(bright_image, "Bright Image")

show_histogram(low_contrast_image, "Low-Contrast Image")

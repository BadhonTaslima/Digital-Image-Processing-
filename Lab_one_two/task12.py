
from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt


image1 = Image.open("images/grayscale.png").convert("L")
img1 = np.array(image1).astype(np.float32)
image2 = image1.copy()
draw = ImageDraw.Draw(image2)

width, height = image2.size

draw.rectangle(
    (width // 2, height // 2,
     width // 2 + 50, height // 2 + 50),
    fill=25
)
img2 = np.array(image2).astype(np.float32)


# IMAGE ARITHMETIC 

# Addition
addition = img1 + img2

# Subtraction
subtraction = np.abs(img1 - img2)

# Multiplication
multiplication = img1 * img2

# Division
division = img1 / (img2 + 1)


# NORMALIZE RESULTS 

def normalize(image):
    image = image - image.min()

    if image.max() != 0:
        image = image / image.max() * 255

    return image.astype(np.uint8)


addition = normalize(addition)
subtraction = normalize(subtraction)
multiplication = normalize(multiplication)
division = normalize(division)


# DISPLAY RESULTS
 
plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(img1, cmap="gray")
plt.title("Image 1")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(img2, cmap="gray")
plt.title("Image 2")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(addition, cmap="gray")
plt.title("Addition")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(subtraction, cmap="gray")
plt.title("Subtraction / Change Detection")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(multiplication, cmap="gray")
plt.title("Multiplication")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(division, cmap="gray")
plt.title("Division")
plt.axis("off")

plt.tight_layout()
plt.show()

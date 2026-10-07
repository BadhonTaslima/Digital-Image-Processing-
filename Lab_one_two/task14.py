from PIL import Image, ImageDraw
import numpy as np
import matplotlib.pyplot as plt

# CREATE TWO BINARY IMAGES 

size = 256

# Create black images

image1 = Image.new("L", (size, size), 0)
image2 = Image.new("L", (size, size), 0)

# Drawing objects

draw1 = ImageDraw.Draw(image1)
draw2 = ImageDraw.Draw(image2)

# IMAGE 1: CIRCLE 

draw1.ellipse(
    (50, 70, 170, 190),
    fill=255
)

# IMAGE 2: SQUARE

draw2.rectangle(
    (110, 100, 210, 200),
    fill=255
)

# Convert to NumPy arrays

A = np.array(image1)
B = np.array(image2)


# CONVERT TO BINARY

A_binary = A > 0
B_binary = B > 0


# LOGICAL OPERATIONS 

# AND
AND_result = np.logical_and(A_binary, B_binary)

# OR
OR_result = np.logical_or(A_binary, B_binary)

# NOT
NOT_A_result = np.logical_not(A_binary)

# XOR
XOR_result = np.logical_xor(A_binary, B_binary)


# DISPLAY RESULTS 

plt.figure(figsize=(12, 8))

plt.subplot(2, 3, 1)
plt.imshow(A_binary, cmap="gray")
plt.title("Image A - Circle")
plt.axis("off")

plt.subplot(2, 3, 2)
plt.imshow(B_binary, cmap="gray")
plt.title("Image B - Square")
plt.axis("off")

plt.subplot(2, 3, 3)
plt.imshow(AND_result, cmap="gray")
plt.title("AND")
plt.axis("off")

plt.subplot(2, 3, 4)
plt.imshow(OR_result, cmap="gray")
plt.title("OR")
plt.axis("off")

plt.subplot(2, 3, 5)
plt.imshow(NOT_A_result, cmap="gray")
plt.title("NOT A")
plt.axis("off")

plt.subplot(2, 3, 6)
plt.imshow(XOR_result, cmap="gray")
plt.title("XOR")
plt.axis("off")

plt.tight_layout()
plt.show()
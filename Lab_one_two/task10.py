
from PIL import Image
import numpy as np


# FIND PIXEL NEIGHBORS 

def find_neighbors(image, x, y):

    height, width = image.shape

    # 4-neighbors
    N4 = []

    # Up
    if x > 0:
        N4.append((x - 1, y))

    # Down
    if x < height - 1:
        N4.append((x + 1, y))

    # Left
    if y > 0:
        N4.append((x, y - 1))

    # Right
    if y < width - 1:
        N4.append((x, y + 1))


    # Diagonal neighbors
    ND = []

    # Top-left
    if x > 0 and y > 0:
        ND.append((x - 1, y - 1))

    # Top-right
    if x > 0 and y < width - 1:
        ND.append((x - 1, y + 1))

    # Bottom-left
    if x < height - 1 and y > 0:
        ND.append((x + 1, y - 1))

    # Bottom-right
    if x < height - 1 and y < width - 1:
        ND.append((x + 1, y + 1))


    # 8-neighbors = 4-neighbors + diagonal neighbors
    N8 = N4 + ND

    return N4, ND, N8



image = Image.open("images/grayscale.png").convert("L")
array = np.array(image)


# Middle pixel
x1 = array.shape[0] // 2
y1 = array.shape[1] // 2

N4, ND, N8 = find_neighbors(array, x1, y1)

print("MIDDLE PIXEL")
print("----------------------")
print("Pixel:", (x1, y1))
print("N4 =", N4)
print("ND =", ND)
print("N8 =", N8)


# Edge pixel
x2 = 0
y2 = array.shape[1] // 2

N4, ND, N8 = find_neighbors(array, x2, y2)

print("\nEDGE PIXEL")
print("----------------------")
print("Pixel:", (x2, y2))
print("N4 =", N4)
print("ND =", ND)
print("N8 =", N8)


# Corner pixel
x3 = 0
y3 = 0

N4, ND, N8 = find_neighbors(array, x3, y3)

print("\nCORNER PIXEL")
print("----------------------")
print("Pixel:", (x3, y3))
print("N4 =", N4)
print("ND =", ND)
print("N8 =", N8)

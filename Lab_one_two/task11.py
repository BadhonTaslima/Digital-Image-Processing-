
import math

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))

x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

dx = abs(x2 - x1)
dy = abs(y2 - y1)

euclidean = math.sqrt(dx ** 2 + dy ** 2)

d4 = dx + dy
d8 = max(dx, dy)

print("\nDISTANCE MEASURES")
print("----------------------")

print("Pixel 1:", (x1, y1))
print("Pixel 2:", (x2, y2))

print("Euclidean Distance =", euclidean)
print("City-block Distance (D4) =", d4)
print("Chessboard Distance (D8) =", d8)

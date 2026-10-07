
from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("images/grayscale.png").convert("L")

# Resize original image to 64 × 64
small_image = image.resize((64, 64), Image.Resampling.LANCZOS)

# Nearest-neighbor interpolation
nearest = small_image.resize(
    (256, 256),
    Image.Resampling.NEAREST
)

# Bilinear interpolation
bilinear = small_image.resize(
    (256, 256),
    Image.Resampling.BILINEAR
)

# Bicubic interpolation
bicubic = small_image.resize(
    (256, 256),
    Image.Resampling.BICUBIC
)


plt.figure(figsize=(15, 5))

plt.subplot(1, 3, 1)
plt.imshow(nearest, cmap="gray")
plt.title("Nearest-Neighbor")
plt.axis("off")

plt.subplot(1, 3, 2)
plt.imshow(bilinear, cmap="gray")
plt.title("Bilinear")
plt.axis("off")

plt.subplot(1, 3, 3)
plt.imshow(bicubic, cmap="gray")
plt.title("Bicubic")
plt.axis("off")

plt.tight_layout()
plt.show()


print("IMAGE INTERPOLATION")
print("----------------------")
print("Original resized image: 64 × 64")
print("Enlarged image: 256 × 256")
print("Scale factor: 4×")
print("Methods tested:")
print("1. Nearest-neighbor")
print("2. Bilinear")
print("3. Bicubic")

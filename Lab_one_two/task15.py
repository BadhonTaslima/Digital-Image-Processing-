from PIL import Image
import matplotlib.pyplot as plt

image = Image.open("images/grayscale.png").convert("L")

width, height = image.size


# 1. TRANSLATION 
# Moving image 50 pixels right and 30 pixels down

tx = 50
ty = 30

translated = image.transform(
    (width, height),
    Image.Transform.AFFINE,
    (1, 0, -tx, 0, 1, -ty),
    resample=Image.Resampling.BILINEAR
)


# 2. ROTATION
# Rotating image by 30 degrees around its center

angle = 30

rotated = image.rotate(
    angle,
    resample=Image.Resampling.BILINEAR,
    expand=False,
    fillcolor=0
)


# 3. SCALING
# Scaling image by a factor of 1.5

scale_factor = 1.5

new_width = int(width * scale_factor)
new_height = int(height * scale_factor)

scaled = image.resize(
    (new_width, new_height),
    Image.Resampling.BILINEAR
)


# DISPLAY RESULTS 

plt.figure(figsize=(14, 8))

# Original

plt.subplot(2, 2, 1)
plt.imshow(image, cmap="gray")
plt.title("Original Image")
plt.axis("off")

# Translation

plt.subplot(2, 2, 2)
plt.imshow(translated, cmap="gray")
plt.title("Translation: x=50, y=30")
plt.axis("off")

# Rotation

plt.subplot(2, 2, 3)
plt.imshow(rotated, cmap="gray")
plt.title("Rotation: 30 degrees")
plt.axis("off")

# Scaling

plt.subplot(2, 2, 4)
plt.imshow(scaled, cmap="gray")
plt.title("Scaling: 1.5×")
plt.axis("off")

plt.tight_layout()
plt.show()


# INFORMATION 

print("BASIC GEOMETRIC TRANSFORMATIONS")
print("--------------------------------")
print("Original size:", width, "×", height)

print("\nTranslation:")
print("X direction:", tx, "pixels")
print("Y direction:", ty, "pixels")

print("\nRotation:")
print("Angle:", angle, "degrees")

print("\nScaling:")
print("Scale factor:", scale_factor)
print("New size:", new_width, "×", new_height)
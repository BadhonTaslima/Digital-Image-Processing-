from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
 
image = Image.open("images/grayscale.png").convert("L")

# Convert image to NumPy array
clean = np.array(image).astype(np.float32)

# Number of noisy images
num_images = 20

# Store all noisy images
noisy_images = []

# GENERATE 20 NOISY IMAGES 
for i in range(num_images):

    # Generate Gaussian noise

    noise = np.random.normal(0, 25, clean.shape)

    # Add noise to the clean image

    noisy = clean + noise

    # Keep pixel values between 0 and 255

    noisy = np.clip(noisy, 0, 255)

    # Store noisy image

    noisy_images.append(noisy)


# AVERAGE ALL 20 IMAGES
 
noisy_stack = np.array(noisy_images)

average_image = np.mean(noisy_stack, axis=0)

# Convert to uint8

average_image = np.clip(average_image, 0, 255).astype(np.uint8)


# DISPLAY 

plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.imshow(noisy_images[0], cmap="gray")
plt.title("One Noisy Image")
plt.axis("off")

plt.subplot(1, 2, 2)
plt.imshow(average_image, cmap="gray")
plt.title("Average of 20 Noisy Images")
plt.axis("off")

plt.tight_layout()
plt.show()


# INFORMATION
 
print("NOISE REDUCTION BY IMAGE AVERAGING")
print("-----------------------------------")
print("Number of noisy images:", num_images)
print("Gaussian noise mean:", 0)
print("Gaussian noise standard deviation:", 25)
print("Image size:", clean.shape)
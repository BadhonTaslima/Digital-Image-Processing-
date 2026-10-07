
from PIL import Image
import matplotlib.pyplot as plt

images = [
    ("images/xray.jpg",
     "X-ray",
     "Used in medical diagnosis, especially for detecting bone fractures."),

    ("images/satellite.jpg",
     "Satellite / Remote Sensing",
     "Used for land-use mapping, agriculture, and environmental monitoring."),

    ("images/microscopy.jpg",
     "Microscopy",
     "Used to observe cells, microorganisms, and biological structures."),

    ("images/ultrasound.png",
     "Ultrasound",
     "Used in medical imaging to examine organs and monitor pregnancy."),

    ("images/infrared.jpeg",
     "Infrared",
     "Used for thermal imaging and detecting heat patterns.")
]

for filename, modality, application in images:

    image = Image.open(filename)

    
    plt.imshow(image, cmap="gray")
    plt.title(modality)
    plt.axis("off")
    plt.show()

    print("Modality:", modality)
    print("Application:", application)
    print("------------------------------")

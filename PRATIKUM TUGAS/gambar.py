import numpy as np
import imageio.v2 as imageio  
import matplotlib.pyplot as plt


def show_image(image, title):
    plt.imshow(image)
    plt.title(title)
    plt.axis('off')
    plt.show()


def load_image(image_path):
    return imageio.imread(image_path)


def get_red_channel(image):
    red_channel = image.copy()
    red_channel[:, :, 1] = 0  
    red_channel[:, :, 2] = 0  
    return red_channel


def get_green_channel(image):
    green_channel = image.copy()
    green_channel[:, :, 0] = 0  
    green_channel[:, :, 2] = 0  
    return green_channel


def get_blue_channel(image):
    blue_channel = image.copy()
    blue_channel[:, :, 0] = 0  
    blue_channel[:, :, 1] = 0  
    return blue_channel


def convert_to_grayscale(image):
    grayscale_image = np.dot(image[..., :3], [0.2989, 0.5870, 0.1140])
    return grayscale_image


def convert_to_binary(image, threshold=128):
    grayscale_image = convert_to_grayscale(image)
    binary_image = (grayscale_image > threshold).astype(np.uint8) * 255
    return binary_image


image_paths = [
    'daun_pepaya.jpg',
    'daun_singkong.jpg',
    'kenikir.jpg'
]


for image_path in image_paths:
    print(f"Processing: {image_path}")
    
    
    image = load_image(image_path)
   
    red_channel = get_red_channel(image)
    show_image(red_channel, f"Red Channel - {image_path}")
   
    green_channel = get_green_channel(image)
    show_image(green_channel, f"Green Channel - {image_path}")

    blue_channel = get_blue_channel(image)
    show_image(blue_channel, f"Blue Channel - {image_path}")

    grayscale_image = convert_to_grayscale(image)
    plt.imshow(grayscale_image, cmap='gray')
    plt.title(f"Grayscale Image - {image_path}")
    plt.axis('off')
    plt.show()

    binary_image = convert_to_binary(image, threshold=128)
    plt.imshow(binary_image, cmap='gray')
    plt.title(f"Binary (Threshold) Image - {image_path}")
    plt.axis('off')
    plt.show()
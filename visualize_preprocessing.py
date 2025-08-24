import matplotlib.pyplot as plt
from preprocess_food_images import preprocess_image
import numpy as np
from PIL import Image
import os

def visualize_preprocessing(image_path, processed_path, augment=False):
    preprocess_image(image_path, processed_path, augment=augment)

    original = Image.open(image_path)
    processed = Image.open(processed_path)

    fig, axs = plt.subplots(1, 2, figsize=(8, 4))
    axs[0].imshow(original)
    axs[0].set_title("Original")
    axs[0].axis("off")

    axs[1].imshow(processed)
    axs[1].set_title("Processed")
    axs[1].axis("off")

    plt.show()


if __name__ == "__main__":
    sample_img = "./samples/pizza.jpg"
    processed_img = "./processed/pizza_demo.jpg"
    os.makedirs("./processed", exist_ok=True)
    visualize_preprocessing(sample_img, processed_img, augment=True)



import cv2
import numpy as np
import argparse
import os
from PIL import Image, ImageEnhance
import random

def preprocess_image(image_path, output_path, size=(224, 224), augment=False):
    """
    Preprocess a food image for classification.
    
    Steps:
    1. Resize to model input size (default: 224x224).
    2. Normalize pixel values to [0,1].
    3. (Optional) Apply augmentation (rotation, flips, brightness).
    4. Save processed image.
    """

    # Load image
    image = Image.open(image_path).convert("RGB")

    # Resize
    image = image.resize(size)

    # Augmentation (if enabled)
    if augment:
        if random.random() > 0.5:
            image = image.transpose(Image.FLIP_LEFT_RIGHT)  # horizontal flip
        if random.random() > 0.5:
            angle = random.choice([90, 180, 270])
            image = image.rotate(angle)
        if random.random() > 0.5:
            enhancer = ImageEnhance.Brightness(image)
            image = enhancer.enhance(random.uniform(0.7, 1.3))  # adjust brightness

    # Convert to numpy array
    img_array = np.array(image).astype("float32")

    # Normalize pixel values (0-1 range)
    img_array /= 255.0

    # Save processed image
    processed_image = Image.fromarray((img_array * 255).astype(np.uint8))
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    processed_image.save(output_path)

    print(f"✅ Processed image saved at {output_path}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Preprocess food images for NutriBot classifier.")
    parser.add_argument("input", help="Path to input image")
    parser.add_argument("output", help="Path to save processed image")
    parser.add_argument("--augment", action="store_true", help="Apply data augmentation")
    args = parser.parse_args()

    preprocess_image(args.input, args.output, augment=args.augment)

from PIL import Image, ImageEnhance
import random

def apply_augmentations(image):
    if random.random() > 0.5:
        image = image.transpose(Image.FLIP_LEFT_RIGHT)
    if random.random() > 0.5:
        angle = random.choice([90, 180, 270])
        image = image.rotate(angle)
    if random.random() > 0.5:
        enhancer = ImageEnhance.Brightness(image)
        image = enhancer.enhance(random.uniform(0.7, 1.3))
    return image

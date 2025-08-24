import os
import argparse
from preprocess_food_images import preprocess_image

def batch_preprocess(input_dir, output_dir, augment=False):
    """
    Preprocess all images in a folder.
    """
    os.makedirs(output_dir, exist_ok=True)

    for file in os.listdir(input_dir):
        if file.lower().endswith((".jpg", ".jpeg", ".png")):
            input_path = os.path.join(input_dir, file)
            output_path = os.path.join(output_dir, file)
            preprocess_image(input_path, output_path, augment=augment)

    print(f"✅ Batch preprocessing completed. Files saved in {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Batch preprocess food images.")
    parser.add_argument("input_dir", help="Path to input folder of images")
    parser.add_argument("output_dir", help="Path to save processed images")
    parser.add_argument("--augment", action="store_true", help="Apply data augmentation")
    args = parser.parse_args()

    batch_preprocess(args.input_dir, args.output_dir, augment=args.augment)

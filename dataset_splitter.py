import os
import shutil
import argparse
import random

def split_dataset(input_dir, output_dir, train_ratio=0.7, val_ratio=0.15):
    """
    Splits dataset into train, validation, and test folders.
    """
    os.makedirs(output_dir, exist_ok=True)

    categories = [d for d in os.listdir(input_dir) if os.path.isdir(os.path.join(input_dir, d))]

    for category in categories:
        files = [f for f in os.listdir(os.path.join(input_dir, category)) if f.lower().endswith((".jpg", ".jpeg", ".png"))]
        random.shuffle(files)

        train_end = int(train_ratio * len(files))
        val_end = train_end + int(val_ratio * len(files))

        splits = {
            "train": files[:train_end],
            "val": files[train_end:val_end],
            "test": files[val_end:]
        }

        for split, split_files in splits.items():
            split_dir = os.path.join(output_dir, split, category)
            os.makedirs(split_dir, exist_ok=True)

            for file in split_files:
                src = os.path.join(input_dir, category, file)
                dst = os.path.join(split_dir, file)
                shutil.copy(src, dst)

    print(f"✅ Dataset split into train/val/test at {output_dir}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split dataset into train, val, and test sets.")
    parser.add_argument("input_dir", help="Input dataset directory (with category folders)")
    parser.add_argument("output_dir", help="Output directory for train/val/test")
    parser.add_argument("--train_ratio", type=float, default=0.7, help="Train set ratio")
    parser.add_argument("--val_ratio", type=float, default=0.15, help="Validation set ratio")
    args = parser.parse_args()

    split_dataset(args.input_dir, args.output_dir, args.train_ratio, args.val_ratio)

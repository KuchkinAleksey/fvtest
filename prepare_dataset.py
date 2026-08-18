import glob
import os

import cv2

INPUT = "zavod70/*"        # folder with the original DJI photos
OUTPUT = "data/zavod70"    # folder NAME becomes the ViPE sequence name
OUTPUT_WIDTH = 640
OUTPUT_HEIGHT = 480
JPEG_QUALITY = 100

os.makedirs(OUTPUT, exist_ok=True)
files = sorted(glob.glob(INPUT))

n = 0
for path in files:
    img = cv2.imread(path)
    if img is None:
        print(f"skip {path}")
        continue

    out = cv2.resize(img, (OUTPUT_WIDTH, OUTPUT_HEIGHT), interpolation=cv2.INTER_AREA)

    cv2.imwrite(f"{OUTPUT}/frame_{n:05d}.jpg", out,
                [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
    print(f"{n + 1}/{len(files)}", end="\r")
    n += 1

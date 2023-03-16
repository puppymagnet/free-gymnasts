from PIL import Image
import sys
import pytesseract
import numpy as np

def main(file_path: str):
    image = img1 = np.array(Image.open(file_path))
    text = pytesseract.image_to_string(img1)

    print(text)

    return


if __name__ == "__main__":
    main(sys.argv[1])
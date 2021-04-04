# data extractor extracts the data from the picture (date & Location)

from exif import Image

with open(r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures\356E0.jpg", "rb") as palm_1_file:
    image = Image(palm_1_file)

print(f"{image.datetime_original}\n")





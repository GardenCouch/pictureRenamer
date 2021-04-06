# data extractor extracts the data from the picture (date & Location)

from exif import Image
import os
from pathlib import Path

path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

dir = path

for count, filename in enumerate(os.listdir(dir)):
    print(filename)

    file_path = os.path.join(dir + "\\" + filename)
    print(file_path)
   

    image = Image(open(file_path, "r", encoding= "Latin-1"))
    print(type(image))
    if image.has_exif:
        print(f"{image.datetime_original}\n")
    else:
        print("no exif")

    print("---------------")




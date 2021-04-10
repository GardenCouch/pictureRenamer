# data extractor extracts the data from the picture (date & Location)

import os
from PIL import Image, ExifTags

path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

dir = path
filename = "35g6k4ldE33.jpg"

file_path_test = os.path.join(dir + "\\" + filename)

def exif_tester(file_path):
    img = Image.open(file_path)
    img_exif = img.getexif()
    print(type(img_exif))
    # <class 'PIL.Image.Exif'>

    if img_exif == {} :
        print('Sorry, image has no exif data.')
        has_exif = False
    else:
        print("there is a exif file")
        has_exif = True

    return has_exif

b = exif_tester(file_path_test)
print(b)

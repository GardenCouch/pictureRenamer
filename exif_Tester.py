# data extractor extracts the data from the picture (date & Location)

import os
from PIL import Image, ExifTags

path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

dir = path
filename = "35g6k4ldE33.jpg"

file_path_test = os.path.join(dir + "\\" + filename)

#function that test if there is an exif file or not. the function returns a variable has_exif that is either true or false. 
# the input is the file path
def exif_tester(file_path):
    img = Image.open(file_path)
    img_exif = img.getexif()

    if img_exif == {} :
        has_exif = False
    else:
        has_exif = True

    return has_exif



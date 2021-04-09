import PIL.Image
from PIL.ExifTags import TAGS
import os

path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

dir = path

#path = "C:\\Users\\Joost\\Documents\\Dapseontour\\Development\\Picture_analysis\\Pictures\\Oostenrijk Feb 202.jpg"


def date_extractor(filepath):

    img = PIL.Image.open(filepath)    

    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }

    print(exif['DateTimeOriginal'])

for filename in os.listdir(dir):
    src = os.path.join(dir, filename)
    print(src)
    date_extractor(src)





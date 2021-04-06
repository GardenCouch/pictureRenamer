from exif import Image
import os

 
with open(r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures\Oostenrijk Feb 202.jpg", encoding= "Latin-1") as image_original:
    image_original = Image(image_original)
    print(type(image_original))
    print(image_original.has_exif)
    

import PIL.Image
from PIL.ExifTags import TAGS
img = PIL.Image.open(r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures\Oostenrijk Feb 202.jpg")    

def get_field (exif,field) :
      for (k,v) in exif.items():
        if TAGS.get(k) == field:
            return v


exif_data = img._getexif()

exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}
print(exif)

print(get_field(exif_data,'DateTimeOriginal'))





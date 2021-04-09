import PIL.Image
from PIL.ExifTags import TAGS
img = PIL.Image.open(r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures\Oostenrijk Feb 202.jpg")    





exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS
}

print(exif['DateTimeOriginal'])




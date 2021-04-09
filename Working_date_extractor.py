import PIL.Image
from PIL.ExifTags import TAGS
import os

#the directory that the pictures are in
path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

#the path of the directory 
dir = path

#data extractor exif file. use print exif to see whats in the exif file available
def exif_data_extractor(filepath):

    img = PIL.Image.open(filepath)    

    exif = {
        PIL.ExifTags.TAGS[k]: v
        for k, v in img._getexif().items()
        if k in PIL.ExifTags.TAGS
    }
    datetimeoriginal = exif['DateTimeOriginal']
    #gps = exif['GPSInfo']
    return datetimeoriginal
    
#create empty dictionairy to store the data 
picture_data_dict = {'filename': [] , "date":[]}

for filename in os.listdir(dir):
    #join source and filename in to push in the exif data exstraction
    src = os.path.join(dir, filename)
    # get data from exif data extractor
    date = exif_data_extractor(src)

    #ad data to empty library
    picture_data_dict['filename'].append(filename)
    picture_data_dict['date'].append(date)

print(picture_data_dict)

#data cleaning in dictionairy

#ad test if exif file 
#https://stackoverflow.com/questions/4764932/in-python-how-do-i-read-the-exif-data-for-an-image




import PIL.Image
from PIL.ExifTags import TAGS
import os
from exif_Tester import exif_tester

#the directory that the pictures are in
path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

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
    
def picture_data_generator(directory_path):
    dir= directory_path
    #create empty dictionairy to store the data 
    picture_data_dict = {'filename': [] , "date":[]}

    for filename in os.listdir(dir):
        #join source and filename in to push in the exif data exstraction
        src = os.path.join(dir, filename)
        
        # use the exif tester function to determine the state (has exif or not)
        exif_state = exif_tester(src)

        # if there is a exif file use the data extractor function to extract the relevant information
        if exif_state == True:    
            date = exif_data_extractor(src)
            #ad data to empty library
            picture_data_dict['filename'].append(filename)
            picture_data_dict['date'].append(date)
        else:
            print(filename + ": " + "has no exif!")

    return picture_data_dict

data = picture_data_generator(path)



#data cleaning in dictionairy



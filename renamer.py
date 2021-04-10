# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
from exif import Image
#from Working_date_extractor import date_extractor
# Function to rename multiple files

def main():
    #change path to the relevant folder
    path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

    dir = path
    for count, filename in enumerate(os.listdir(dir)):
        print("----------------------------------------")
        print(os.path.abspath(filename)) # this prints the file path. I can ad the filepath in the dat extractor to turn it into a Image file
        print("----------------------------------------")

        dst = os.path.join(dir, f"35g6k4ldE3{count}.jpg")
        src = os.path.join(dir, filename)
        print(dst)
        os.rename(src, dst)
        
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
  
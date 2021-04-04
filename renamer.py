# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os
from exif import Image

# Function to rename multiple files


def main():
    #change path to the relevant folder
    path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

    dir = path
    for count, filename in enumerate(os.listdir(dir)):
        print(os.path.abspath(filename)) # this prints the file path. I can ad the filepath in the dat extractor to turn it into a Image file


        dst = os.path.join(dir, f"356E{count}.jpg")
        src = os.path.join(dir, filename)

        os.rename(src, dst)
 

  


# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
  
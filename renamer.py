# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os

# Function to rename multiple files

#change path to the relevant folder
path= (r"C:\Users\Joost\Documents\Dapseontour\Development\Picture_analysis\Pictures")

def main():
    dir = path
    for count, filename in enumerate(os.listdir(dir)):
        dst = os.path.join(dir, f"356E{count}.jpg")
        src = os.path.join(dir, filename)
    
        os.rename(src, dst)
  
# Driver Code
if __name__ == '__main__':
      
    # Calling main() function
    main()
  
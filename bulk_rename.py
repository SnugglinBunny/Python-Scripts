import os

folderToRename = "rename"
  
# Function to rename multiple files
def main(filetype, newname):
  
    for count, filename in enumerate(os.listdir(folderToRename)):
        if filetype == os.path.splitext(filename)[1]:
            dst = f"{folderToRename}/{newname}{str(count)}{filetype}"
            src = f"{folderToRename}/{filename}"
            os.rename(src, dst)
        
  
# Driver Code - if this is the the main file running, no called from another file
if __name__ == '__main__':
    filetype = input("Which file type do you want to rename?")
    newname = input("What name would you like to use?")

    # Calling main() function
    main(filetype, newname)
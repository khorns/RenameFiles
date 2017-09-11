import shutil, os, re
from pathlib import Path

# Path of a current directory
path = os.getcwd()
path = path + "\Random3"
NFileName = "Moon"

# 
def renameFile():
    allFile = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    # allFile = os.listdir(path)
    i  = 1
    # allFile.sort()
    allFile = sorted(allFile, key=lambda x: (int(re.sub('\D','',x)),x))

    # for file in allFile:
    #     print(file)

    for file in allFile:
        OldPathName = os.path.join(path, file)
        ext = Path(OldPathName).suffix                    # Extension
        newName = NFileName + str(i)
        NewPathName = os.path.join(path, newName)
        NewPathName = NewPathName + ext
        
        # Renaming the file
        # os.rename(OldPathName, NewPathName)
        
        # Print 
        print(OldPathName)
        print(NewPathName)
        i = i + 1


    ### Handle FileExistsError

    # for file in [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]:
    #     print(file)
    #     newName = "Hello_" + str(i)
    #     os.rename(file, newName)
    #     i = i + 1

    

if __name__ == "__main__":
	renameFile()
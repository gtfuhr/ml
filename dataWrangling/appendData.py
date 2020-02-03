import os

def foldersExist(folderNames):
    if folderNames in os.listdir():
        return True
    return False
    
def createFolders(inputFolderName, outputFolderName):
    try:
        os.mkdir(inputFolderName)
        os.mkdir(outputFolderName)
        print("Sucessfully created input and output folder")
    except Exception as err:
        print(err)
        print("Can't create the output and output folders")
        exit(0)
        
def openFile(name, mode):
    try:
        return open(name,mode)
    except Exception as err:
        print(err)
        print("Can't open file {0} at mode {1}".format(name, mode))
        exit(0)

def appendData(inputFolderName,outputFolderName,originalFilename,appendFilename,outputFilename):
    with openFile(os.path.join(inputFolderName,appendFilename),'r') as newData:
        with openFile(os.path.join(inputFolderName,originalFilename), 'a') as original:
            original.write(newData.readlines())


def main():
    originalFilename = "original.csv"
    appendFilename = "append.csv"
    outputFilename = "output.csv"
    inputFolderName = "input"
    outputFolderName = "output"

    if foldersExist([inputFolderName,outputFolderName]):
        appendData(inputFolderName,outputFolderName,originalFilename,appendFilename,outputFilename)
    else:
        createFolders(inputFolderName, outputFolderName)
        print("Input and output folders created, now insert the {0} and the {1} in the {2} folder".format(originalFilename, appendFilename, inputFolderName))



if __name__ == "__main__":
    main()
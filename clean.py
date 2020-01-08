### This is a tiny script to organize Desktop files in directories by extensions
# 1. Create directories (images, docs)
# 2. List files which are image or document files
# 3. Move image files to ./images/ folder and 

import os

class Organize:
    def __init__(self, extension, folder):
        self.extension = extension
        self.folder = folder

    ## Return Current working cirectory path
    def cwd(self):
        return os.path.dirname(os.path.abspath(__file__))

    ## Filter files by extension in current working directory
    def filteredFiles(self):
        files = []
        for x in os.listdir(self.cwd()):
            for y in self.extension:
                if x.endswith(y): 
                    files.append(x)
        return files

    ## Create new folder to move files in (exception is passed if necessary)
    def newFolder(self):
        try:
            os.mkdir(clean.cwd()+os.sep+self.folder)   
        except FileExistsError:
            pass

    ## Generate source path of filtered files for further renaming
    def sourcesList(self):
        sourcePathList = [self.cwd()+os.sep+x for x in self.filteredFiles()]
        return sourcePathList

    ## Generate destination path of filtered files for further renaming
    def destinationsList(self):
        destinationPaths = [self.cwd() + os.sep + self.folder + os.sep + x for x in self.filteredFiles()]
        return destinationPaths

    ## Finally Move filtered files to set destination
    def renameFiles(self):
        self.newFolder()
        for x,y in zip(self.sourcesList(),self.destinationsList()):
            os.rename(x,y)


docs = [".doc",".docx",".xls",".xlsx",".pdf"]
images = [".jpg",".jpeg",".png",".tif", ".svg", ".psd"]
code = [".py",".c",".dart",".html",".css",".js"]

# clean = Organize(docs, "Docs")
clean = Organize(images, "Images")

print(*os.listdir(clean.cwd()), '\n')
clean.renameFiles()
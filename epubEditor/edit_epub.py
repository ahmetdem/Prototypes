import os, shutil, glob
from zipfile import ZipFile

#Change Epub to zip
epubDir = input("Enter the path: ")
epubName = list(epubDir.split('\\'))[-1]

newName = epubDir.replace(".epub", ".zip")

os.rename(epubDir, newName)

#Extract The zip
folderName = epubName.replace(".epub", "") # folderName == Coral of the Moon, THe folder we want to extract
zipPath = epubDir.replace(".epub", "")

with ZipFile(epubDir.replace(".epub", ".zip"), 'r') as zObject:
    zObject.extractall(
        path = zipPath
    )

# Find the styles
files = glob.glob(
    pathname = zipPath + '\**\*.css', 
    recursive = True
)

for file in files:
    if "style" in file.split("\\")[-1] or "Style" in file.split("\\")[-1]:
        cssFile = file

cssFileName = cssFile.split("\\")[-1]

#change the former style with the new one
os.remove(cssFile)

shutil.copy('stylesheet.css',
            cssFile)
n = shutil.make_archive(folderName, "zip", zipPath)

os.rename(n, epubDir)
os.remove(newName)

os.startfile(epubDir)


import os
import shutil

def main():

    src = r'C:\Users\ahmet\Documents\GitHub\python-projects\bleach\bleachEpub'
    root_dir, tail = os.path.split(src)


    if not os.path.isfile("bleach.epub"):

        fileName = shutil.make_archive("bleach", "zip", src)
        base = os.path.splitext(fileName)[0]

        target = base + '.epub'
        os.rename(fileName, target)

    else: 
        os.remove("bleach.epub")

        fileName = shutil.make_archive("bleach", 'zip', src)
        base = os.path.splitext(fileName)[0]

        target = base + '.epub'

        os.rename(fileName, target)


    os.startfile(r'C:\Users\ahmet\Documents\GitHub\python-projects\bleach\bleach.epub')


if __name__ ==  "__main__":
    main()
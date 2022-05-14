notice = """
   Save selected image region Demo
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""

from Python_BMP.BITMAPlib import(
        loadBMP,
        copyrect,
        convertselection2BMP,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(rootdir + '/assets/earth.bmp') #load earth to memory
        buff = copyrect(bmp, 7, 7, 61, 61) # copy rectagular region (x1,y1,x2,y2) uint to buff
        nbmp = convertselection2BMP(buff)# convert buffer to bitmap
        file = 'HelloSaveSelection.bmp' #file name
        saveBMP(file, nbmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()


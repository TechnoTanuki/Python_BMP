notice = """
 Hello Vertical Brightness Gradient
 in a circular region Demo
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
        vertbrightnessgrad2circregion,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(rootdir + '/assets/somebody.bmp')
        r = 110
        vertbrightnessgrad2circregion(
                bmp, # unsigned byte array
                10 + r, # int x
                5 + r, # int y
                r, # int radius r
                [-80, 150]) # the brightness gradient
        file = 'HelloVertBrightGradCircReg.bmp' #file name
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()





notice = """
  Hello World Vertical Italic Font
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
        newBMP,
        plotitalicstringvertical,
        getcolorname2RGBdict,
        font8x14,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx, my = 90, 1300 # bitmap size
        bmp = newBMP(mx,my,24) # RGB bitmap
        plotitalicstringvertical(bmp,
                40, 0, # position the text
                'Hello World!!', # random text
                7, # uint font size multiplier
                1, # uint space between pixels
                0, # uint default space between char
                getcolorname2RGBdict()['yellow'],
                font8x14)
        file = 'HelloWorlditalicvert.bmp' #file name
        saveBMP(file,bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()

notice = """
   Hello sideways text Earth Demo
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
        getcolorname2RGBdict,
        plotstringsideway,
        font8x14,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(rootdir + '/assets/earth.bmp') # load earth to memory wow.., it fits
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        x = y = 150
        fontsize =2
        pixspace = 1 # space between bitmap font pixels (0 = default)
        charspace = 0 # space bitmap font characters (0 = default)
        plotstringsideway(bmp, x, y,
                'Hello!!!',
                fontsize, pixspace, charspace,
                c['brightyellow'], font8x14)
        file = 'HelloEarthSidewayText.bmp' #file name
        saveBMP(file,bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()



notice = """
 Adjust the brightness of an image
 by %i percent brighter Demo
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
        brightnesseadjto24bitimage,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        peradj = 75
        print(notice % (peradj))
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(rootdir + '/assets/tanuki.bmp') #load to memory
        brightnesseadjto24bitimage(bmp,peradj) # 2nd param brightness adj percent + or -
        file='HelloBrightnessAdj.bmp' # file name <string>
        saveBMP(file, bmp) #dump the bytearray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()

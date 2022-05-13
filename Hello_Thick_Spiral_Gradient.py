notice = """
  Hello Thick Spiral Gradient Demo
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
        gradvert,
        bsplinevert,
        spiralcontrolpointsvert,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 300 #bitmap size
        bmp = newBMP(mx, my, 24)
        gradvert(bmp,
                bsplinevert(
                        spiralcontrolpointsvert(
                                150, 150, 7, 1, 10),
                        False, False),
                5, [255, 0], [.9, .5, .9])
        file = 'HelloThickGradSpiral.bmp' # random file name
        saveBMP(file, bmp) # dump the byterray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()




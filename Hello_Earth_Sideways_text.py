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

from pythonbmp.BITMAPlib import(
        loadBMP as l,
        getcolorname2RGBdict,
        plotstringsideway as f,
        font8x14,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(l)}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = l(f'{rootdir}/assets/earth.bmp') # call loadBMP
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = l(f'{rootdir}/assets/earth.bmp')
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        x = y = 150
        fontsize = 2
        pixspace = 1 # space between bitmap font pixels (0 = default)
        charspace = 0 # space bitmap font characters (0 = default)
        f(bmp, x, y, 'Hello!!!', # call plotstringsideway
          fontsize, pixspace, charspace,
          c['brightyellow'], font8x14)
        file = f'Hello{l.__name__}{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



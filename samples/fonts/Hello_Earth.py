notice = """
   Hello Earth Demo (Text on image)
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
        loadBMP as f,
        getcolorname2RGBdict,
        plotstring,
        font8x14,
        font8x8,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = f(f'{rootdir}/../assets/earth.bmp')
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        fontsize = 4 # font size
        pixspace = 1 # space between bitmap font pixels (0 = default)
        charspace = 1 # space bitmap font characters (0 = default)
        plotstring(bmp, 5, 25, 'Hello',
                fontsize, pixspace, charspace,
                c['brightyellow'], font8x14)
        plotstring(bmp, 5, 85, 'Earth',
                fontsize, pixspace, charspace,
                c['brightwhite'],font8x8)
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

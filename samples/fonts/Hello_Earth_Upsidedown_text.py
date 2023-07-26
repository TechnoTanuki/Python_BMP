notice = """
Hello Earth with upsidedown text Demo
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
        plotstring as f,
        plotstringupsidedown as p,
        font8x14,
        font8x8,
        getcolorname2RGBdict,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(l)}\n{meta(f)}\n{meta(p)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = l(f'{rootdir}/../assets/earth.bmp')# call loadBMP
        c = getcolorname2RGBdict() #friendly color names 2 rgb
        fontsize = 4 # font size
        pixspace = 1 # space between bitmap font pixels (0 = default)
        charspace = 0 # space bitmap font characters (0 = default)
        f(bmp, 5, 25, 'Hello', fontsize,
          pixspace, charspace,
          c['brightred'], font8x14) # call plotstring
        p(bmp, 5, 85, 'World', fontsize,
          pixspace, charspace,
          c['brightyellow'], font8x8) # call plottringupsidedown
        file = f'Hello{l.__name__}{f.__name__}{p.__name__}.bmp' #file name
        saveBMP(file, bmp)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()




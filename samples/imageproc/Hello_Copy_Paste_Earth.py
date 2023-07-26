notice = """
   Hello Earth Copy and Paste Demo
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
        loadBMP,
        copyrect as c,
        pasterect as p,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(c)}\n{meta(p)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/../assets/earth.bmp')
        buf = c(bmp, 3, 3, 60, 60) # copy a rectangular region (x1,y1,x2,y2) to a buffer
        p(bmp, buf, 40, 40) # paste buffer to a rectangular region at (x1,y1)
        file = f'HelloEarth{c.__name__}{p.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



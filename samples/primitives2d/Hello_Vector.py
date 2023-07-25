notice = """
      Hello Vector (arrow) Demo
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
        newBMP,
        drawvec as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 200 # bitmap size
        bmp = newBMP(mx, my, 1) # 1 bit or mono
        p1 = (7, 7) # (x,y) point 1 or origin
        p2 = [mx - 7, my - 7] # (x,y) point 2 or where the vector points
        arrowhead = 0 # 0=auto other value will set length
        color = 1
        f(bmp, p1, p2, arrowhead, color, 5)
        file = f'Hello{f.__name__}.bmp' # file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

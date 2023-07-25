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

from pythonbmp.BITMAPlib import(
        newBMP,
        gradvert as g,
        bsplinevert as b,
        spiralcontrolpointsvert as s,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(g)}\n{meta(b)}\n{meta(s)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 300 #bitmap size
        bmp = newBMP(mx, my, 24)
        g(bmp, b(s(150, 150, 7, 1, 10),
          False, False), 5, [255, 0],
          [.9, .5, .9])
        file = f'Hello{g.__name__}{b.__name__}{s.__name__}.bmp' # random file name
        saveBMP(file, bmp) # dump the byterray to disk
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()




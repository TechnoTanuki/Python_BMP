notice = """
Gamma Adjust Rectangular Region Demo
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
        gammaadjto24bitregion as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = loadBMP(f'{rootdir}/../assets/earth.bmp')
        #gammaadjto24bitregion(bmp,x1,y1,x2,y2,gammadj <ufloat>)
        f(bmp, 30, 30, 138, 138, 4) # gamma adjustment
        f(bmp, 50, 50, 118, 118, 0.1)
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # bmp<byte array in bitmap format> --> file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



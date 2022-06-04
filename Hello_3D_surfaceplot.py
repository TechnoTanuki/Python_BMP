notice = """
     Hello 3D Surface Plot Demo
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
from math import sin, cos, pi
from Python_BMP.BITMAPlib import(
        centercoord,
        getRGBfactors,
        newBMP,
        plot3Dsolid,
        rotvec3D,
        saveBMP,
        surfplot3Dvertandsurface as f,
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames[0:6]}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 500
        file = f'Hello{fname}.bmp'
        bmp = newBMP(mx, my, 24)
        cenpt = centercoord(bmp) # bitmap dependent coords
        cf = getRGBfactors() # color info
        d = 200 # distance of the observer
        tvect = [0, 0, 100] #3D translation vector
        _2pi = 2 * pi
        fnxy = lambda x, y: sin(x / 50 * _2pi ) * 4 + \
                            cos(y / 50 * _2pi ) * 4
        plot3Dsolid(bmp,
                f(-50, -50, 50, 50, 5, fnxy),
                True, cf['brightcyan'],
                True, 0, rotvec3D(30, 27, 30),
                tvect, d, cenpt)

        saveBMP(file, bmp) # dump bytes to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()




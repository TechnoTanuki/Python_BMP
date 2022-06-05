notice = """
            Benzene Demo
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
        centercoord,
        gradvert as f,
        regpolygonvert,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 250 #bitmap size
        bmp = newBMP(mx, my, 24) # 24 bit BMP
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = 80 # radius of circle that circumscribes the regular polygon
        sides = 6 # we want a hexagon
        lumrange = (255, 0) # lum intensity decrease from center (byte,byte) unsigned
        rgbfactors = (.4, .7, .3) # color as unsigned tuple of (r,g,b) -> min 0 max 1
        angle = 0 # angle of rotation of regular polygon in degrees
        polyvertlist = regpolygonvert(x, y, r, sides, angle) # generate polygon vertices
        atomrad = 55 # make radius of carbon atoms 55 pixels
        f(bmp, polyvertlist, atomrad,
          lumrange, rgbfactors) # call gradvert
        file = f'Hello{f.__name__}.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



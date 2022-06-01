notice = """
 Gradient Thick Regular Polygon Demo
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
        regpolygonvert,
        gradthickplotpoly,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my= 400 # bitmap size
        bmp =  newBMP(mx, my ,24) # RGB bitmap black background
        (x, y) = centercoord(bmp) # How to get center of the bitmap
        r = x - 20 # radius of a circle that contains all the vertices
        sides = 5 # for a pentagon
        angle = 30 # for rotation in degrees
        penradius = 15 # radius of pen
        lumrange = (0, 255) # increasing luminosity from center of pen
        rgbfactors = (.7, .5, .6) # rgb values from 0 to 1 ufloat
        polygonvertexlist = regpolygonvert(x, y, r, sides, angle) # generate vertices
        gradthickplotpoly(bmp, polygonvertexlist, penradius,
                lumrange, rgbfactors)  # plot the polygon
        file='HelloThickGradientRegularPolygon.bmp' # file name
        saveBMP(file, bmp) # save the bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

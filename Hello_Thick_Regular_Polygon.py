notice = """
  Hello Thick Regular Polygon Demo
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
        regpolygonvert,
        thickplotpoly,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 200 # bitmap size
        bmp =  newBMP(mx, my, 4) # 2^4=16 color bitmap black background
        x = y = mx // 2 # centerpoint
        r = x - 20 # radius of a circle that contains all the vertices
        sides = 5 # for a pentagon
        angle = 30 # for rotation in degrees
        polygonvertexlist = \
                regpolygonvert(x, y, r, sides, angle) # generate vertices
        color = 11 # color in 4 bit mode (min 0 - max 15)
        penradius = 5 # radius of pen
        thickplotpoly(bmp, polygonvertexlist, penradius, color)  # plot the polygon
        file = 'HelloThickRegularPolygon.bmp' # file name
        saveBMP(file, bmp) # save the bitmap
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()





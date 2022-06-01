notice = """
Thick Exponential Spiral Gradient Demo
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
        gradvert,
        spiralcontrolpointsvert,
        bsplinevert,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = newBMP(300, 300, 24) # RGB bitmap 300 x 300
        (x,y) = centercoord(bmp) # How to get center of the bitmap
        step = 7 # growth increment of spiral
        growthfactor = 1.61803399 # Golden Ratio...
        turns = 5 # number of turns of the spiral
        vertlist = \
                spiralcontrolpointsvert(x, y,
                        step,
                        growthfactor,
                        turns) # compute points of control points
        isclosed = False # closed or open curve
        curveback = False # do extra compute to trace back to origin
        pts = bsplinevert(vertlist, isclosed, curveback) # compute points of bspline 
        penradius = 5 # radius of pen in pixel
        lumrange = (255, 0) # brightness decrease from center of pen to edge <ubytes>
        rgbfactors = (.9, .5, .9) # color as (r,g,b) values between 1 and 0 <ufloat>
        gradvert(bmp, pts, penradius,
                lumrange, rgbfactors) # render the spiral
        file = 'HelloThickExpGradSpiral.bmp' #file name
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

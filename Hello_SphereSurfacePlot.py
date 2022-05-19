notice = """
  Hello  Sphere Surface Plot Demo
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

from random import randint
from math import sin, cos

from Python_BMP.BITMAPlib import(
        newBMP,
        spherevertandsurfaceplot,
        centercoord,
        plot3Dsolid,
        rotvec3D,
        getX11RGBfactors,
        getX11colorname2RGBdict,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 320 # x=y square bmp
        file = 'HelloSphereSurfplot.bmp' # some random file name as string
        bmp = newBMP(mx, my, 24) # 16 color bmp
        f = lambda lat, lon:  sin(lon)
        x11cf = getX11RGBfactors()
        x11c = getX11colorname2RGBdict()
        plot3Dsolid(bmp,
                spherevertandsurfaceplot(
                    [0, 0, 0], 50, 10, f),
                True, # toggle solid
                x11cf['darkolivegreen1'], # color of solid
                False, # toggle outline
                x11c['darkolivegreen3'], # outline color
                rotvec3D(70, 7, 20), # rotation vector (x,y,z) in degrees
                [0, 0, 200], # 3D translation vector
                400, # distance of screen from observer
                centercoord(bmp) # 2D screen positioning
                )
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(imgedt + ' ' + file) # load image in editor

if __name__=="__main__":
        main()

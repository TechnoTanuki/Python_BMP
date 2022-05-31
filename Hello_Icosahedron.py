notice = """
         Icosahedron Demo
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
        getRGBfactors,
        rotvec3D,
        plot3Dsolid,
        icosahedvertandsurface,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 250 # x=y square bmp
        file = 'HelloIcosahedron.bmp' # some random file name as string
        bmp = newBMP(mx, my, 24) # RGB bmp
        cf = getRGBfactors() # color info with presets
        plot3Dsolid(bmp,
                icosahedvertandsurface(40), # parameter is radius of sphere that holds the solid
                True, # toggle solid render
                cf['brightwhite'], # color of solid
                False, # toggle outline display
                0, # outline color
                rotvec3D(70, 7, 20), # rotation vector (x,y,z) in degrees
                [0, 0, 200], # 3D translation vector
                400, # distance of the observer the to 2D projection
                centercoord(bmp))
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()



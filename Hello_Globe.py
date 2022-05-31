notice = """
          Hello Globe Demo
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
        spherevertandsurface,
        centercoord,
        plot3Dsolid,
        rotvec3D,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 320 # x=y square bmp
        file = 'HelloGlobe.bmp' # some random file name as string
        bmp = newBMP(mx, my, 4) # 16 color bmp
        plot3Dsolid(bmp,
                spherevertandsurface([0, 0, 0], 50, 15),
                False, # toggle solid
                0, # color of solid
                True, # toggle outline
                10, # outline color
                rotvec3D(70, 7, 20), # rotation vector (x,y,z) in degrees
                [0, 0, 200], # 3D translation vector
                400, # distance of screen from observer
                centercoord(bmp) # 2D screen positioning
                )
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()

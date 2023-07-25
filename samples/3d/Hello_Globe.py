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

from pythonbmp.BITMAPlib import(
        newBMP,
        spherevertandsurface as f,
        centercoord,
        plot3Dsolid,
        rotvec3D,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 320 # x=y square bmp
        file = f'Hello{f.__name__}1.bmp' # some random file name as string
        bmp = newBMP(mx, my, 4) # 16 color bmp
        plot3Dsolid(bmp,
                f([0, 0, 0], 50, 15),
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
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

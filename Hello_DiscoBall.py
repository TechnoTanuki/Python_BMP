notice = """
         3D disco ball demo
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
        centercoord,
        getRGBfactors,
        rotvec3D,
        plot3Dsolid,
        spherevertandsurface as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 250 # x = y square bmp
        file = f'Hello{f.__name__}.bmp' # some random file name as string
        bmp = newBMP(mx, my, 24) # RGB bmp
        cenpt = centercoord(bmp) # helper method to get center of a bitmap
        cf = getRGBfactors() # color info with presets
        d, translationvector = 400, [0, 0, 200] # be careful with these variables or object goes offscreen
        isSolid = True # toggle solid or outline
        showoutline = False # can show outline even if solid
        color = cf['brightwhite'] # color of solid
        outlinecolor = 10 # outline color
        rotation = rotvec3D(70, 70, 20) # rotation vector (x,y,z) in degrees
        plot3Dsolid(bmp, f([0, 0, 0], 50, 15),
                isSolid, color,
                showoutline, outlinecolor,
                rotation,
                translationvector, d,
                cenpt)
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
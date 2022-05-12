notice = """
            3D Coin Demo
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
        cylindervertandsurface,
        plot3Dsolid,
        saveBMP
        )

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my =250 # x=y square bmp
        file = 'HelloCoin.bmp' # some random file name as string
        bmp = newBMP(mx, my, 24) # RGB bmp
        cenpt = centercoord(bmp) # helper method to get center of a bitmap
        cf = getRGBfactors() # color info with presets
        d, translationvector=400, [0, 0, 200] # be careful with these variables or object goes offscreen
        isSolid = True # toggle solid or outline
        showoutline = True # can show outline even if solid
        cf = getRGBfactors() # color list
        color = cf['brightyellow'] # color of solid
        outlinecolor = 0 # outline color
        rotation = rotvec3D(25, 30, 40) # rotation vector (x,y,z) in degrees
        vcen = (1, 0, 0) # x y z coords
        r = 40 # radius of cylinder
        zlen = 10 # height of cylinder
        deganglestep = 5 # how finely we tile flat surfaces around the cylinder
        obj3D = cylindervertandsurface(vcen, r, zlen, deganglestep)# A solid is defined by vertices and surfaces
        plot3Dsolid(bmp, obj3D,
                isSolid, color,
                showoutline, outlinecolor,
                rotation, translationvector,
                d, cenpt)
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret =proc.call(imgedt + ' ' + file) # replace with another editor if Unix

if __name__=="__main__":
        main()

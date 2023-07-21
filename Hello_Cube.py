notice = """
             Cube Demo
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
        getX11RGBfactors,
        getshapesidedict,
        plot3Dsolid,
        rotvec3D,
        cubevert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my = 250 # x = y square bmp
        file = f'Hello{f.__name__}.bmp' # some random file name as string
        bmp = newBMP(mx, my, 24) # RGB bmp
        cenpt = centercoord(bmp) # helper method to get center of a bitmap
        d, translationvector = 400, [0, 0, 200] # be careful with these variables or object goes offscreen
        isSolid = True # toggle solid or outline
        showoutline = False # can show outline even if solid
        cf = getX11RGBfactors() # color list
        color = cf['teal'] # color of solid
        outlinecolor = 10 # outline color
        sd = getshapesidedict() # common shape dict for surface definitions
        rotation = rotvec3D(40, 80, 50) # rotation vector (x,y,z) in degrees
        plot3Dsolid(bmp, [f(40), sd["cube"]],
                isSolid, color,
                showoutline, outlinecolor,
                rotation, translationvector,
                d, cenpt)
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

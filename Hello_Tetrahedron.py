notice = """
          Tetrahedron Demo
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
        getshapesidedict,
        tetrahedravert as f,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 250 # x=y square bmp
        file = f'Hello{f.__name__}.bmp' # some random file name as string
        bmp = newBMP(mx, my, 24) # RGB bmp
        cenpt = centercoord(bmp) # helper method to get center of a bitmap
        cf = getRGBfactors() # color info with presets
        d, translationvector= 400, [0, 0, 200] # be careful with these variables or object goes offscreen
        isSolid = True # toggle solid or outline
        showoutline = False # can show outline even if solid
        cf = getRGBfactors() # color list
        color = cf['brightred'] # color of solid
        outlinecolor = 10 # outline color
        sd = getshapesidedict() # common shape dict for surface definitions
        rotation = rotvec3D(45, 60, 15) # rotation vector (x,y,z) in degrees
        vertices = f(60) # get tetrahedra vetices
        surfaces = sd["tetrahedra"] # get tetrahedra surfaces
        obj3D = [vertices, surfaces] # A solid is defined by vertices and surfaces
        plot3Dsolid(bmp, obj3D, isSolid, color,
                showoutline, outlinecolor,
                rotation, translationvector,
                d, cenpt)
        saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()
notice = """
           Octahedra Demo
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
        getshapesidedict,
        plot3Dsolid,
        octahedravert as f,
        rotvec3D,
        getfuncmetastr as meta,
        saveBMP
        )

import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        file = f'Hello{f.__name__}.bmp' # some random file name as string
        mx = my = 300 # bitmap dimensions
        bmp = newBMP(mx, my, 24) # RGB bmp
        cenpt = centercoord(bmp) # helper method to get center of a bitmap
        cf = getRGBfactors() # color info with presets
        d, translationvector = 400, [-10, 0, 200] # be careful with these variables or object goes offscreen
        isSolid = True # toggle solid or outline
        showoutline = False # can show outline even if solid
        cf = getRGBfactors() # color list
        color = cf['brightyellow'] # color of solid
        outlinecolor = 0 # outline color
        sd = getshapesidedict() # common shape dict for surface definitions
        rotation = rotvec3D(60, 60, 30) # rotation vector (x,y,z) in degrees
        vertices = f(50) # get octahedra vertices
        surfaces = sd["octahedra"] # get octahedra surfaces
        obj3D = [vertices, surfaces] # A solid is defined by vertices and surfaces
        plot3Dsolid(bmp, obj3D, isSolid, color,
                showoutline, outlinecolor,
                rotation, translationvector, d, cenpt)
        saveBMP(file, bmp) # dump byte array to file system as-is
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

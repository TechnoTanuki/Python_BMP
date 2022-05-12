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
import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = my = 250 # x=y square bmp
        file = 'HelloDiscoBall.bmp' # some random file name as string
        bmp = b.newBMP(mx,my,24) # RGB bmp
        cenpt = b.centercoord(bmp) # helper method to get center of a bitmap
        cf = b.getRGBfactors() # color info with presets
        d, translationvector= 400, [0,0,200] # be careful with these variables or object goes offscreen
        isSolid = True # toggle solid or outline
        showoutline = False # can show outline even if solid
        cf = b.getRGBfactors() # color list
        color = cf['brightwhite'] # color of solid
        outlinecolor = 10 # outline color
        rotation = b.rotvec3D(70, 70, 20) # rotation vector (x,y,z) in degrees
        b.plot3Dsolid(bmp,
                b.spherevertandsurface([0, 0, 0],
                50, 15),
                isSolid, color,
                showoutline, outlinecolor,
                rotation,
                translationvector, d,
                cenpt)
        b.saveBMP(file, bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt))
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__":
        main()

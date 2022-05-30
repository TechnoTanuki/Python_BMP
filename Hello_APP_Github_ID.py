notice = """
        Hello Github ID Demo
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
from math import sin, cos, pi
from Python_BMP.BITMAPlib import(
        centercoord,
        getX11RGBfactors,
        getX11colorname2RGBdict,
        newBMP,
        plot3Dsolid,
        plotstring,
        font8x14,
        rotvec3D,
        sphere,
        fern,
        fillbackgroundwithgrad,
        surfplot3Dvertandsurface,
        icosahedvertandsurface,
        getdefaultlumrange,
        saveBMP,
        )

import subprocess as proc
from os import path


def main():
        file = 'Hello_GithubID.bmp'
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        bmp = newBMP(1280, 640, 24)
        [cx, cy] = centercoord(bmp) # bitmap dependent coords
        cf = getX11RGBfactors() # color info
        c = getX11colorname2RGBdict()
        lum = getdefaultlumrange()

        d = 200 # distance of the observer
        tvect = [0, 0, 100] #3D translation vector

        fontsize = 6 # font size
        pixspace = 1 # space between bitmap font pixels (0 = default)
        charspace = 1 # space bitmap font characters (0 = default)
        sx = 120
        sy = 80

        fillbackgroundwithgrad(bmp,
                lum['maxasc'], cf['cornflowerblue'], 0)

        plotstring(bmp, sx, sy + 60,
        'Pure Python Bitmap',
                fontsize, pixspace, charspace,
                c['red'], font8x14)

        plotstring(bmp, sx, sy + 120,
        '2D and 3D Graphics',
                fontsize, pixspace, charspace,
                c['green'], font8x14)

        plotstring(bmp, sx, sy + 180,
        'Library',
                fontsize, pixspace, charspace,
                c['blue'], font8x14)


        _2pi = 2 * pi
        _f = 50
        fnxy = lambda x, y: sin(x / _f * _2pi ) * 4 + \
                            cos(y / _f * _2pi ) * 4
        plot3Dsolid(bmp,
                surfplot3Dvertandsurface (
                -50, -50, 50, 50, 5, fnxy),
                  True, cf['gold'],
                  True, c['gold'], rotvec3D(0, -35, 45),
                  tvect, d, [cx + 50, cy + sy])

        plot3Dsolid(bmp,
                icosahedvertandsurface(80), # parameter is radius of sphere that holds the solid
                True, # toggle solid render
                cf['greenyellow'], # color of solid
                False, # toggle outline display
                0, # outline color
                rotvec3D(70, 7, 20), # rotation vector (x,y,z) in degrees
                [0, 0, 200], # 3D translation vector
                d, # distance of the observer the to 2D projection
                (cx - 100, cy + sy))

        sphere(bmp, 280, cy + 100, 80, cf['royalblue'])
        fern(bmp, 940, 100, 1190, 570, c['darkolivegreen3'])

        saveBMP(file,bmp) # dump bytes to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()




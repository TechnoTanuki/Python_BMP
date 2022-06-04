notice = """
          Hello 3D Demo
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
        addvect,
        bottomrightcoord,
        centercoord,
        conevertandsurface,
        cubevert,
        cylindervertandsurface,
        decahedvertandsurface,
        getcolorname2RGBdict,
        getRGBfactors,
        getshapesidedict,
        hexahedravert,
        icosahedvertandsurface,
        newBMP,
        octahedravert,
        plot3Dsolid as f,
        RGB2int,
        rotvec3D,
        saveBMP,
         spherevertandsurface,
        surfplot3Dvertandsurface,
        tetrahedravert,
        trans
        )

import subprocess as proc
from os import path


def main():
        print(notice)
        fname = f.__name__
        print(f'def {fname}{f.__code__.co_varnames}\n\t{f.__doc__}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) # get path of this script
        mx = 1024
        my = 768
        file = f'Hello{fname}.bmp'
        bmp = newBMP(mx, my, 24)
        maxpt = bottomrightcoord(bmp)
        cenpt = centercoord(bmp) # bitmap dependent coords
        c = getcolorname2RGBdict()
        cf = getRGBfactors() # color info
        d = 200 #
        tvect = [0,0,100] # be careful with these variables or object goes offscreen
        sd = getshapesidedict() # shape dictonary
        pts = tetrahedravert(80) # get points in 3D space that forms a tetrahedron
        # or  the object goes offscreen
        d = 200 # distance of the observer
        tvect = [0, 0, 100] #3D translation vector

        shapes = [[[trans(cubevert(30), pts[3]),
                  sd["cube"]],
                  cf["darkblue"], True, c['black']],
                [[trans(tetrahedravert(30), pts[2]),
                  sd["tetrahedra"]],
                  cf["darkred"], True, c['white']],
                [[trans(octahedravert(20), pts[1]),
                  sd["octahedra"]],
                  cf["yellow"], True, c['darkgray']],
                [[trans(hexahedravert(30), pts[0]),
                  sd["hexahedra"]],
                  cf["darkgreen"], True, c['darkgreen']]]
        for s in shapes:
                f(bmp, s[0], True, s[1], s[2], s[3],
                  rotvec3D(10, 5, 5), tvect, d,
                  addvect(cenpt, [-160, -10]))
        f(bmp, decahedvertandsurface(25),
          True, cf['brightred'], False,
          0, rotvec3D(7, 77, 20),
          tvect, d, addvect(cenpt, [280, -250]))
        f(bmp, icosahedvertandsurface(25),
          True, cf['brightwhite'], False,
          0, rotvec3D(70, 7, 20),
          tvect, d, addvect(cenpt, [+60, -130]))
        f(bmp, spherevertandsurface([5, 0, 0], 60, 10),
          True, cf['brightwhite'], False,
          0, rotvec3D(190, 145, 70),
          tvect, d, addvect(cenpt, [300, -50]))
        f(bmp, cylindervertandsurface([1,0,0], 20, 10, 5),
          True, cf['brightyellow'], True,
          RGB2int(20,20,0), rotvec3D(60, 74, 72),
          tvect, d, addvect(cenpt,[-200, -50]))
        f(bmp, conevertandsurface([1, 0, 0], 20, 15, 5),
          True, cf['brightorange'],
          False, RGB2int(20,20,0),
          rotvec3D(6,67,2),
          tvect, d, addvect(cenpt, [-300, -150]))
        fnxy = lambda x, y: x | y
        f(bmp, surfplot3Dvertandsurface(-15, -35, 35, 35, 5, fnxy),
          True, cf['brightcyan'],
          True, 0, rotvec3D(20, 67, 30),
          tvect, d, addvect(cenpt, [-420, -25]))

        saveBMP(file,bmp) # dump bytes to file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user we are done
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()




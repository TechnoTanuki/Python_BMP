notice = """
 Feature and speed test
 for a Pure Python graphics library
 that saves to a bitmap

 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|       The primary author and any  |
| any subsequent code contributors  |
| shall not be liable in any event  |
| for  incidental or consequential  |
| damages  in connection with,  or  |
| arising out from the use of this  |
| code in current form or with any  |
| modifications.                    |
|-----------------------------------|
|   Contact primary author          |
|   if you plan to use this         |
|   in a commercial product at      |
|   joelalcarez1975@gmail.com       |
|-----------------------------------|
|   Educational or hobby use is     |
|   highly encouraged...            |
|   have fun coding !               |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""
from Python_BMP.BITMAPlib import(
        addvect,
        adjustcolordicttopal,
        beziercurve,
        bottomrightcoord,
        bspline,
        bsplinevert,
        centercoord,
        conevertandsurface,
        convertselection2BMP,
        copyrect,
        cubevert,
        cylindervertandsurface,
        decahedvertandsurface,
        drawvec,
        fillbackgroundwithgrad,
        filledgradrect,
        filledrect,
        font8x14,
        font8x8,
        getcolorname2RGBdict,
        getdefaultlumrange,
        getIFSparams,
        getRGBfactors,
        getshapesidedict,
        gradcircle,
        gradellipse,
        gradthickcircle,
        gradthickellipserot,
        gradthickroundline,
        gradvert,
        hexahedravert,
        icosahedvertandsurface,
        IFS,
        loadBMP,
        mandelbrot,
        mandelparamdict,
        newBMP,
        octahedravert,
        pasterect,
        piechart,
        plot3Dsolid,
        plot8bitpatternastext,
        plotbmpastext,
        plotfilledflower,
        plotlines,
        plotpoly,
        plotreversestring,
        plotstring,
        plotstringsideway,
        plotstringupsidedown,
        plotstringvertical,
        rectangle,
        regpolygonvert,
        RGB2int,
        rotvec3D,
        saveBMP,
        spherevertandsurface,
        spiralcontrolpointsvert,
        surfplot3Dvertandsurface,
        tetrahedravert,
        trans,
        XYaxis,
        XYscatterplot
        )

import subprocess as proc
from time import(
        process_time_ns as _time_ns
        )

from random import randint
from os import path

def elaspedtimeinseconds(inittime):
        return (_time_ns() - inittime) / 1000000000

def hhmmsselaspedtime(inittime):
        secs, ns = \
                divmod((_time_ns() - inittime), 1000000000)
        mins, secs = divmod(secs, 60)
        hrs, mins = divmod(mins, 60)
        return str(hrs).zfill(2) + ':' \
             + str(mins).zfill(2) + ':' \
             + str(secs).zfill(2) + '.' + str(ns)

def main():
        rootdir = path.dirname(__file__)
        plotbmpastext(loadBMP(rootdir + '/assets/pp.bmp')) #load logo
        print(notice)

        demostart = _time_ns()
        starttime = _time_ns()
        mx = 1024
        my = 768
        bmp = newBMP(mx, my, 24)
        print('New bitmap in ' + hhmmsselaspedtime(starttime))
        maxpt = bottomrightcoord(bmp)
        cenpt = centercoord(bmp) #bitmap dependent coords
        c = getcolorname2RGBdict()
        cf = getRGBfactors()
        lum = getdefaultlumrange() #color info
        adjustcolordicttopal(bmp, c)
        starttime = _time_ns()
        fillbackgroundwithgrad(bmp,
                lum['maxasc'], cf['blue'], 0)
        print('Background gradient test done in ',
                hhmmsselaspedtime(starttime))
        starttime = _time_ns()
        rectangle(bmp, 1, 1,
                  maxpt[0] - 1,
                  maxpt[1] - 1,
                  c['white'])
        filledgradrect(bmp,
                395, 5, 955, 41,
                lum['upperdesc'],
                cf['orange'], 1)
        filledrect(bmp,
                395, 44, 955, 55,
                c['darkblue'])
        print('Rectangle tests done in ',
                hhmmsselaspedtime(starttime))
        starttime = _time_ns()
        hc = spiralcontrolpointsvert(
                350, 180, 5, 1.1, 5)#we will use this later to make smooth spiral
        gradthickroundline(bmp,
                [800, 620], # end point 1
                [800, 600], # end point 2
                7, # thickness
                lum['upperdesc'], # how bright the gradient
                cf['darkred']) # color of the gradient
        plotlines(bmp, hc, c['yellow'])
        cp = [50, 150]#all arrows must point outward from cp or bug report please

        drawvec(bmp, cp, [50, 100], 0, c['white'])#color dict more readable than color int
        drawvec(bmp, cp, [100, 150], 0, c['green'])#but if you want to use color int
        drawvec(bmp, cp, [50, 200], 0, c['red'])#the functions will work too
        drawvec(bmp, cp, [5, 150], 0, c['blue'])#up to the color supported
        drawvec(bmp, cp, [75, 175], 0, c['yellow'])# by the loaded bitmap file
        drawvec(bmp, cp, [25, 125], 0, c['magenta'])
        drawvec(bmp, cp, [25, 175], 0, c['orange'])
        drawvec(bmp, cp, [75, 125], 0, c['gray'])
        print('Line tests done in ',
        hhmmsselaspedtime(starttime))
        starttime = _time_ns()
        fnt = font8x8
        strtest = 'abcdefghijklmnopqrstuvwxyz\n0123456789\'":;.,?!~`@#$%^&()[]{}_*+-/=<>\nABCDEFGHIJKLMNOPQRSTUVWXYZ'
        plotstring(bmp, 400, 10,
                'My Python GL test',
                 4, 1, 0, c['lightgray'],
                 fnt)
        plotstring(bmp, 400, 45,
                'Copyright 2021 by Joel C. Alcarez (joelalcarez1975@gmail.com)',1,1,0,c['brightwhite'],fnt)
        plotstring(bmp, 300, 64,
                strtest, 1, 0, 0,
                c['brightgreen'],
                fnt)
        plotstringupsidedown(bmp,
                10, 737,
                strtest, 1, 0, 0,
                c['brightgreen'],
                fnt)
        plotreversestring(bmp,
                300, 100,
                strtest, 1, 0, 0,
                c['brightgreen'],
                fnt)
        fnt = font8x14
        plotstringvertical(bmp,
                970, 30,
                'Matrix text',
                2, 0, 0, c['green'],
                fnt)
        plotstringsideway(bmp, 970, 730,
                strtest, 1, 0, 0,
                c['white'], fnt)
        print('Text tests done in ',
        hhmmsselaspedtime(starttime))

        starttime = _time_ns()

        #be careful with these variables
        # or  the object goes offscreen
        d = 200 # distance of the observer
                # from the screen
        tvect = [0, 0, 100] #3D translation vector

        sd = getshapesidedict()
        pts = tetrahedravert(80)
        shapes = [[[trans(cubevert(30),
                  pts[3]),
                  sd["cube"]],
                  cf["darkblue"], True,
                  c['black']],
                [[trans(tetrahedravert(30),
                  pts[2]),
                  sd["tetrahedra"]],
                  cf["darkred"], True,
                  c['white']],
                [[trans(octahedravert(20),
                  pts[1]),
                  sd["octahedra"]],
                  cf["yellow"], True,
                  c['darkgray']],
                [[trans(hexahedravert(30),
                  pts[0]),
                  sd["hexahedra"]],
                  cf["darkgreen"], True,
                  c['darkgreen']]]
        for s in shapes:
                plot3Dsolid(bmp,
                        s[0], True,
                        s[1], s[2], s[3],
                        rotvec3D(10, 5, 5),
                        tvect, d,
                        addvect(cenpt, [-160, -10]))
        plot3Dsolid(bmp,
                decahedvertandsurface(25),
                   True, cf['brightred'], False,
                   0, rotvec3D(7, 77, 20),
                   tvect, d, addvect(cenpt, [280, -250]))
        plot3Dsolid(bmp,
                icosahedvertandsurface(25),
                   True, cf['brightwhite'], False,
                   0, rotvec3D(70, 7, 20),
                   tvect, d, addvect(cenpt, [+60, -130]))
        plot3Dsolid(bmp,
                spherevertandsurface([5, 0, 0], 60, 10),
                True, cf['brightwhite'], False,
                0, rotvec3D(190, 145, 70),
                tvect, d, addvect(cenpt, [300, -50]))
        plot3Dsolid(bmp,
                cylindervertandsurface([1,0,0], 20, 10, 5),
                True, cf['brightyellow'], True,
                RGB2int(20,20,0), rotvec3D(60, 74, 72),
                tvect, d, addvect(cenpt,[-200, -50]))
        plot3Dsolid(bmp,
                conevertandsurface([1, 0, 0], 20, 15, 5),
                True, cf['brightorange'],
                False, RGB2int(20,20,0),
                rotvec3D(6,67,2),
                tvect, d, addvect(cenpt, [-300, -150]))
        fnxy = lambda x, y: x & y
        plot3Dsolid(bmp,
                surfplot3Dvertandsurface (
                -35, -35, 35, 35, 15, 5, fnxy),
                  True, cf['brightcyan'],
                  True, 0, rotvec3D(20, 67, 30),
                  tvect, d, addvect(cenpt, [-420, -25]))
        print('3D tests done in ',
                hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        mandelpar = mandelparamdict()
        mandelbrot(bmp, 10, 600, 130, 735,
                mandelpar['maxeqdim'],
                    cf['brightgreen'], 255)
        p = getIFSparams()#same here add more to this dict
        IFS(bmp, p['fern'],
                170, 600, 270, 730, 12, 12, 30, 30,
                c['lightgreen'], 10000)
        IFS(bmp, p['tree'],
                270, 600, 370, 730, 100, 100, 0, 0,
                c['brown'], 10000)
        IFS(bmp,p['cantortree'],
                370, 600, 450, 730, 100, 100, 0, 0,
                c['lightcyan'], 10000)
        IFS(bmp, p['sierpinskitriangle'],
                450, 600, 670, 730, 100, 100, 0, 0,
                c['cyan'], 10000)
        print('Fractal tests done in ',
        hhmmsselaspedtime(starttime))
        p = regpolygonvert(250, 80, 40, 6, 0)
        starttime = _time_ns()
        beziercurve(bmp, p, 3, c['brightorange'])
        beziercurve(bmp, hc, 0, c['lightred'])
        print('Bezier curve tests done in ',
        hhmmsselaspedtime(starttime) )

        starttime = _time_ns() #bspline follow control points better than bezier
        bspline(bmp, p, 0, c['red'], True, True)
        bspline(bmp, hc, 0, c['brightwhite'], True, True)
        gradvert(bmp,
                 bsplinevert(
                  spiralcontrolpointsvert(
                          165, 135, 7, 1.2, 3),
                  False,
                 False),
                 5,
                 lum['upperdesc'],
                 cf['brightwhite'])
        print('Bspline tests done in ',
         hhmmsselaspedtime(starttime) )

        starttime = _time_ns()
        gradcircle(bmp, 900, 140, 30,
                lum['maxdesc'], cf['brightyellow'])
        gradthickcircle(bmp, 900, 550, 40, 8,
                lum['upperdesc'], cf['lightred'])
        print('Circle tests done in ',
         hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        gradellipse(bmp, 750, 550, 20, 40,
                lum['upperdesc'], cf['brightorange'])
        gradthickellipserot(bmp, 790, 700, 50, 30, 45, 5,
                lum['upperdesc'], cf['yellow'])
        print('Ellipse tests done in ',
          hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        pdata = []#[[20,c['red']],[30,c['brightyellow']],...]
        for color in c:
                pdata.append([1,c[color]])
        piedata = piechart(bmp, 75, 540, 45, pdata)
        print('Arc and pie chart tests done in ',
                    hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        plotpoly(bmp, p, c['brightcyan'])
        print('Polygon tests done in ',
          hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        plotfilledflower(bmp, 40, 40, 30, 5, 45,
                lum['maxasc'], cf['brightyellow'])
        print('Filled flower test done in ',
              hhmmsselaspedtime(starttime))

        starttime = _time_ns() #[x,y,rad=constant for sample can be variable,isfilled]
        XYdata = []#[[45,45,5,c['brightcyan'],True],[100,60,5,c['brightgreen'],True],..]
        for color in  c:
                XYdata.append(
                        [randint(20,140),
                          randint(30,70),
                          5, c[color], True])
                XYdata.append(
                        [randint(20,140),
                          randint(30,70),
                          5, c[color], False])
                XYcoordinfo = XYaxis(bmp,
                        [172, 598],[40, 40],
                        [666, 398],[20, 30],
                                   [10, 10],
                           c['brightwhite'],
                                  c['gray'],
                                       True,
                              c['darkgreen'])
        XYscatterplot(bmp, XYdata, XYcoordinfo,
                        True, c['green'])
        print('XY scatterplot test done in ',
                hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        buff = copyrect(bmp, 3, 3, 80, 80)
        pasterect(bmp, buff, 858, 611)
        print('Copy paste done in ',
         hhmmsselaspedtime(starttime))
        starttime = _time_ns()
        nbmp = convertselection2BMP(buff)
        nfile = rootdir +'/assets/flower.bmp'
        saveBMP(nfile, nbmp)
        print('Save selection to ',
                nfile,' done in ',
                hhmmsselaspedtime(starttime))

        starttime = _time_ns()
        file = 'test.bmp' # some random filename
        saveBMP(file, bmp) # dump byte array to file
        print('Saved ' + file + ' in ',
        hhmmsselaspedtime(starttime))
        print('Demo done in ',
        hhmmsselaspedtime(demostart))

        print('\nAll done close mspaint to finish')
        ret = proc.call('mspaint ' + file) # replace with another editor if Unix
        print('\nThe')
        print(plot8bitpatternastext([0x00,0x00,0x38,0x6C,0x6C,0x38,0x76,0xDC,0xCC,0xCC,0x76,0x00,0x00,0x00],'&',' '))


if __name__ == "__main__":
        main()

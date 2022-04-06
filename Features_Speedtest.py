#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#
#We make no warranty of any kind, expressed or implied.
#
#The primary author and any subsequent code contributors shall not
#be liable in any event for incidental or consquential damages
#in connection with, or arising out of the use of this code
#in current form or with modifications.
#
#Contact primary author if you plan to use this in a commercial product at
# joelalcarez1975@gmail.com.

#Educational or hobby use highly encouraged.
#
#ps:created out of extreme boredom during the COVID-19 pandemic.
#
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
import time as t
from random import randint
from os import path,getcwd
        
def elaspedtimeinseconds(inittime): return (t.process_time_ns()-inittime)/1000000000

def hhmmsselaspedtime(inittime):
        secs,ns=divmod((t.process_time_ns()-inittime),1000000000)
        mins,secs=divmod(secs,60)
        hrs,mins=divmod(mins,60)
        return str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(secs).zfill(2)+ '.'+str(ns)

def main():
        rootdir=path.abspath(getcwd())
        b.plotbmpastext(b.loadBMP(rootdir+'/assets/pp.bmp')) #load logo
        print('Test for Pure Python graphics lib\n')

        demostart=t.process_time_ns()
        starttime=t.process_time_ns()
        mx=1024
        my=768
        bmp=b.newBMP(mx,my,24)
        print('New bitmap in '+ hhmmsselaspedtime(starttime))
        maxpt,cenpt=b.bottomrightcoord(bmp),b.centercoord(bmp) #bitmap dependent coords
        c,cf,lum=b.getcolorname2RGBdict(),b.getRGBfactors(),b.getdefaultlumrange() #color info
        b.adjustcolordicttopal(bmp,c)
        starttime=t.process_time_ns()
        b.fillbackgroundwithgrad(bmp,lum['maxasc'],cf['blue'],0)
        print('Background gradient test done in ',hhmmsselaspedtime(starttime))
        starttime=t.process_time_ns()
        b.rectangle(bmp,1,1,maxpt[0]-1,maxpt[1]-1,c['white'])
        b.filledgradrect(bmp,395,5,955,41,lum['upperdesc'],cf['orange'],1)
        b.filledrect(bmp,395,44,955,55,c['darkblue'])
        print('Rectangle tests done in ',hhmmsselaspedtime(starttime))
        starttime=t.process_time_ns()
        hc=b.spiralcontrolpointsvert(350,180,5,1.1,5)#we will use this later to make smooth spiral
        b.gradthickroundline(bmp,[800,620],[800,600],7,lum['upperdesc'],cf['darkred'])
        b.plotlines(bmp,hc,c['yellow'])
        cp=[50,150]#all arrows must point outward from cp or bug report please

        b.drawvec(bmp,cp,[50,100],0,c['white'])#color dict more readable than color int
        b.drawvec(bmp,cp,[100,150],0,c['green'])#but if you want to use color int
        b.drawvec(bmp,cp,[50,200],0,c['red'])#the functions will work too
        b.drawvec(bmp,cp,[5,150],0,c['blue'])#up to the color supported
        b.drawvec(bmp,cp,[75,175],0,c['yellow'])# by the loaded bitmap file
        b.drawvec(bmp,cp,[25,125],0,c['magenta'])
        b.drawvec(bmp,cp,[25,175],0,c['orange'])
        b.drawvec(bmp,cp,[75,125],0,c['gray'])
        print('Line tests done in ',hhmmsselaspedtime(starttime))
        starttime=t.process_time_ns()
        fnt=b.font8x8
        strtest='abcdefghijklmnopqrstuvwxyz\n0123456789\'":;.,?!~`@#$%^&()[]{}_*+-/=<>\nABCDEFGHIJKLMNOPQRSTUVWXYZ'
        b.plotstring(bmp,400,10,'My Python GL test',4,1,0,c['lightgray'],fnt)
        b.plotstring(bmp,400,45,'Copyright 2021 by Joel C. Alcarez (joelalcarez1975@gmail.com)',1,1,0,c['brightwhite'],fnt)
        b.plotstring(bmp,300,64,strtest,1,0,0,c['brightgreen'],fnt)
        b.plotstringupsidedown(bmp,10,737,strtest,1,0,0,c['brightgreen'],fnt)
        b.plotreversestring(bmp,300,100,strtest,1,0,0,c['brightgreen'],fnt)
        fnt=b.font8x14
        b.plotstringvertical(bmp,970,30,'Matrix text',2,0,0,c['green'],fnt)
        b.plotstringsideway(bmp,970,730,strtest,1,0,0,c['white'],fnt)
        print('Text tests done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        d,tvect=200,[0,0,100]#be careful with these variables or object goes offscreen
        sd=b.getshapesidedict()
        pts=b.tetrahedravert(80)
        shapes=[[[b.trans(b.cubevert(30),pts[3]),sd["cube"]],cf["darkblue"],True,c['black']],[[b.trans(b.tetrahedravert(30),pts[2]),sd["tetrahedra"]],cf["darkred"],True,c['white']],[[b.trans(b.octahedravert(20),pts[1]),sd["octahedra"]],cf["yellow"],True,c['darkgray']],[[b.trans(b.hexahedravert(30),pts[0]),sd["hexahedra"]],cf["darkgreen"],True,c['darkgreen']]]
        for s in shapes:
                b.plot3Dsolid(bmp,s[0],True,s[1],s[2],s[3],b.rotvec3D(10,5,5),tvect,d,b.addvect(cenpt,[-160,-10]))
                b.plot3Dsolid(bmp,b.decahedvertandsurface(25),True,cf['brightred'],False,0,b.rotvec3D(7,77,20),tvect,d,b.addvect(cenpt,[280,-250]))
                b.plot3Dsolid(bmp,b.dodecahedvertandsurface(25),True,cf['brightwhite'],False,0,b.rotvec3D(70,7,20),tvect,d,b.addvect(cenpt,[+60,-130]))
                b.plot3Dsolid(bmp,b.spherevertandsurface([5,0,0],60,10),True,cf['brightwhite'],False,0,b.rotvec3D(190,145,70),tvect,d,b.addvect(cenpt,[300,-50]))
                b.plot3Dsolid(bmp,b.cylindervertandsurface([1,0,0],20,10,5),True,cf['brightyellow'],True,b.RGB2int(20,20,0),b.rotvec3D(60,74,72),tvect,d,b.addvect(cenpt,[-200,-50]))
                b.plot3Dsolid(bmp,b.conevertandsurface([1,0,0],20,15,5),True,cf['brightorange'],False,b.RGB2int(20,20,0),b.rotvec3D(6,67,2),tvect,d,b.addvect(cenpt,[-300,-150]))
                b.plot3Dsolid(bmp,b.surfplot3Dvertandsurface (-35,-35,35,35,15,5),True,cf['brightcyan'],True,0,b.rotvec3D(20,67,30),tvect,d,b.addvect(cenpt,[-420,-25]))
        print('3D tests done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        mandelpar=b.mandelparamdict()#seems preferable to store common params
        b.mandelbrot(bmp,10,600,130,735,mandelpar['maxeqdim'],cf['brightgreen'],255)
        p=b.getIFSparams()#same here add more to this dict
        b.IFS(bmp,p['fern'],170,600,270,730,12,12,30,30,c['lightgreen'],10000)
        b.IFS(bmp,p['tree'],270,600,370,730,100,100,0,0,c['brown'],10000)
        b.IFS(bmp,p['cantortree'],370,600,450,730,100,100,0,0,c['lightcyan'],10000)
        b.IFS(bmp,p['sierpinskitriamgle'],450,600,670,730,100,100,0,0,c['cyan'],10000)
        print('Fractal tests done in ',hhmmsselaspedtime(starttime))
        p=b.regpolygonvert(250,80,40,6,0)
        starttime=t.process_time_ns()
        b.beziercurve(bmp,p,3,c['brightorange'])
        b.beziercurve(bmp,hc,0,c['lightred'])
        print('Bezier curve tests done in ',hhmmsselaspedtime(starttime) )

        starttime=t.process_time_ns() #bspline follow control points better than bezier
        b.bspline(bmp,p,0,c['red'],True,True)
        b.bspline(bmp,hc,0,c['brightwhite'],True,True)
        b.gradvert(bmp,b.bsplinevert(b.spiralcontrolpointsvert(165,135,7,1.2,3),False,False),5,lum['upperdesc'],cf['brightwhite'])
        print('Bspline tests done in ',hhmmsselaspedtime(starttime) )

        starttime=t.process_time_ns()
        b.gradcircle(bmp,900,140,30,lum['maxdesc'],cf['brightyellow'])
        b.gradthickcircle(bmp,900,550,40,8,lum['upperdesc'],cf['lightred'])
        print('Circle tests done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        b.gradellipse(bmp,750,550,20,40,lum['upperdesc'],cf['brightorange'])
        b.gradthickellipserot(bmp,790,700,50,30,45,5,lum['upperdesc'],cf['yellow'])
        print('Ellipse tests done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()#works but no live db conn yet plot as code below
        pdata=[]#[[20,c['red']],[30,c['brightyellow']],...]
        for color in  c: pdata.append([1,c[color]])
        piedata=b.piechart(bmp,75,540,45,pdata)
        print('Arc and pie chart tests done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        b.plotpoly(bmp,p,c['brightcyan'])
        print('Polygon tests done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        b.plotfilledflower(bmp,40,40,30,5,45,lum['maxasc'],cf['brightyellow'])
        print('Filled flower test done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns() #[x,y,rad=constant for sample can be variable,isfilled]
        XYdata=[]#[[45,45,5,c['brightcyan'],True],[100,60,5,c['brightgreen'],True],..]
        for color in  c:
                XYdata.append([randint(20,140),randint(30,70),5,c[color],True])
                XYdata.append([randint(20,140),randint(30,70),5,c[color],False])
                XYcoordinfo=b.XYaxis(bmp,[172,598],[40,40],[666,398],[20,30],[10,10],c['brightwhite'],c['gray'],True,c['darkgreen'])
        b.XYscatterplot(bmp,XYdata,XYcoordinfo,True,c['green'])
        print('XY scatterplot test done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        buff=b.copyrect(bmp,3,3,80,80)
        b.pasterect(bmp,buff,858,611)
        print('Copy paste done in ',hhmmsselaspedtime(starttime))
        starttime=t.process_time_ns()
        nbmp=b.convertselection2BMP(buff)
        nfile='assets/flower.bmp'
        b.saveBMP(nfile,nbmp)
        print('Save selection to ',nfile,' done in ',hhmmsselaspedtime(starttime))

        starttime=t.process_time_ns()
        file='test.bmp'
        b.saveBMP(file,bmp)
        print('Saved '+ file + ' in ',hhmmsselaspedtime(starttime))
        print('Demo done in ',hhmmsselaspedtime(demostart))

        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix
        print('\nThe')
        print(b.plot8bitpatternastext([0x00,0x00,0x38,0x6C,0x6C,0x38,0x76,0xDC,0xCC,0xCC,0x76,0x00,0x00,0x00],'&',' '))


if __name__=="__main__": 
        main()



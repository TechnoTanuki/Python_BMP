#/--------------------------------------------------------------------------\
#|    Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]      |
#|--------------------------------------------------------------------------|
#|    We make absolutely no warranty of any kind, expressed or implied.     |
#|--------------------------------------------------------------------------|
#|    The primary author and any subsequent code contributors shall not     |
#|    be liable  in any event  for  incidental or consquential  damages     |
#|    in connection with,  or arising out  from  the  use of  this code     |
#|    in current form or with any modifications.                            |
#|--------#--------------------------------------------------------#--------|
#|        |  Contact primary author if you plan to use this        |        |
#|        |  in a commercial product at joelalcarez1975@gmail.com  |        |
#|--------#--------------------------------------------------------#--------|
#|    Educational or hobby use highly encouraged... have fun coding !       |
#|    ps:created out of extreme boredom during the COVID-19 pandemic.       |
#|--------#--------------------------------------------------------#--------|
#|        |  Note: This graphics library outputs to a bitmap file. |        |
#\--------#--------------------------------------------------------#--------/

import Python_BMP.BITMAPlib as b,subprocess as proc
import time as t
from random import randint
from os import path,sys
        
def elaspedtimeinseconds(inittime): return (t.process_time_ns()-inittime)/1000000000

def hhmmsselaspedtime(inittime):
        secs,ns=divmod((t.process_time_ns()-inittime),1000000000)
        mins,secs=divmod(secs,60)
        hrs,mins=divmod(mins,60)
        return str(hrs).zfill(2)+':'+str(mins).zfill(2)+':'+str(secs).zfill(2)+ '.'+str(ns)

def main():
        rootdir=path.abspath(sys.path[0])
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
import unittest,os
from Python_BMP.BITMAPlib import loadBMP,getRGBfactors,int2RGB,getcolorname2RGBdict,invertregion2file,flipXY2file,fliphorizontal2file,flipverticalregion2file,fliphorizontalregion2file,cropBMPandsave,imgregionbyRGB2file,adjustbrightness2file,gammaadj2file,adjustbrightnessinregion2file,monochrome2file,monofilterinregion2file,colorfilter2file,colorfilterinregion2file,adjustthresholdinregion2file,gammaadjtoregion2file,resizeNtimessmaller2file,resizeNtimesbigger2file,outline2file,outlineregion2file,monochromecircregion2file,colorfiltercircregion2file,circle2file,thresholdadjcircregion2file,gammacorrectcircregion2file,brightnessadjcircregion2file,invertbitsincircregion2file,flipvertcircregion2file,fliphoricircregion2file,outlinecircregion2file,flipXYcircregion2file,magnifyNtimescircregion2file,copycircregion2file,verticalbrightnessgradregion2file,horizontalbrightnessgradregion2file,mirrortop2file,mirrorbottom2file,mirrortopleft2file,mirrortopright2file,mirrorbottomleft2file,mirrorbottomright2file,mirrorleft2file,mirrorright2file,verticalbrightnessgrad2file,horizontalbrightnessgrad2file,vertbrightnessgrad2circregion2file,horibrightnessgrad2circregion2file,mirrorrightinregion2file,mirrorleftinregion2file,mirrortopinregion2file,mirrorbottominregion2file,mirrortopleftinregion2file,mirrortoprightinregion2file,mirrorbottomleftinregion2file,mirrorbottomrightinregion2file,rectangle2file,fern2file,thresholdadjust2file,eraseeverynthhoriline2file,eraseeverynthhorilineinregion2file,eraseeverynthhorilineinccircregion2file,pixelizenxncircregion2file,pixelizenxntofile,sphere2file,thickencirclearea2file,filledcircle2file,mirrortopincircregion2file,mirrorbottomincircregion2file,mirrorleftincircregion2file,mirrorrightincircregion2file,mirrortopleftincircregion2file,mirrorbottomleftincircregion2file,mirrortoprightincircregion2file,mirrorbottomrightincircregion2file,upgradeto24bitimage2file,reduce24bitimagebits,autocropimg2file

rootdir =os.path.abspath(os.sys.path[0])
testimgdir='/assets/test_images/'
sdir=rootdir+testimgdir
odir=rootdir+'/test_output/'
ofile=sdir+'raccoon.bmp'

cf=getRGBfactors()
c=getcolorname2RGBdict()

class Test2filefunc(unittest.TestCase):

        def filecmp(self,filename1,filename2):
                bmp1,bmp2=loadBMP(filename1),loadBMP(filename2)
                self.assertIsNotNone(bmp1)
                self.assertIsNotNone(bmp2)
                self.assertEqual(bmp1,bmp2)

        def dotestfullimg(self,filename,func):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile)
                self.filecmp(reffile,newfile)

        def dotestfullimgwithparam(self,filename,func,funcparam):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile,funcparam)
                self.filecmp(reffile,newfile)

        def dotestrectregion(self,filename,func,x1,y1,x2,y2):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile,x1,y1,x2,y2)
                self.filecmp(reffile,newfile)

        def dotestrectregionwithparam(self,filename,func,x1,y1,x2,y2,funcparam):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile,x1,y1,x2,y2,funcparam)
                self.filecmp(reffile,newfile)

        def dotestcircregion(self,filename,func,x,y,r):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile,x,y,r)
                self.filecmp(reffile,newfile)

        def dotestcircregionwithparam(self,filename,func,x,y,r,funcparam):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile,x,y,r,funcparam)
                self.filecmp(reffile,newfile)
                  
        def setUp(self): pass

        def tearDown(self): pass

        def testmirrortop2file(self): self.dotestfullimg('raccoon-mirrortop.bmp',mirrortop2file)

        def testmirrorbottom2file(self): self.dotestfullimg('raccoon-mirrorbottom.bmp',mirrorbottom2file)

        def testmirrorleft2file(self): self.dotestfullimg('raccoon-mirrorleft.bmp',mirrorleft2file)

        def testmirrorright2file(self): self.dotestfullimg('raccoon-mirrorright.bmp',mirrorright2file)

        def testmirrortopleft2file(self): self.dotestfullimg('raccoon-mirrortopleft.bmp',mirrortopleft2file)

        def testmirrortopright2file(self): self.dotestfullimg('raccoon-mirrortopright.bmp',mirrortopright2file)

        def testmirrorbottomleft2file(self): self.dotestfullimg('raccoon-mirrorbottomleft.bmp',mirrorbottomleft2file)

        def testmirrorbottomright2file(self): self.dotestfullimg('raccoon-mirrorbottomright.bmp',mirrorbottomright2file)

        def testmonochrome2file(self): self.dotestfullimg('raccoon-monochrome.bmp',monochrome2file)

        def testoutline2file(self): self.dotestfullimg('raccoon-outline.bmp',outline2file)
                
        def testflipXY2file(self): self.dotestfullimg('raccoon-flipXY.bmp',flipXY2file)
        
        def testfliphorizontal2file(self): self.dotestfullimg('raccoon-fliphorizontal.bmp',fliphorizontal2file)

        def testflipverticalregion2file(self): self.dotestrectregion('raccoon-flipverticalregion.bmp',flipverticalregion2file,250,60,860,666)
        
        def testoutlineregion2file(self):  self.dotestrectregion('raccoon-outlineregion.bmp',outlineregion2file,250,60,860,666)

        def testinvertregion2file(self): self.dotestrectregion('raccoon-inv-reg.bmp',invertregion2file,250,60,860,666)

        def testfliphorizontalregion2file(self): self.dotestrectregion('raccoon-fliphorizontalregion.bmp',fliphorizontalregion2file,250,60,860,666)
        
        def testcropBMPandsave(self): self.dotestrectregion('raccoon-cropregion.bmp',cropBMPandsave,250,60,860,666)

        def testmonofilterinregion2file(self): self.dotestrectregion('raccoon-monofilterinregion.bmp',monofilterinregion2file,250,60,860,666)

        def testmirrorrightinregion2file(self): self.dotestrectregion('raccoon-mirrorrightinregion.bmp',mirrorrightinregion2file,250,60,860,666)

        def testmirrorleftinregion2file(self): self.dotestrectregion('raccoon-mirrorleftinregion.bmp',mirrorleftinregion2file,250,60,860,666)

        def testmirrortopinregion2file(self): self.dotestrectregion('raccoon-mirrortopinregion.bmp',mirrortopinregion2file,250,60,860,666)

        def testmirrorbottominregion2file(self): self.dotestrectregion('raccoon-mirrorbottominregion.bmp',mirrorbottominregion2file,250,60,860,666)

        def testmirrortopleftinregion2file(self): self.dotestrectregion('raccoon-mirrortopleftinregion.bmp',mirrortopleftinregion2file,250,60,860,666)

        def testmirrortoprightinregion2file(self): self.dotestrectregion('raccoon-mirrortoprightinregion.bmp',mirrortoprightinregion2file,250,60,860,666)

        def testmirrorbottomleftinregion2file(self): self.dotestrectregion('raccoon-mirrorbottomleftinregion.bmp',mirrorbottomleftinregion2file,250,60,860,666)

        def testmirrorbottomrightinregion2file(self): self.dotestrectregion('raccoon-mirrorbottomrightinregion.bmp',mirrorbottomrightinregion2file,250,60,860,666)

        def testeraseeverynthhoriline2file(self): self.dotestfullimgwithparam('raccoon-eraseeverynthhoriline.bmp',eraseeverynthhoriline2file,3)

        def testpixelizenxntofile(self): self.dotestfullimgwithparam('raccoon-pixelizenx.bmp',pixelizenxntofile,15)

        def testthresholdadjust2file(self): self.dotestfullimgwithparam('raccoon-thresholdadjust.bmp',thresholdadjust2file,[24,192])

        def testgammaadj2file(self): self.dotestfullimgwithparam('raccoon-gammaadj.bmp',gammaadj2file,.45)

        def testverticalbrightnessgrad2file(self): self.dotestfullimgwithparam('raccoon-verticalbrightnessgrad.bmp',verticalbrightnessgrad2file,[200,-100])

        def testhorizontalbrightnessgrad2file(self): self.dotestfullimgwithparam('raccoon-horizontalbrightnessgrad.bmp',horizontalbrightnessgrad2file,[200,-100])

        def testcolorfilter2file(self): self.dotestfullimgwithparam('raccoon-cyanfilter.bmp',colorfilter2file,cf['cyan'])

        def testadjustbrightness2file(self): self.dotestfullimgwithparam('raccoon-adjustbrightness.bmp',adjustbrightness2file,200)

        def testresizeNtimessmaller2file(self):  self.dotestfullimgwithparam('raccoon-8timessmall.bmp',resizeNtimessmaller2file,8)

        def testresizeNtimesbigger2file(self):  self.dotestfullimgwithparam('raccoon-3timebigger.bmp',resizeNtimesbigger2file,3)
        
        def testadjustbrightnessinregion2file(self): self.dotestrectregionwithparam('raccoon-adjustbrightnessinregion.bmp',adjustbrightnessinregion2file,250,60,860,666,150)

        def testrectangle2file(self): self.dotestrectregionwithparam('raccoon-rectangle.bmp',rectangle2file,250,60,860,666,c['red'])

        #def testfern2file(self): self.dotestrectregionwithparam('raccoon-fern.bmp',fern2file,250,60,860,666,c['green'])

        def testcolorfilterinregion2file(self):  self.dotestrectregionwithparam('raccoon-cyanfilteregion.bmp',colorfilterinregion2file,250,60,860,666,cf['cyan'])
        
        def testhorizontalbrightnessgradregion2file(self):   self.dotestrectregionwithparam('raccoon-horizontalbrightnessgradregion.bmp',horizontalbrightnessgradregion2file,250,60,860,666,[200,-80])
        
        def testeraseeverynthhorilineinregion2fil(self):  self.dotestrectregionwithparam('raccoon-eraseeverynthhorilineinregion.bmp',eraseeverynthhorilineinregion2file,250,60,860,666,3)

        def testadjustthresholdinregion2file(self):  self.dotestrectregionwithparam('raccoon-adjustthresholdinregion.bmp',adjustthresholdinregion2file,250,60,860,666,[24,160])

        def testgammaadjtoregion2file(self):  self.dotestrectregionwithparam('raccoon-gammaadjtoregion.bmp',gammaadjtoregion2file,250,60,860,666,.45)

        def testinvertbitsincircregion2file(self): self.dotestcircregion('raccoon-invertbitsincircregion.bmp',invertbitsincircregion2file,500,300,400)
        
        def testflipvertcircregion2file(self): self.dotestcircregion('raccoon-flipvertcircregion.bmp',flipvertcircregion2file,500,300,300)
        
        def testfliphoricircregion2file(self): self.dotestcircregion('raccoon-fliphoricircregion.bmp',fliphoricircregion2file,500,300,300)

        def testoutlinecircregion2file(self): self.dotestcircregion('raccoon-outlinecircregion.bmp',outlinecircregion2file,500,360,400)

        def testflipXYcircregion2file(self):  self.dotestcircregion('raccoon-flipXYcircregion.bmp',flipXYcircregion2file,500,300,300)
        
        def testmonochromecircregion2file(self): self.dotestcircregion('raccoon-monochromecircregion.bmp',monochromecircregion2file,500,300,300)
        
        def testcolorfiltercircregion2file(self):  self.dotestcircregionwithparam('raccoon-yellowcircregion.bmp',colorfiltercircregion2file,500,300,300,cf['yellow'])                

        def testcircle2file(self): self.dotestcircregionwithparam('raccoon-thinredcircle.bmp',circle2file,500,300,280,c['red'])

        def testthresholdadjcircregion2file(self): self.dotestcircregionwithparam('raccoon-thresholdadjcircregion.bmp',thresholdadjcircregion2file,500,400,250,[32,152])

        def testgammacorrectcircregion2file(self):  self.dotestcircregionwithparam('raccoon-gammacorrectcircregion.bmp',gammacorrectcircregion2file,500,300,280,.45)
        
        def testbrightnessadjcircregion2file(self):  self.dotestcircregionwithparam('raccoon-brightnessadjcircregion.bmp',brightnessadjcircregion2file,500,300,290,80)
                
        def testmagnifyNtimescircregion2file(self):   self.dotestcircregionwithparam('raccoon-magnify2timescircregion.bmp',magnifyNtimescircregion2file,500,300,300,2)
        
        def testcopycircregion2file(self):  self.dotestcircregionwithparam('raccoon-copycircregion.bmp',copycircregion2file,500,300,200,[240,400])
        
        def testvertbrightnessgrad2circregion2file(self):  self.dotestcircregionwithparam('raccoon-vertbrightnessgrad2circregion.bmp',vertbrightnessgrad2circregion2file,500,350,250,[200,-100])

        def testhoribrightnessgrad2circregion2file(self):  self.dotestcircregionwithparam('raccoon-horibrightnessgrad2circregion.bmp',horibrightnessgrad2circregion2file,500,300,300,[200,-100])

        def testeraseeverynthhorilineinccircregion2file(self):  self.dotestcircregionwithparam('raccoon-eraseeverynthhorilineinccircregion.bmp',eraseeverynthhorilineinccircregion2file,500,300,300,3)

        def testpixelizenxncircregion2file(self):  self.dotestcircregionwithparam('raccoon-pixelizenxncircregion.bmp',pixelizenxncircregion2file,500,300,300,9)

        def testsphere2file(self):  self.dotestcircregionwithparam('raccoon-sphere.bmp',sphere2file,120,170,100,cf['cyan'])

        def testthickencirclearea2file(self):  self.dotestcircregionwithparam('raccoon-thickencirclearea.bmp',thickencirclearea2file,500,300,280,cf['yellow'])

        def testfilledcircle2file(self):  self.dotestcircregionwithparam('raccoon-filledcircle.bmp',filledcircle2file,120,170,100,c['yellow'])

        def testmirrortopincircregion2file(self):  self.dotestcircregion('raccoon-mirrortopincircregion.bmp',mirrortopincircregion2file,500,300,300)
        
        def testmirrorbottomincircregion2file(self):  self.dotestcircregion('raccoon-mirrorbottomincircregion.bmp',mirrorbottomincircregion2file,500,300,300)

        def testmirrorleftincircregion2file(self):  self.dotestcircregion('raccoon-mirrorleftincircregion.bmp',mirrorleftincircregion2file,500,300,300)

        def testmirrorrightincircregion2file(self):  self.dotestcircregion('raccoon-mirrorrightincircregion.bmp',mirrorrightincircregion2file,500,300,300)

        def testmirrortopleftincircregion2file(self):  self.dotestcircregion('raccoon-mirrortopleftincircregion.bmp',mirrortopleftincircregion2file,500,300,300)

        def testmirrorbottomleftincircregion2file(self):  self.dotestcircregion('raccoon-mirrorbottomleftincircregion.bmp',mirrorbottomleftincircregion2file,500,300,300)

        def testmirrortoprightincircregion2file(self):  self.dotestcircregion('raccoon-mirrortoprightincircregion.bmp',mirrortoprightincircregion2file,500,300,300)

        def testmirrorbottomrightincircregion2file(self):  self.dotestcircregion('raccoon-mirrorbottomrightincircregion.bmp',mirrorbottomrightincircregion2file,500,300,300)

        def testimgregionbyRGB2file(self):
                filename='raccoon-edgebycolorbrown.bmp'
                newfile,reffile=odir+filename,sdir+filename
                imgregionbyRGB2file(ofile,newfile,1,c['brown'],int2RGB(c['brown']),120,True)
                self.filecmp(reffile,newfile)
                
        def testreduce24bitimagebits(self):
                filename='raccoon-4bit.bmp'
                newfile,reffile=odir+filename,sdir+filename
                reduce24bitimagebits(ofile,newfile,4,24,False,[0.25,.5,1])
                self.filecmp(reffile,newfile)
        
        def testautocropimg2file(self):
                filename='flower-autocrop.bmp'
                newfile,reffile=odir+filename,sdir+filename
                autocropimg2file(sdir+'flower.bmp',newfile,64) 
                self.filecmp(reffile,newfile)                
                

if __name__ == "__main__":
        unittest.main()
   

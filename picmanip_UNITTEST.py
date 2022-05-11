#/--------------------------------------------------------------------\
#|  Copyright 2022 by Joel C. Alcarez    [joelalcarez1975@gmail.com]  |
#|--------------------------------------------------------------------|
#|  We make absolutely no warranty of any kind, expressed or implied. |
#|--------------------------------------------------------------------|
#|  The primary author and any subsequent code contributors shall not |
#|  be liable  in any event  for  incidental or consequential damages |
#|  in connection with,  or arising out  from  the  use of  this code |
#|  in current form or with any modifications.                        |
#|-----#--------------------------------------------------------#-----|
#      |  Contact primary author if you plan to use this        |     |
#|     |  in a commercial product at joelalcarez1975@gmail.com  |     |
#|-----#--------------------------------------------------------#-----|
#|  Educational or hobby use highly encouraged... have fun coding !   |
#|  ps:created out of extreme boredom during the COVID-19 pandemic.   |
#|-----#--------------------------------------------------------#-----|
#|     |  Note: This graphics library outputs to a bitmap file. |     |
#\-----#--------------------------------------------------------------/

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

        def dotestcircregion(
                self,
                filename,
                func,
                x, y, r):
                newfile,reffile=odir+filename,sdir+filename
                func(ofile,newfile,x,y,r)
                self.filecmp(reffile,newfile)

        def dotestcircregionwithparam(
                self,
                filename,
                func,
                x, y, r,
                funcparam):
                newfile = odir + filename
                reffile = sdir + filename
                func(ofile, newfile,
                     x, y, r, funcparam)
                self.filecmp(reffile, newfile)

        def setUp(self): pass

        def tearDown(self): pass

        def testmirrortop2file(self):
                self.dotestfullimg('raccoon-mirrortop.bmp',mirrortop2file)

        def testmirrorbottom2file(self):
                self.dotestfullimg('raccoon-mirrorbottom.bmp',mirrorbottom2file)

        def testmirrorleft2file(self):
                self.dotestfullimg('raccoon-mirrorleft.bmp',mirrorleft2file)

        def testmirrorright2file(self):
                self.dotestfullimg('raccoon-mirrorright.bmp',mirrorright2file)

        def testmirrortopleft2file(self):
                self.dotestfullimg('raccoon-mirrortopleft.bmp',mirrortopleft2file)

        def testmirrortopright2file(self):
                self.dotestfullimg('raccoon-mirrortopright.bmp',mirrortopright2file)

        def testmirrorbottomleft2file(self):
                self.dotestfullimg('raccoon-mirrorbottomleft.bmp',mirrorbottomleft2file)

        def testmirrorbottomright2file(self):
                self.dotestfullimg('raccoon-mirrorbottomright.bmp',mirrorbottomright2file)

        def testmonochrome2file(self):
                self.dotestfullimg('raccoon-monochrome.bmp',monochrome2file)

        def testoutline2file(self):
                self.dotestfullimg('raccoon-outline.bmp',outline2file)

        def testflipXY2file(self):
                self.dotestfullimg('raccoon-flipXY.bmp',flipXY2file)

        def testfliphorizontal2file(self):
                self.dotestfullimg('raccoon-fliphorizontal.bmp',fliphorizontal2file)

        def testflipverticalregion2file(self):
                self.dotestrectregion('raccoon-flipverticalregion.bmp',flipverticalregion2file,250,60,860,666)

        def testoutlineregion2file(self):
                self.dotestrectregion('raccoon-outlineregion.bmp',outlineregion2file,250,60,860,666)

        def testinvertregion2file(self):
                self.dotestrectregion('raccoon-inv-reg.bmp',invertregion2file,250,60,860,666)

        def testfliphorizontalregion2file(self):
                self.dotestrectregion('raccoon-fliphorizontalregion.bmp',fliphorizontalregion2file,250,60,860,666)

        def testcropBMPandsave(self):
                self.dotestrectregion('raccoon-cropregion.bmp',cropBMPandsave,250,60,860,666)

        def testmonofilterinregion2file(self):
                self.dotestrectregion('raccoon-monofilterinregion.bmp',monofilterinregion2file,250,60,860,666)

        def testmirrorrightinregion2file(self):
                self.dotestrectregion('raccoon-mirrorrightinregion.bmp',mirrorrightinregion2file,250,60,860,666)

        def testmirrorleftinregion2file(self):
                self.dotestrectregion('raccoon-mirrorleftinregion.bmp',mirrorleftinregion2file,250,60,860,666)

        def testmirrortopinregion2file(self):
                self.dotestrectregion('raccoon-mirrortopinregion.bmp',mirrortopinregion2file,250,60,860,666)

        def testmirrorbottominregion2file(self):
                self.dotestrectregion('raccoon-mirrorbottominregion.bmp',mirrorbottominregion2file,250,60,860,666)

        def testmirrortopleftinregion2file(self):
                self.dotestrectregion('raccoon-mirrortopleftinregion.bmp',mirrortopleftinregion2file,250,60,860,666)

        def testmirrortoprightinregion2file(self):
                self.dotestrectregion('raccoon-mirrortoprightinregion.bmp',mirrortoprightinregion2file,250,60,860,666)

        def testmirrorbottomleftinregion2file(self):
                self.dotestrectregion('raccoon-mirrorbottomleftinregion.bmp',mirrorbottomleftinregion2file,250,60,860,666)

        def testmirrorbottomrightinregion2file(self):
                self.dotestrectregion('raccoon-mirrorbottomrightinregion.bmp',mirrorbottomrightinregion2file,250,60,860,666)

        def testeraseeverynthhoriline2file(self):
                self.dotestfullimgwithparam('raccoon-eraseeverynthhoriline.bmp',eraseeverynthhoriline2file,3)

        def testpixelizenxn2file(self):
                self.dotestfullimgwithparam('raccoon-pixelizenx.bmp',pixelizenxntofile,15)

        def testthresholdadjust2file(self):
                self.dotestfullimgwithparam('raccoon-thresholdadjust.bmp',thresholdadjust2file,[24,192])

        def testgammaadj2file(self):
                self.dotestfullimgwithparam('raccoon-gammaadj.bmp',gammaadj2file,.45)

        def testverticalbrightnessgrad2file(self):
                self.dotestfullimgwithparam('raccoon-verticalbrightnessgrad.bmp',verticalbrightnessgrad2file,[200,-100])

        def testhorizontalbrightnessgrad2file(self):
                self.dotestfullimgwithparam('raccoon-horizontalbrightnessgrad.bmp',horizontalbrightnessgrad2file,[200,-100])

        def testcolorfilter2file(self):
                self.dotestfullimgwithparam('raccoon-cyanfilter.bmp',colorfilter2file,cf['cyan'])

        def testadjustbrightness2file(self):
                self.dotestfullimgwithparam('raccoon-adjustbrightness.bmp',adjustbrightness2file,200)

        def testresizeNtimessmaller2file(self):
                self.dotestfullimgwithparam('raccoon-8timessmall.bmp',resizeNtimessmaller2file,8)

        def testresizeNtimesbigger2file(self):
                self.dotestfullimgwithparam('raccoon-3timebigger.bmp',resizeNtimesbigger2file,3)

        def testadjustbrightnessinregion2file(self):
                self.dotestrectregionwithparam('raccoon-adjustbrightnessinregion.bmp',adjustbrightnessinregion2file,250,60,860,666,150)

        def testrectangle2file(self):
                self.dotestrectregionwithparam('raccoon-rectangle.bmp',rectangle2file,250,60,860,666,c['red'])

        #def testfern2file(self): self.dotestrectregionwithparam('raccoon-fern.bmp',fern2file,250,60,860,666,c['green'])

        def testcolorfilterinregion2file(self):
                self.dotestrectregionwithparam('raccoon-cyanfilteregion.bmp',colorfilterinregion2file,250,60,860,666,cf['cyan'])

        def testhorizontalbrightnessgradregion2file(self):
                self.dotestrectregionwithparam('raccoon-horizontalbrightnessgradregion.bmp',horizontalbrightnessgradregion2file,250,60,860,666,[200,-80])

        def testeraseeverynthhorilineinregion2fil(self):
                self.dotestrectregionwithparam('raccoon-eraseeverynthhorilineinregion.bmp',eraseeverynthhorilineinregion2file,250,60,860,666,3)

        def testadjustthresholdinregion2file(self):
                self.dotestrectregionwithparam('raccoon-adjustthresholdinregion.bmp',adjustthresholdinregion2file,250,60,860,666,[24,160])

        def testgammaadjtoregion2file(self):
                self.dotestrectregionwithparam('raccoon-gammaadjtoregion.bmp',gammaadjtoregion2file,250,60,860,666,.45)

        def testinvertbitsincircregion2file(self):
                self.dotestcircregion('raccoon-invertbitsincircregion.bmp',invertbitsincircregion2file,500,300,400)

        def testflipvertcircregion2file(self):
                self.dotestcircregion('raccoon-flipvertcircregion.bmp',flipvertcircregion2file,500,300,300)

        def testfliphoricircregion2file(self):
                self.dotestcircregion('raccoon-fliphoricircregion.bmp',fliphoricircregion2file,500,300,300)

        def testoutlinecircregion2file(self):
                self.dotestcircregion('raccoon-outlinecircregion.bmp',outlinecircregion2file,500,360,400)

        def testflipXYcircregion2file(self):
                self.dotestcircregion('raccoon-flipXYcircregion.bmp',flipXYcircregion2file,500,300,300)

        def testmonochromecircregion2file(self):
                self.dotestcircregion('raccoon-monochromecircregion.bmp',monochromecircregion2file,500,300,300)

        def testcolorfiltercircregion2file(self):
                self.dotestcircregionwithparam('raccoon-yellowcircregion.bmp',colorfiltercircregion2file,500,300,300,cf['yellow'])

        def testcircle2file(self):
                self.dotestcircregionwithparam('raccoon-thinredcircle.bmp',circle2file,500,300,280,c['red'])

        def testthresholdadjcircregion2file(self):
                self.dotestcircregionwithparam('raccoon-thresholdadjcircregion.bmp',thresholdadjcircregion2file,500,400,250,[32,152])

        def testgammacorrectcircregion2file(self):
                self.dotestcircregionwithparam('raccoon-gammacorrectcircregion.bmp',gammacorrectcircregion2file,500,300,280,.45)

        def testbrightnessadjcircregion2file(self):
                self.dotestcircregionwithparam('raccoon-brightnessadjcircregion.bmp',brightnessadjcircregion2file,500,300,290,80)

        def testmagnifyNtimescircregion2file(self):
                self.dotestcircregionwithparam('raccoon-magnify2timescircregion.bmp',magnifyNtimescircregion2file,500,300,300,2)

        def testcopycircregion2file(self):
                self.dotestcircregionwithparam('raccoon-copycircregion.bmp',copycircregion2file,500,300,200,[240,400])

        def testvertbrightnessgrad2circregion2file(self):  self.dotestcircregionwithparam('raccoon-vertbrightnessgrad2circregion.bmp',vertbrightnessgrad2circregion2file,500,350,250,[200,-100])

        def testhoribrightnessgrad2circregion2file(self):
                self.dotestcircregionwithparam('raccoon-horibrightnessgrad2circregion.bmp',horibrightnessgrad2circregion2file,500,300,300,[200,-100])

        def testeraseeverynthhorilineinccircregion2file(self):
                self.dotestcircregionwithparam('raccoon-eraseeverynthhorilineinccircregion.bmp',eraseeverynthhorilineinccircregion2file,500,300,300,3)

        def testpixelizenxncircregion2file(self):
                self.dotestcircregionwithparam('raccoon-pixelizenxncircregion.bmp',pixelizenxncircregion2file,500,300,300,9)

        def testsphere2file(self):
                self.dotestcircregionwithparam('raccoon-sphere.bmp',sphere2file,120,170,100,cf['cyan'])

        def testthickencirclearea2file(self):
                self.dotestcircregionwithparam('raccoon-thickencirclearea.bmp',thickencirclearea2file,500,300,280,cf['yellow'])

        def testfilledcircle2file(self):  self.dotestcircregionwithparam('raccoon-filledcircle.bmp',filledcircle2file,120,170,100,c['yellow'])

        def testmirrortopincircregion2file(self):
                self.dotestcircregion('raccoon-mirrortopincircregion.bmp',mirrortopincircregion2file,500,300,300)

        def testmirrorbottomincircregion2file(self):
                self.dotestcircregion('raccoon-mirrorbottomincircregion.bmp',mirrorbottomincircregion2file,500,300,300)

        def testmirrorleftincircregion2file(self):
                self.dotestcircregion('raccoon-mirrorleftincircregion.bmp',mirrorleftincircregion2file,500,300,300)

        def testmirrorrightincircregion2file(self):
                self.dotestcircregion('raccoon-mirrorrightincircregion.bmp',mirrorrightincircregion2file,500,300,300)

        def testmirrortopleftincircregion2file(self):
                self.dotestcircregion('raccoon-mirrortopleftincircregion.bmp',mirrortopleftincircregion2file,500,300,300)

        def testmirrorbottomleftincircregion2file(self):
                self.dotestcircregion('raccoon-mirrorbottomleftincircregion.bmp',mirrorbottomleftincircregion2file,500,300,300)

        def testmirrortoprightincircregion2file(self):
                self.dotestcircregion('raccoon-mirrortoprightincircregion.bmp',mirrortoprightincircregion2file,500,300,300)

        def testmirrorbottomrightincircregion2file(self):
                self.dotestcircregion('raccoon-mirrorbottomrightincircregion.bmp',mirrorbottomrightincircregion2file,500,300,300)

        def testimgregionbyRGB2file(self):
                filename='raccoon-edgebycolorbrown.bmp'
                newfile = odir + filename
                reffile = sdir + filename
                imgregionbyRGB2file(
                        ofile,
                        newfile,
                        1,
                        c['brown'],
                        int2RGB(c['brown']),
                        120, True)
                self.filecmp(reffile,
                             newfile)

        def testreduce24bitimagebits(self):
                filename='raccoon-4bit.bmp'
                newfile = odir + filename
                reffile = sdir + filename
                reduce24bitimagebits(
                        ofile,
                        newfile,
                        4, 24,
                        False,
                        [0.25,.5,1])
                self.filecmp(reffile,
                             newfile)

        def testautocropimg2file(self):
                filename = 'flower-autocrop.bmp'
                newfile = odir + filename
                reffile = sdir + filename
                autocropimg2file(sdir + 'flower.bmp',
                                 newfile,64)
                self.filecmp(reffile,
                             newfile)


if __name__ == "__main__":
        unittest.main()


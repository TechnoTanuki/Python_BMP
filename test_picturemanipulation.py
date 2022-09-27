notice = """
 Unit tests
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
from typing import Callable
import unittest
from os import path
from Python_BMP.BITMAPlib import(
        adjustbrightness2file,
        adjustbrightnessinregion2file,
        adjustthresholdinregion2file,
        autocropimg2file,
        brightnessadjcircregion2file,
        circle2file,
        colorfilter2file,
        colorfiltercircregion2file,
        colorfilterinregion2file,
        copycircregion2file,
        cropBMPandsave,
        eraseeverynthhoriline2file,
        eraseeverynthhorilineinccircregion2file,
        eraseeverynthhorilineinregion2file,
        filledcircle2file,
        filledrect2file,
        filledgradrect2file,
        filleddichromaticgradrect2file,
        fliphoricircregion2file,
        fliphorizontal2file,
        flipvertical2file,
        fliphorizontalregion2file,
        flipvertcircregion2file,
        flipverticalregion2file,
        flipXY2file,
        flipXYcircregion2file,
        gammaadj2file,
        gammaadjtoregion2file,
        gammacorrectcircregion2file,
        getcolorname2RGBdict,
        getRGBfactors,
        horibrightnessgrad2circregion2file,
        horizontalbrightnessgrad2file,
        horizontalbrightnessgradregion2file,
        imgregionbyRGB2file,
        int2RGB,
        invertbits2file,
        invertbitsincircregion2file,
        invertregion2file,
        loadBMP,
        magnifyNtimescircregion2file,
        mirrorbottom2file,
        mirrorbottomincircregion2file,
        mirrorbottominregion2file,
        mirrorbottomleft2file,
        mirrorbottomleftincircregion2file,
        mirrorbottomleftinregion2file,
        mirrorbottomright2file,
        mirrorbottomrightincircregion2file,
        mirrorbottomrightinregion2file,
        mirrorleft2file,
        mirrorleftincircregion2file,
        mirrorleftinregion2file,
        mirrorright2file,
        mirrorrightincircregion2file,
        mirrorrightinregion2file,
        mirrortop2file,
        mirrortopincircregion2file,
        mirrortopinregion2file,
        mirrortopleft2file,
        mirrortopleftincircregion2file,
        mirrortopleftinregion2file,
        mirrortopright2file,
        mirrortoprightincircregion2file,
        mirrortoprightinregion2file,
        monochrome2file,
        monochromecircregion2file,
        monofilterinregion2file,
        outline2file,
        outlinecircregion2file,
        outlineregion2file,
        pixelizenxncircregion2file,
        pixelizenxntofile,
        rectangle2file,
        reduce24bitimagebits,
        resizeNtimesbigger2file,
        resizeNtimessmaller2file,
        sphere2file,
        smoothsteplerp,
        thickencirclearea2file,
        thresholdadjcircregion2file,
        thresholdadjust2file,
        upgradeto24bitimage2file,
        vertbrightnessgrad2circregion2file,
        verticalbrightnessgrad2file,
        verticalbrightnessgradregion2file,
        getX11colorname2RGBdict
        )


rootdir = path.dirname(__file__)


class Test2filefunc(unittest.TestCase):

        testimgdir ='/assets/test_images/'
        sourcedir = rootdir + testimgdir
        outputdir = f'{rootdir}/test_output/'
        ofile = f'{sourcedir}raccoon.bmp'

        cf = getRGBfactors()
        c = getcolorname2RGBdict()
        c1 = getX11colorname2RGBdict()
        cwhite = c['white']
        cred = c['red']
        cyellow = c['yellow']
        cfcyan = cf['cyan']
        cfyellow = cf['yellow']


        def _filepaths(self, filename: str) -> list[str, str]:
                return (f'{self.outputdir}{filename}',
                        f'{self.sourcedir}{filename}')


        def filecmp(
                self,
                filename1: str,
                filename2: str):
                bmp1 = loadBMP(filename1)
                bmp2 = loadBMP(filename2)
                self.assertIsNotNone(bmp1)
                self.assertIsNotNone(bmp2)
                self.assertEqual(bmp1, bmp2)


        def dotestfullimg(self,
                filename: str, func: Callable):
                p = self._filepaths(filename)
                func(self.ofile, p[0])
                self.filecmp(*p)


        def dotestfullimgwithparam(
                self,
                filename: str,
                func: Callable,
                funcparam):
                p = self._filepaths(filename)
                func(self.ofile, p[0], funcparam)
                self.filecmp(*p)


        def dotestrectregion(
                self,
                filename: str,
                func: Callable,
                x1: int, y1: int,
                x2: int, y2: int):
                p = self._filepaths(filename)
                func(self.ofile, p[0], x1, y1, x2, y2)
                self.filecmp(*p)


        def dotestrectregionwithparam(
                self,
                filename: str,
                func: Callable,
                x1: int, y1: int,
                x2: int, y2: int,
                *funcparam):
                p = self._filepaths(filename)
                func(self.ofile, p[0],
                        x1, y1, x2, y2, *funcparam)
                self.filecmp(*p)


        def dotestcircregion(
                self,
                filename: str,
                func: Callable,
                x: int, y:int, r:int):
                p = self._filepaths(filename)
                func(self.ofile, p[0], x, y, r)
                self.filecmp(*p)


        def dotestcircregionwithparam(
                self,
                filename: str,
                func: Callable,
                x: int, y: int, r: int,
                funcparam):
                p = self._filepaths(filename)
                func(self.ofile, p[0],
                     x, y, r, funcparam)
                self.filecmp(*p)


        def dotestcircregionwith2param(
                self,
                filename: str,
                func: Callable,
                x: int, y: int, r: int,
                funcparam1, funcparam2):
                p = self._filepaths(filename)
                func(self.ofile, p[0],
                     x, y, r, funcparam1, funcparam2)
                self.filecmp(*p)



        def testmirrortop2file(self):
                self.dotestfullimg(
                        'raccoon-mirrortop.bmp',
                        mirrortop2file)


        def testmirrorbottom2file(self):
                self.dotestfullimg(
                        'raccoon-mirrorbottom.bmp',
                        mirrorbottom2file)


        def testmirrorleft2file(self):
                self.dotestfullimg(
                        'raccoon-mirrorleft.bmp',
                        mirrorleft2file)


        def testmirrorright2file(self):
                self.dotestfullimg(
                        'raccoon-mirrorright.bmp',
                        mirrorright2file)


        def testmirrortopleft2file(self):
                self.dotestfullimg(
                        'raccoon-mirrortopleft.bmp',
                        mirrortopleft2file)


        def testmirrortopright2file(self):
                self.dotestfullimg(
                        'raccoon-mirrortopright.bmp',
                        mirrortopright2file)


        def testmirrorbottomleft2file(self):
                self.dotestfullimg(
                        'raccoon-mirrorbottomleft.bmp',
                        mirrorbottomleft2file)


        def testmirrorbottomright2file(self):
                self.dotestfullimg(
                        'raccoon-mirrorbottomright.bmp',
                        mirrorbottomright2file)


        def testmonochrome2file(self):
                self.dotestfullimg(
                        'raccoon-monochrome.bmp',
                        monochrome2file)


        def testoutline2file(self):
                self.dotestfullimg(
                        'raccoon-outline.bmp',
                        outline2file)


        def testflipXY2file(self):
                self.dotestfullimg(
                        'raccoon-flipXY.bmp',
                        flipXY2file)


        def testfliphorizontal2file(self):
                self.dotestfullimg(
                        'raccoon-fliphorizontal.bmp',
                        fliphorizontal2file)


        def testflipvertical2file(self):
                self.dotestfullimg(
                        'raccoon-flipvertical.bmp',
                        flipvertical2file)


        def testinvertbits2file(self):
                self.dotestfullimg(
                        'raccoon-invertbits.bmp',
                        invertbits2file)


        def testflipverticalregion2file(self):
                self.dotestrectregion(
                        'raccoon-flipverticalregion.bmp',
                        flipverticalregion2file,
                        250, 60, 860, 666)


        def testoutlineregion2file(self):
                self.dotestrectregion(
                        'raccoon-outlineregion.bmp',
                        outlineregion2file,
                        250, 60, 860, 666)


        def testinvertregion2file(self):
                self.dotestrectregion(
                        'raccoon-inv-reg.bmp',
                        invertregion2file,
                        250, 60, 860, 666)


        def testfliphorizontalregion2file(self):
                self.dotestrectregion(
                        'raccoon-fliphorizontalregion.bmp',
                        fliphorizontalregion2file,
                        250, 60, 860, 666)


        def testcropBMPandsave(self):
                self.dotestrectregion(
                        'raccoon-cropregion.bmp',
                        cropBMPandsave,
                        250, 60, 860, 666)


        def testmonofilterinregion2file(self):
                self.dotestrectregion(
                        'raccoon-monofilterinregion.bmp',
                        monofilterinregion2file,
                        250, 60, 860, 666)


        def testmirrorrightinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrorrightinregion.bmp',
                        mirrorrightinregion2file,
                        250, 60, 860, 666)


        def testmirrorleftinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrorleftinregion.bmp',
                        mirrorleftinregion2file,
                        250, 60, 860, 666)


        def testmirrortopinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrortopinregion.bmp',
                        mirrortopinregion2file,
                        250, 60, 860, 666)


        def testmirrorbottominregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrorbottominregion.bmp',
                        mirrorbottominregion2file,
                        250, 60, 860, 666)


        def testmirrortopleftinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrortopleftinregion.bmp',
                        mirrortopleftinregion2file,
                        250, 60, 860, 666)


        def testmirrortoprightinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrortoprightinregion.bmp',
                        mirrortoprightinregion2file,
                        250, 60, 860, 666)


        def testmirrorbottomleftinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrorbottomleftinregion.bmp',
                        mirrorbottomleftinregion2file,
                        250, 60, 860, 666)


        def testmirrorbottomrightinregion2file(self):
                self.dotestrectregion(
                        'raccoon-mirrorbottomrightinregion.bmp',
                        mirrorbottomrightinregion2file,
                        250, 60, 860, 666)


        def testeraseeverynthhoriline2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-eraseeverynthhoriline.bmp',
                        eraseeverynthhoriline2file, 3)


        def testpixelizenxn2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-pixelizenx.bmp',
                        pixelizenxntofile, 15)


        def testthresholdadjust2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-thresholdadjust.bmp',
                        thresholdadjust2file, [24, 192])


        def testgammaadj2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-gammaadj.bmp',
                        gammaadj2file, .45)


        def testverticalbrightnessgrad2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-verticalbrightnessgrad.bmp',
                        verticalbrightnessgrad2file,
                        [200, -100])


        def testhorizontalbrightnessgrad2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-horizontalbrightnessgrad.bmp',
                        horizontalbrightnessgrad2file,
                        [200, -100])


        def testcolorfilter2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-cyanfilter.bmp',
                        colorfilter2file, self.cfcyan)


        def testadjustbrightness2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-adjustbrightness.bmp',
                        adjustbrightness2file, 200)


        def testresizeNtimessmaller2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-8timessmall.bmp',
                        resizeNtimessmaller2file, 8)


        def testresizeNtimesbigger2file(self):
                self.dotestfullimgwithparam(
                        'raccoon-3timebigger.bmp',
                        resizeNtimesbigger2file, 3)


        def testadjustbrightnessinregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-adjustbrightnessinregion.bmp',
                        adjustbrightnessinregion2file,
                        250, 60, 860, 666, 150)


        def testrectangle2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-rectangle.bmp',
                        rectangle2file,
                        250, 60, 860, 666, self.cred)


        def testfilledrect2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-filledrectangle.bmp',
                        filledrect2file,
                        250, 60, 860, 666, self.cyellow)


        def testfilledgradrect2file0(self):
                self.dotestrectregionwithparam(
                        'raccoon-filledgradrectangle0.bmp',
                        filledgradrect2file,
                        250, 60, 860, 666, [255, 0], self.cfyellow, 0)


        def testfilledgradrect2file0smoothstep(self):
                self.dotestrectregionwithparam(
                        'raccoon-filledgradrectangle0smoothstep.bmp',
                        filledgradrect2file,
                        250, 60, 860, 666, [255, 0], self.cfyellow, 0, smoothsteplerp)


        def testfilledgradrect2file1(self):
                self.dotestrectregionwithparam(
                        'raccoon-filledgradrectangle1.bmp',
                        filledgradrect2file,
                        250, 60, 860, 666, [255, 0], self.cfyellow, 1)


        def testfilledgradrect2file1smoothstep(self):
                self.dotestrectregionwithparam(
                        'raccoon-filledgradrectangle1smoothstep.bmp',
                        filledgradrect2file,
                        250, 60, 860, 666, [255, 0], self.cfyellow, 1, smoothsteplerp)


        def testfilleddichromaticgradrect2file0(self):
                self.dotestrectregionwithparam(
                        'raccoon-filleddichromaticgradrectangle0.bmp',
                        filleddichromaticgradrect2file,
                        250, 60, 860, 666, self.cred, self.cyellow, 0)


        def testfilleddichromaticgradrect2file1(self):
                self.dotestrectregionwithparam(
                        'raccoon-filleddichromaticgradrectangle1.bmp',
                        filleddichromaticgradrect2file,
                        250, 60, 860, 666, self.cred, self.cyellow, 1)




        def testfilleddichromaticgradrect2file0(self):
                self.dotestrectregionwithparam(
                        'raccoon-filleddichromaticgradrectangle0smoothstep.bmp',
                        filleddichromaticgradrect2file,
                        250, 60, 860, 666, self.cred, self.cyellow, 0, smoothsteplerp)


        def testfilleddichromaticgradrect2file1(self):
                self.dotestrectregionwithparam(
                        'raccoon-filleddichromaticgradrectangle1smoothstep.bmp',
                        filleddichromaticgradrect2file,
                        250, 60, 860, 666, self.cred, self.cyellow, 1, smoothsteplerp)


        def testcolorfilterinregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-cyanfilteregion.bmp',
                        colorfilterinregion2file,
                        250, 60, 860, 666, self.cfcyan)


        def testhorizontalbrightnessgradregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-horizontalbrightnessgradregion.bmp',
                        horizontalbrightnessgradregion2file,
                        250, 60, 860, 666, [200,-80])


        def testeraseeverynthhorilineinregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-eraseeverynthhorilineinregion.bmp',
                        eraseeverynthhorilineinregion2file,
                        250, 60, 860, 666, 3)


        def testadjustthresholdinregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-adjustthresholdinregion.bmp',
                        adjustthresholdinregion2file,
                        250, 60, 860, 666, [24, 160])


        def testgammaadjtoregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-gammaadjtoregion.bmp',
                        gammaadjtoregion2file,
                        250, 60, 860, 666, .45)


        def testinvertbitsincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-invertbitsincircregion.bmp',
                        invertbitsincircregion2file,
                        500, 300, 400)


        def testflipvertcircregion2file(self):
                self.dotestcircregion(
                        'raccoon-flipvertcircregion.bmp',
                        flipvertcircregion2file,
                        500, 300, 300)


        def testfliphoricircregion2file(self):
                self.dotestcircregion(
                        'raccoon-fliphoricircregion.bmp',
                        fliphoricircregion2file,
                        500, 300, 300)


        def testoutlinecircregion2file(self):
                self.dotestcircregion(
                        'raccoon-outlinecircregion.bmp',
                        outlinecircregion2file,
                        500, 360, 400)


        def testflipXYcircregion2file(self):
                self.dotestcircregion(
                        'raccoon-flipXYcircregion.bmp',
                        flipXYcircregion2file,
                        500, 300, 300)


        def testmonochromecircregion2file(self):
                self.dotestcircregion(
                        'raccoon-monochromecircregion.bmp',
                        monochromecircregion2file,
                        500, 300, 300)


        def testcolorfiltercircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-yellowcircregion.bmp',
                        colorfiltercircregion2file,
                        500, 300, 300, self.cfyellow)


        def testcircle2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-thinredcircle.bmp',
                        circle2file,
                        500, 300, 280, self.cred)

        def testthresholdadjcircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-thresholdadjcircregion.bmp',
                        thresholdadjcircregion2file,
                        500, 400, 250, [32, 152])


        def testgammacorrectcircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-gammacorrectcircregion.bmp',
                        gammacorrectcircregion2file,
                        500, 300, 280, .45)


        def testbrightnessadjcircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-brightnessadjcircregion.bmp',
                        brightnessadjcircregion2file,
                        500, 300, 290, 80)


        def testmagnifyNtimescircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-magnify2timescircregion.bmp',
                        magnifyNtimescircregion2file,
                        500, 300, 300, 2)


        def testcopycircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-copycircregion.bmp',
                        copycircregion2file,
                        500, 300, 200, [240, 400])


        def testvertbrightnessgrad2circregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-vertbrightnessgrad2circregion.bmp',
                        vertbrightnessgrad2circregion2file,
                        500, 350, 250,[200, -100])


        def testhoribrightnessgrad2circregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-horibrightnessgrad2circregion.bmp',
                        horibrightnessgrad2circregion2file,
                        500, 300, 300, [200, -100])


        def testeraseeverynthhorilineinccircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-eraseeverynthhorilineinccircregion.bmp',
                        eraseeverynthhorilineinccircregion2file,
                        500, 300, 300, 3)


        def testpixelizenxncircregion2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-pixelizenxncircregion.bmp',
                        pixelizenxncircregion2file,
                        500, 300, 300, 9)


        def testsphere2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-sphere.bmp',
                        sphere2file,
                        120, 170, 100, self.cfcyan)


        def testdichromicsphere2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-spheredichromic.bmp',
                        sphere2file,
                        120, 170, 100, [self.cyellow, self.cred])


        def testsphere2file(self):
                self.dotestcircregionwith2param(
                        'raccoon-spheresmoothstep.bmp',
                        sphere2file,
                        120, 170, 100, self.cfcyan, smoothsteplerp)


        def testdichromicsphere2file(self):
                self.dotestcircregionwith2param(
                        'raccoon-spheredichromicsmoothstep.bmp',
                        sphere2file,
                        120, 170, 100, [self.cyellow, self.cred], smoothsteplerp)



        def testthickencirclearea2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-thickencirclearea.bmp',
                        thickencirclearea2file,
                        500, 300, 280, self.cfyellow)


        def testfilledcircle2file(self):
                self.dotestcircregionwithparam(
                        'raccoon-filledcircle.bmp',
                        filledcircle2file,
                        120, 170, 100, self.cyellow)


        def testmirrortopincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrortopincircregion.bmp',
                        mirrortopincircregion2file,
                        500, 300, 300)


        def testmirrorbottomincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrorbottomincircregion.bmp',
                        mirrorbottomincircregion2file,
                        500, 300, 300)


        def testmirrorleftincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrorleftincircregion.bmp',
                        mirrorleftincircregion2file,
                        500, 300, 300)


        def testmirrorrightincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrorrightincircregion.bmp',
                        mirrorrightincircregion2file,
                        500, 300, 300)


        def testmirrortopleftincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrortopleftincircregion.bmp',
                        mirrortopleftincircregion2file,
                        500, 300, 300)


        def testmirrorbottomleftincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrorbottomleftincircregion.bmp',
                        mirrorbottomleftincircregion2file,
                        500, 300, 300)


        def testmirrortoprightincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrortoprightincircregion.bmp',
                        mirrortoprightincircregion2file,
                        500, 300, 300)


        def testmirrorbottomrightincircregion2file(self):
                self.dotestcircregion(
                        'raccoon-mirrorbottomrightincircregion.bmp',
                        mirrorbottomrightincircregion2file,
                        500, 300, 300)


        def testimgregionbyRGB2file(self):
                colorstr = 'gray'
                color = self.c1[colorstr]
                p = self._filepaths(f'tanuki-edgebycolor{colorstr}.bmp')
                imgregionbyRGB2file(
                        f'{self.sourcedir}tanuki.bmp',
                        p[0], 1, color,
                        int2RGB(color),
                        120, True)
                self.filecmp(*p)


        def testreduce24bitimagebits(self):
                p = self._filepaths('earth-4bit.bmp')
                reduce24bitimagebits(
                        f'{self.sourcedir}earth.bmp',
                        p[0], 4, 24, False)
                self.filecmp(*p)


        def testadjustbrightness4bit2file(self):
                p = self._filepaths('earth-4bitbrightadj.bmp')
                adjustbrightness2file(f'{self.sourcedir}earth-4bit.bmp',
                        p[0], 200)
                self.filecmp(*p)


        def testgammaadjust4bit2file(self):
                p = self._filepaths('earth-4bitgammaadj.bmp')
                gammaadj2file(f'{self.sourcedir}earth-4bit.bmp',
                        p[0], .5)
                self.filecmp(*p)


        def testcolorfilter4bit2file(self):
                p = self._filepaths('earth-4bitcolorfilter.bmp')
                colorfilter2file(f'{self.sourcedir}earth-4bit.bmp',
                        p[0], self.cf["green"])
                self.filecmp(*p)


        def testmonofilter4bit2file(self):
                p = self._filepaths('earth-4bitmono.bmp')
                monochrome2file(f'{self.sourcedir}earth-4bit.bmp',
                        p[0])
                self.filecmp(*p)


        def testthresholdadj4bit2file(self):
                p = self._filepaths('earth-4bitthresholdadj.bmp')
                thresholdadjust2file(f'{self.sourcedir}earth-4bit.bmp',
                        p[0], [64, 200])
                self.filecmp(*p)


        def testupgradeto24bitimage(self):
                p = self._filepaths('earth-4bit-to-24bit.bmp')
                upgradeto24bitimage2file(
                        f'{self.sourcedir}earth-4bit.bmp',
                        p[0])
                self.filecmp(*p)


        def testautocropimg2file(self):
                p = self._filepaths('flower-autocrop.bmp')
                autocropimg2file(f'{self.sourcedir}flower.bmp',
                                 p[0], 64)
                self.filecmp(*p)


        def testbrightnessgradregion2file(self):
                self.dotestrectregionwithparam(
                        'raccoon-verticalbrightnessgradregion.bmp',
                        verticalbrightnessgradregion2file,
                        250, 60, 860, 666, [-100, 200])


if __name__ == "__main__":
        print(notice)
        print('Root directory is: ',rootdir)
        unittest.main()


notice = """
 Unit tests for fractals
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
import filecmp
import unittest
from os import path
from Python_BMP.BITMAPlib import(
        loadBMP,
        savemandelbrotfractal2file as mandel,
        savemultibrotfractal2file as multibrot,
        savejuliafractal2file as julia,
        savemultijuliafractal2file as multijulia,
        savetricornfractal2file as tricorn,
        savemulticornfractal2file as multicorn,
        savenewtonsfractal2file as newton,
        funcparamdict,
        getX11RGBfactors,
        fractaldomainparamdict,
        savehilbertcurve2file as hilbert,
        savekochsnowflake2file as koch
        )


rootdir = path.dirname(__file__)


class TestFractal2filefunc(unittest.TestCase):

    testimgdir = '/assets/fractals/'
    sdir = rootdir + testimgdir
    odir = f'{rootdir}/test_output/'
    c = getX11RGBfactors()
    d = fractaldomainparamdict()['maxeqdim']
    imag = -0.70176 - 0.3842j


    def filecmp(self, file: str):
        bmp1 = loadBMP(f'{self.odir}{file}')
        bmp2 = loadBMP(f'{self.sdir}{file}')
        self.assertIsNotNone(bmp1)
        self.assertIsNotNone(bmp2)
        self.assertEqual(bmp1, bmp2)


    def testsavemandelbrotfractal2file(self):
        file = "mandelbrot.bmp"
        mandel(f'{self.odir}{file}', 600, 600,
        self.d, self.c['deepskyblue'])
        self.filecmp(file)


    def testsavemultibrotfractal2file(self):
        file = "multibrot.bmp"
        multibrot(f'{self.odir}{file}', 600, 600,
        5, self.d, self.c['cornflowerblue'])
        self.filecmp(file)


    def testsavejuliafractal2file(self):
        file = "julia.bmp"
        julia(f'{self.odir}{file}', 600, 600,
        self.imag, # complex number
        self.d, self.c['darkslategray1'])
        self.filecmp(file)


    def testsavemultijuliafractal2file(self):
        file = "multijulia.bmp"
        multijulia(f'{self.odir}{file}', 600, 600,
        self.imag, # complex nunber
        5, self.d, self.c['darkseagreen1'])
        self.filecmp(file)


    def testsavetricornfractal2file(self):
        file = "tricorn.bmp"
        tricorn(f'{self.odir}{file}', 600, 600,
        self.d, self.c['springgreen'])
        self.filecmp(file)


    def testsavemulticornfractal2file(self):
        file = "multicorn.bmp"
        multicorn(f'{self.odir}{file}', 600, 600,
        5, self.d, self.c['aquamarine'])
        self.filecmp(file)


    def testsavenewtonsfractal2file(self):
        file = "newtons.bmp"
        newton(f'{self.odir}{file}', 600, 600,
        funcparamdict()[3], self.d,
        (self.c['red'], self.c['green'], self.c['blue']))
        self.filecmp(file)


    def testmonohilbert6thorder(self):
        file = "hilbert6.bmp"
        hilbert(f'{self.odir}{file}', 512, 512, 6)
        self.filecmp(file)


    def test16colorhilber4thorder(self):
        file = "hilbert4.bmp"
        hilbert(f'{self.odir}{file}', 512, 512,
        4, 4, 15, 2, 5, 1)
        self.filecmp(file)


    def testkoch4thorder(self):
        file = "koch4.bmp"
        koch(f'{self.odir}{file}', 250, 4, 0, 4, 15, 2)
        self.filecmp(file)


    def testkoch3rdorderthick(self):
        file = "koch3.bmp"
        koch(f'{self.odir}{file}', 250, 3, 0, 4, 15, 2, 6)
        self.filecmp(file)

#koch(f'{odir}{file}', 250, 3)

if __name__ == "__main__":
        print(notice)
        print('Root directory is: ',rootdir)
        unittest.main()


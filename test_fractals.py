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
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""
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
    sourcedir = rootdir + testimgdir
    outputdir = f'{rootdir}/test_output/'
    c = getX11RGBfactors()
    domain = fractaldomainparamdict()['maxeqdim']
    imag = -0.70176 - 0.3842j


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


    def testsavemandelbrotfractal2file(self):
        p = self._filepaths("mandelbrot.bmp")
        mandel(p[0], 256, 256,
        self.domain, self.c['deepskyblue'])
        self.filecmp(*p)


    def testsavemultibrotfractal2file(self):
        p = self._filepaths("multibrot.bmp")
        multibrot(p[0], 256, 256,
        5, self.domain, self.c['cornflowerblue'])
        self.filecmp(*p)


    def testsavejuliafractal2file(self):
        p = self._filepaths("julia.bmp")
        julia(p[0], 256, 256,
        self.imag, # complex number
        self.domain, self.c['darkslategray1'])
        self.filecmp(*p)


    def testsavemultijuliafractal2file(self):
        p = self._filepaths("multijulia.bmp")
        multijulia(p[0], 256, 256,
        self.imag, # complex nunber
        5, self.domain, self.c['darkseagreen1'])
        self.filecmp(*p)


    def testsavetricornfractal2file(self):
        p = self._filepaths("tricorn.bmp")
        tricorn(p[0], 256, 256,
        self.domain, self.c['springgreen'])
        self.filecmp(*p)


    def testsavemulticornfractal2file(self):
        p = self._filepaths("multicorn.bmp")
        multicorn(p[0], 256, 256,
        5, self.domain, self.c['aquamarine'])
        self.filecmp(*p)


    def testsavenewtonsfractal2file(self):
        p = self._filepaths("newtons.bmp")
        newton(p[0], 256, 256,
        funcparamdict()[3], self.domain,
        (self.c['red'], self.c['green'], self.c['blue']))
        self.filecmp(*p)


    def testmonohilbert6thorder(self):
        p = self._filepaths("hilbert6.bmp")
        hilbert(p[0], 512, 512, 6)
        self.filecmp(*p)


    def test16colorhilber4thorder(self):
        p = self._filepaths("hilbert4.bmp")
        hilbert(p[0], 512, 512,
        4, 4, 15, 2, 5, 1)
        self.filecmp(*p)


    def testkoch4thorder(self):
        p = self._filepaths("koch4.bmp")
        koch(p[0], 250, 4, 0, 4, 15, 2)
        self.filecmp(*p)


    def testkoch3rdorderthick(self):
        p = self._filepaths("koch3.bmp")
        koch(p[0], 123, 3, 0, 4, 15, 2, 3)
        self.filecmp(*p)



if __name__ == "__main__":
        print(notice)
        print('Root directory is: ',rootdir)
        unittest.main()


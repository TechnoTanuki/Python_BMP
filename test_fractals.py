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
        lambdafractal,
        loadBMP,
        multicircle,
        savebarnsleytreefractal2file as barnsleytree,
        savemandelbrotfractal2file as mandel,
        savemultibrotfractal2file as multibrot,
        savemulticirclefractal2file as multicircle,
        saveikedaattractor2file as ikedaattractor,
        savejuliafractal2file as julia,
        savelambdafractal2file as lambdafractal,
        savemultijuliafractal2file as multijulia,
        savespiraljulia2file as spiraljulia,
        savetricornfractal2file as tricorn,
        savemulticornfractal2file as multicorn,
        savenewtonsfractal2file as newton,
        savenattractor2file as nattractor,
        savexorfractal2file as xorfractal,
        savexordivfractal2file as xordivfractal,
        savegumowskimiraattractor2file as gumowskimiraattractor,
        savemultibiomorphfractal2file as biomorph,
        savemultisinbiomorphfractal2file as sinbiomorph,
        savemulticosbiomorphfractal2file as cosbiomorph,
        savemultitanbiomorphfractal2file as tanbiomorph,
        savemultiexpbiomorphfractal2file as expbiomorph,
        savemultisinhbiomorphfractal2file as sinhbiomorph,
        savemultitanhbiomorphfractal2file as tanhbiomorph,
        savemultibiomorphvariantfractal2file as biomorphvariant,
        savengonfractal2file as ngonfractal,
        savesinjulia2file as sinjulia,
        savecosjulia2file as cosjulia,
        savetetrationfractal2file as tetration,
        savemarekdragon2file as marekdragon,
        funcparamdict,
        getX11RGBfactors,
        fractaldomainparamdict,
        savehilbertcurve2file as hilbert,
        savekochsnowflake2file as koch,
        savepeterdejongattractor2file as peterdejong,
        savecliffordattractor2file as clifford,
        savehopalongattractor2file as hopalong,
        savefractaldreamattractor2file as fractaldream,
        savesymmetriciconattractor2file as symicon
        )


rootdir = path.dirname(__file__)


class TestFractal2filefunc(unittest.TestCase):

    testimgdir = '/assets/fractals/'
    sourcedir = rootdir + testimgdir
    outputdir = f'{rootdir}/test_output/'
    c = getX11RGBfactors()
    domain = fractaldomainparamdict()['maxeqdim']
    imag = -0.70176 - 0.3842j
    fdict = funcparamdict()

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


    def testsavemulticirclefractal2file(self):
        p = self._filepaths("multicircle.bmp")
        multicircle(p[0], 256, 256,
        2.5, [-20, 20, -20, 20], self.c['royalblue'])
        self.filecmp(*p)


    def testsavejuliafractal2file(self):
        p = self._filepaths("julia.bmp")
        julia(p[0], 256, 256,
        self.imag, # complex number
        self.domain, self.c['darkslategray1'])
        self.filecmp(*p)


    def testsavespiralfractal2file(self):
        p = self._filepaths("spiraljulia.bmp")
        spiraljulia(p[0], 256, 256,
        2.2 + 0.33j, # complex number
        self.domain, self.c['greenyellow'])
        self.filecmp(*p)


    def testsavelambdafractal2file(self):
        p = self._filepaths("lambda.bmp")
        lambdafractal(p[0], 256, 256,
        0.85 - 0.6j, # complex number
        [-.5, .5, -.5, .5], self.c['gold'])
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


    def testsavebarnsleytreefractal2file(self):
        p = self._filepaths("barnsleytree.bmp")
        barnsleytree(p[0], 256, 256,
          0.6 + 1.1j, # complex number
          [-1.5, 1.5, -1.5, 1.5], # location to plot
          self.c['yellowgreen'])
        self.filecmp(*p)


    def testsavexorfractal2file(self):
        p = self._filepaths("xor.bmp")
        xorfractal(p[0], 256, 256,
        97, [-200, 200, -200, 200], [], 8)
        self.filecmp(*p)


    def testsavexordivfractal2file(self):
        p = self._filepaths("xordiv.bmp")
        xordivfractal(p[0], 256, 256,
        13, [-200, 200, -200, 200], [], 8)
        self.filecmp(*p)


    def testsavenewtonsfractal2file(self):
        p = self._filepaths("newtons.bmp")
        newton(p[0], 256, 256,
        self.fdict[3], self.domain,
        (self.c['red'],
         self.c['green'],
         self.c['blue']))
        self.filecmp(*p)


    def testsavenewtonsfractal4file(self):
        p = self._filepaths("newtons4.bmp")
        newton(p[0], 256, 256,
        self.fdict[4], self.domain,
        (self.c['red'],
         self.c['yellow'],
         self.c['green'],
         self.c['blue']))
        self.filecmp(*p)


    def testmonohilbert6thorder(self):
        p = self._filepaths("hilbert6.bmp")
        hilbert(p[0], 256, 256, 6)
        self.filecmp(*p)


    def test16colorhilber4thorder(self):
        p = self._filepaths("hilbert4.bmp")
        hilbert(p[0], 256, 256,
        4, 4, 15, 2, 3, 1)
        self.filecmp(*p)


    def testkoch4thorder(self):
        p = self._filepaths("koch4.bmp")
        koch(p[0], 250, 4, 0, 4, 15, 2)
        self.filecmp(*p)


    def testkoch3rdorderthick(self):
        p = self._filepaths("koch3.bmp")
        koch(p[0], 123, 3, 0, 4, 15, 2, 3)
        self.filecmp(*p)


    def testikedaattractor(self):
        p = self._filepaths("ikedaattractor.bmp")
        ikedaattractor(p[0], # path to new file
        256, 256, # size of file x, y
        24, # bit depth
        0.85, 0.9, 0.4, 7.7, # constants (float)
        100000 # number of iterations
        )
        self.filecmp(*p)


    def testnattractor(self):
        p = self._filepaths("nattractor.bmp")
        nattractor(p[0], # path to new file
        256, 256, # size of file x, y
        24, # bit depth
         1.641, -1.902, 1.316, 1.525,# constants (float)
        50000 # number of iterations
        )
        self.filecmp(*p)

    def testgumowskimiraattractor(self):
        p = self._filepaths("gumowskimiraattractor.bmp")
        gumowskimiraattractor(p[0], # path to new file
        256, 256, # size of file
        24, # bit depth
        1, .34, .34, 1,# constants (float)
        50000 # number of iterations
        )
        self.filecmp(*p)


    def testbiomorphvariant(self):
        p = self._filepaths("biomorphvariant.bmp")
        biomorphvariant(p[0], 256, 256, # file and bitmap size
        1 + 1j, # complex number
        5, # power of z
        self.domain, # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testbiomorph(self):
        p = self._filepaths("biomorph.bmp")
        biomorph(p[0], 256, 256, # file and bitmap size
        1 + 1j, # complex nunber
        5, # power of z
        [-2.5, 2.5, -2.5, 2.5], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testsinbiomorph(self):
        p = self._filepaths("sinbiomorph.bmp")
        sinbiomorph(p[0], 256, 256, # file and bitmap size
        .8 + .9j, # complex number
        2, # power of z
        [-5, 5, -5, 5], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testcosbiomorph(self):
        p = self._filepaths("cosbiomorph.bmp")
        cosbiomorph(p[0], 256, 256, # file and bitmap size
        .4 + .9j, # complex number
        3, # power of z
        [-1.7, 1.7, -1.7, 1.7], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testsinhbiomorph(self):
        p = self._filepaths("sinhbiomorph.bmp")
        sinhbiomorph(p[0], 256, 256, # file and bitmap size
        .8 + .9j, # complex number
        5, # power of z
        [-1.25, 1.25, -1.25, 1.25], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testexpbiomorph(self):
        p = self._filepaths("expbiomorph.bmp")
        expbiomorph(p[0], 256, 256, # file and bitmap size
        .1 + .9j, # complex number
        5, # power of z
        [-2, 2, -2, 2], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testtanbiomorph(self):
        p = self._filepaths("tanbiomorph.bmp")
        tanbiomorph(p[0], 256, 256, # file and bitmap size
        .8 + .9j, # complex number
        3, # power of z
        [-2.5, 2.5, -2.5, 2.5], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testtanhbiomorph(self):
        p = self._filepaths("tanhbiomorph.bmp")
        tanhbiomorph(p[0], 256, 256, # file and bitmap size
        .3 + .8j, # complex number
        3, # power of z
        [-1.9, 1.9, -1.9, 1.9], # location to plot
        self.c['darkseagreen1']) # color
        self.filecmp(*p)


    def testngonfractal(self):
        p = self._filepaths("ngonfractal.bmp")
        ngonfractal(p[0], 256, 256, # file and bitmap size
          -(1.7/5), # float pararm
          7, # sides
          [-1.2, 1.2, -1.2, 1.2], # location to plot
          self.c['yellowgreen']) # color
        self.filecmp(*p)


    def testsinjuliafractal(self):
        p = self._filepaths("sinjulia.bmp")
        sinjulia(p[0], # path to new file
        256, 256, # size of file
        1 + 1j, # complex number
        self.domain, # fractal domain
        self.c['gold']) # color
        self.filecmp(*p)


    def testcosjuliafractal(self):
        p = self._filepaths("cosjulia.bmp")
        cosjulia(p[0], # path to new file
        256, 256, # size of file
        1 + 1j, # complex number
        self.domain, # fractal domain
        self.c['aqua']) # color
        self.filecmp(*p)


    def testtetrationfractal(self):
        p = self._filepaths("tetration.bmp")
        tetration(p[0], 256, 256, 16,
        [1, 2.5, -.75, .75], [], 4)
        self.filecmp(*p)


    def testmarekdragon(self):
        p = self._filepaths("marekdragon.bmp")
        marekdragon(p[0], 256, 256, 0.040884634,
        [-1.5, .5, -1.25, 1], self.c['yellowgreen'])
        self.filecmp(*p)


    def testpeterdejong(self):
        p = self._filepaths("peterdejong.bmp")
        peterdejong(p[0], 256, 256, # size of file
        24, # bit depth
        1.641, 1.902, .316, 1.525,# constants (float)
        220000 # number of iterations
        )
        self.filecmp(*p)


    def testcliford(self):
        p = self._filepaths("cliffordattractor.bmp")
        clifford(p[0], # path to new file
        256, 256, # size of file
        24, # bit depth
        -1.7, 1.3, -.1, -1.2, # constants (float)
        80060 # number of iterations
        )
        self.filecmp(*p)


    def testhopalong(self):
        p = self._filepaths("hopalongattractor.bmp")
        hopalong(p[0], # path to new file
        256, 256, # size of file
        24, # bit depth
        1.441, 1.802, -.316,# constants (float)
        500000 # number of iterations
        )
        self.filecmp(*p)


    def testfractaldreamattractor(self):
        p = self._filepaths("fractaldreamattractor.bmp")
        fractaldream(p[0], # path to new file
        256, 256, # size of file
        24, # bit depth
        -0.966918, 2.879879, 0.765145, 0.744728, # constants (float)
        88800 # number of iterations
        )
        self.filecmp(*p)


    def testsymmetriciconattractor(self):
        p = self._filepaths("symmetriciconattractor.bmp")
        symicon(p[0], # path to new file
        256, 256, # size of file
        24, # bit depth
        0.01, 0.01, 1.0, -0.1, 0.167, 0.0, -2.08,# constants (float)
        7, # degree int
        30100 # number of iterations
        )
        self.filecmp(*p)


if __name__ == "__main__":
        print(notice)
        print('Root directory is: ',rootdir)
        unittest.main()


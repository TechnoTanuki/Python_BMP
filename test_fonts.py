notice = """
 Unit tests for fonts
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
from array import array
from typing import Callable
import unittest
from os import path
from Python_BMP.BITMAPlib import(
        loadBMP,
        plotstring2file,
        plotstringasdots2file,
        plotreversedstring2file,
        plotreversedstringasdots2file,
        plotupsidedownstring2file,
        plotupsidedownstringasdots2file,
        plotitalicstringasdots2file,
        plotitalicstring2file,
        plotreverseditalicstring2file,
        plotverticalstring2file,
        getX11colorname2RGBdict,
        getcolorname2RGBdict,
        font8x8,
        font8x14
        )


rootdir = path.dirname(__file__)


class TestFontfilefunc(unittest.TestCase):

    testimgdir = '/assets/fonts/'
    sourcedir = rootdir + testimgdir
    outputdir = f'{rootdir}/test_output/'
    c = getX11colorname2RGBdict()
    c1 = getcolorname2RGBdict()
    teststr = """abcdefghijklmnopqrs
tuvwxyz0123456789\'
":;.,?!~`@#$%^&()[]
{}_*+-/=<>ABCDEFGHI
JKLMNOPQRSTUVWXYZ"""
    rainbow = (c1['brightred'],
               c1['brightorange'],
               c1['brightyellow'],
               c1['brightgreen'],
               c1['cyan'],
               c1['brightblue'],
               c1['brightmagenta'])


    def genname(self,
                fn: Callable,
              font: array,
             color: int,
              size: int,
          pixspace: int,
  spacebetweenchar: int,
   backgroundcolor: int = 0,
              bits: int = 24) -> str:
        return f'8x{font[0]}x{size}px{pixspace}cs{spacebetweenchar}{bits}bit{fn.__name__}bc{backgroundcolor}c{color if type(color) == int else "multi"}'


    def dofontfunc(self,
                fn: Callable,
              font: array,
             color: int,
              size: int,
          pixspace: int,
  spacebetweenchar: int,
   backgroundcolor: int = 0,
              bits: int = 24):
        p = self._filepaths(f'{self.genname(fn, font, color, size, pixspace, spacebetweenchar, backgroundcolor, bits)}.bmp')
        fn(p[0], self.teststr, size, pixspace, spacebetweenchar,color, font, backgroundcolor, bits)
        self.filecmp(*p)


    def _filepaths(self, filename: str) -> list[str, str]:
            return (f'{self.outputdir}{filename}',
                    f'{self.sourcedir}{filename}')


    def filecmp(self, filename1: str,
                      filename2: str):
            bmp1 = loadBMP(filename1)
            bmp2 = loadBMP(filename2)
            self.assertIsNotNone(bmp1)
            self.assertIsNotNone(bmp2)
            self.assertEqual(bmp1, bmp2)

    aqua = c['aqua']
    darkolive = c['darkolivegreen1']
    orange = c['orange']
    green =  c['green']
    yellow = c['yellow']

    testcases = (
    #0
    (plotstring2file, font8x8, aqua, 1, 0, 0),
    #1
    (plotstring2file, font8x8, 1, 3, 0, 0, 0, 1),
    #2
    (plotstring2file, font8x8, aqua, 3, 1, 0),
    #3
    (plotstring2file, font8x14, darkolive, 1, 0, 0),
    #4
    (plotstring2file, font8x14, green, 3, 0, 0),
    #5
    (plotstring2file, font8x14, darkolive, 3, 1, 0),
    #6
    (plotitalicstring2file, font8x8, rainbow, 4, 1, 0),
    #7
    (plotreversedstring2file, font8x8, aqua, 1, 0, 0),
    #8
    (plotupsidedownstring2file, font8x8, aqua, 1, 0, 0),
    #9
    (plotstringasdots2file, font8x8, rainbow, 4, 1, 0),
    #10
    (plotstringasdots2file, font8x14, darkolive, 4, 1, 0),
    #11
    (plotreversedstringasdots2file, font8x14, darkolive, 4, 1, 0),
    #12
    (plotupsidedownstringasdots2file, font8x14, green, 3, 0, 0),
    #13
    (plotitalicstringasdots2file, font8x14, darkolive, 4, 1, 0),
    #14
    (plotreverseditalicstring2file, font8x14, yellow, 1, 0, 0),
    #15
    (plotverticalstring2file, font8x8, orange, 1, 0, 0),
    #16
    (plotverticalstring2file, font8x8, orange, 3, 1, 0)
    )

    def test0(self): self.dofontfunc(*self.testcases[0])
    def test1(self): self.dofontfunc(*self.testcases[1])
    def test2(self): self.dofontfunc(*self.testcases[2])
    def test3(self): self.dofontfunc(*self.testcases[3])
    def test4(self): self.dofontfunc(*self.testcases[4])
    def test5(self): self.dofontfunc(*self.testcases[5])
    def test6(self): self.dofontfunc(*self.testcases[6])
    def test7(self): self.dofontfunc(*self.testcases[7])
    def test8(self): self.dofontfunc(*self.testcases[8])
    def test9(self): self.dofontfunc(*self.testcases[9])
    def test10(self): self.dofontfunc(*self.testcases[10])
    def test11(self): self.dofontfunc(*self.testcases[11])
    def test12(self): self.dofontfunc(*self.testcases[12])
    def test13(self): self.dofontfunc(*self.testcases[13])
    def test14(self): self.dofontfunc(*self.testcases[14])
    def test15(self): self.dofontfunc(*self.testcases[15])
    def test16(self): self.dofontfunc(*self.testcases[16])

if __name__ == "__main__":
    print(notice)
    print('Root directory is: ',rootdir)
    unittest.main()


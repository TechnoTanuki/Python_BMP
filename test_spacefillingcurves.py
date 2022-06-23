notice = """
 Unit tests for space filling curves
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
        savehilbertcurve2file as hilbert,
        )


rootdir = path.dirname(__file__)
testimgdir = '/assets/fractals/'
sdir = rootdir + testimgdir
odir = f'{rootdir}/test_output/'

class Testspacefillingcurve2filefunc(unittest.TestCase):

        def filecmp(
                self,
                file:str):
                bmp1 = loadBMP(f'{odir}{file}')
                bmp2 = loadBMP(f'{sdir}{file}')
                self.assertIsNotNone(bmp1)
                self.assertIsNotNone(bmp2)
                self.assertEqual(bmp1, bmp2)


        def testmonohilbert6thorder(self):
            file = "hilbert6.bmp"
            hilbert(f'{odir}{file}', 512, 512, 6)
            self.filecmp(file)


        def test16colorhilber4thorder(self):
            file = "hilbert4.bmp"
            hilbert(f'{odir}{file}', 512, 512,
            4, 4, 15, 2, 5, 1)
            self.filecmp(file)


if __name__ == "__main__":
        print(notice)
        print('Root directory is: ',rootdir)
        unittest.main()


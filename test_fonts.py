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
        getX11colorname2RGBdict,
        getcolorname2RGBdict,
        font8x8,
        font8x14
        )


rootdir = path.dirname(__file__)


class TestFontfilefunc(unittest.TestCase):

    testimgdir = '/assets/fonts/'
    sdir = rootdir + testimgdir
    odir = f'{rootdir}/test_output/'
    c = getX11colorname2RGBdict()
    c1 = getcolorname2RGBdict()
    teststr = \
"""abcdefghijklmnopqrs
tuvwxyz0123456789\'
":;.,?!~`@#$%^&()[]
{}_*+-/=<>ABCDEFGHI
JKLMNOPQRSTUVWXYZ"""


    def filecmp(self, file: str):
        bmp1 = loadBMP(f'{self.odir}{file}')
        bmp2 = loadBMP(f'{self.sdir}{file}')
        self.assertIsNotNone(bmp1)
        self.assertIsNotNone(bmp2)
        self.assertEqual(bmp1, bmp2)


    def test8x14x1fontRGB(self):
        file = "8x14x1fontRGB.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 1, 0, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


    def test8x14x1fontRGB(self):
        file = "8x8x1font8bitRGB.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 1, 0, 0,
        self.c['aqua'], font8x8)
        self.filecmp(file)


    def test8x14x1upsidedownfontRGB(self):
        file = "8x8x1upsidedownfont8bitRGB.bmp"
        plotupsidedownstring2file(f'{self.odir}{file}',
        self.teststr, 1, 0, 0,
        self.c['aqua'], font8x8)
        self.filecmp(file)


    def test8x14x3fontRGB(self):
        file = "8x14x3fontRGB.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 3, 0, 0,
        self.c['green'], font8x14)
        self.filecmp(file)


    def test8x14x3fontasdotsRGB(self):
        file = "8x14x3fontasdotsRGB.bmp"
        plotstringasdots2file(f'{self.odir}{file}',
        self.teststr, 3, 0, 0,
        self.c['green'], font8x14)
        self.filecmp(file)


    def test8x14x3upsidedownfontasdotsRGB(self):
        file = "8x14x3upsidedownfontasdotsRGB.bmp"
        plotupsidedownstringasdots2file(f'{self.odir}{file}',
        self.teststr, 3, 0, 0,
        self.c['green'], font8x14)
        self.filecmp(file)


    def test8x8x3font1bit(self):
        file = "8x8x3font1bit.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 3, 0, 0,
        1, font8x8, 0, 1)
        self.filecmp(file)


    def test8x14xfontRGBpxspace1(self):
        file = "8x14x3fontRGBpixspace1.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 3, 1, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


    def test8x14x4fontRGBasdotspxspace1(self):
        file = "8x14x4fontRGBasdotspixspace1.bmp"
        plotstringasdots2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


    def test8x8x3fontpxspace1(self):
        file = "8x8x3fontRGBpxspace1.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 3, 1, 0,
        self.c['aqua'], font8x8)
        self.filecmp(file)


    def test8x8x4fontpxspace1rainbow(self):
        file = "8x8x4fontRGBpxspace1rainbow.bmp"
        plotstring2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        (self.c1['brightred'],
         self.c1['brightorange'],
         self.c1['brightyellow'],
         self.c1['brightgreen'],
         self.c1['cyan'],
         self.c1['brightblue'],
         self.c1['brightmagenta']),
        font8x8)
        self.filecmp(file)


    def test8x8x4reversedfontpxspace1rainbow(self):
        file = "8x8x4reversedfontRGBpxspace1rainbow.bmp"
        plotreversedstring2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        (self.c1['brightred'],
         self.c1['brightorange'],
         self.c1['brightyellow'],
         self.c1['brightgreen'],
         self.c1['cyan'],
         self.c1['brightblue'],
         self.c1['brightmagenta']),
        font8x8)
        self.filecmp(file)


    def test8x8x2reversedfontrainbow(self):
        file = "8x8x2reversedfontRGBrainbow.bmp"
        plotreversedstring2file(f'{self.odir}{file}',
        self.teststr, 2, 0, 0,
        (self.c1['brightred'],
         self.c1['brightorange'],
         self.c1['brightyellow'],
         self.c1['brightgreen'],
         self.c1['cyan'],
         self.c1['brightblue'],
         self.c1['brightmagenta']),
        font8x8)
        self.filecmp(file)


    def test8x8x4fontpxspace1asdotsrainbow(self):
        file = "8x8x4fontRGBpxspace1asdotsrainbow.bmp"
        plotstringasdots2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        (self.c1['brightred'],
         self.c1['brightorange'],
         self.c1['brightyellow'],
         self.c1['brightgreen'],
         self.c1['cyan'],
         self.c1['brightblue'],
         self.c1['brightmagenta']),
        font8x8)
        self.filecmp(file)


    def test8x14x4reversedfontRGBasdotspxspace1(self):
        file = "8x14x4reversedfontRGBasdotspixspace1.bmp"
        plotreversedstringasdots2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


    def test8x14x2italicfontRGB(self):
        file = "8x14x2italicfontRGB.bmp"
        plotitalicstring2file(f'{self.odir}{file}',
        self.teststr, 2, 0, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


    def test8x14x1italicfontRGB(self):
        file = "8x14x1italicfontRGB.bmp"
        plotitalicstring2file(f'{self.odir}{file}',
        self.teststr, 1, 0, 0,
        self.c['aqua'], font8x14)
        self.filecmp(file)


    def test8x14x4italicfontRGBpxspace1(self):
        file = "8x14x4italicfontRGBpxspace1.bmp"
        plotitalicstring2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


    def test8x14x4italicfontasdotsRGBpxspace1(self):
        file = "8x14x4italicfontasdotRGBpxspace1.bmp"
        plotitalicstringasdots2file(f'{self.odir}{file}',
        self.teststr, 4, 1, 0,
        self.c['darkolivegreen1'], font8x14)
        self.filecmp(file)


if __name__ == "__main__":
    print(notice)
    print('Root directory is: ',rootdir)
    unittest.main()


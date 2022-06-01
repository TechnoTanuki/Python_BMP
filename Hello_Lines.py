notice = """
          Hello Lines Demo
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""
from Python_BMP.BITMAPlib import(
        newBMP,
        bottomrightcoord,
        centercoord,
        line,
        saveBMP
)

import subprocess as proc
from os import path

def main():
        print(notice)
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        mx = my= 300 # bitmap size
        bmp = newBMP(mx,my,4) # 4 bit = 16 color
        (mx, my) = bottomrightcoord(bmp) #max-1 for screen
        (cx, cy) = centercoord(bmp) # How to get center of the bitmap
        #Python_BMP.BITMAPlib.line(bmp bytearray,x1 int,y1 int,x2 int, y2 int,color int) all unsigned
        line(bmp,0,0,mx,my,15)
        line(bmp,mx,0,0,my,14)
        line(bmp,0,0,mx,0,13)
        line(bmp,0,0,0,my,11)
        line(bmp,mx,my,mx,0,10)
        line(bmp,mx,my,0,my,9)
        line(bmp,cx,cy,cx,0,8)
        line(bmp,cx,cy,mx,cy,7)
        line(bmp,cx,cy,cx,my,6)
        line(bmp,cx,cy,0,cy,5)
        file = 'HelloLines.bmp' # file name
        saveBMP(file,bmp) # save file
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()


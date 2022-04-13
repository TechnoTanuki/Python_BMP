#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # Get directory of this script
        mx,my=75,75 # bitmap size
        bmp=b.newBMP(mx,my,4) # 4 bit = 16 color
        mx,my=mx-1,my-1 #max-1 for screen
        (cx,cy)=b.centercoord(bmp) # How to get center of the bitmap
        #Python_BMP.BITMAPlib.line(bmp bytearray,x1 int,y1 int,x2 int, y2 int,color int) all unsigned
        b.line(bmp,0,0,mx,my,15)
        b.line(bmp,mx,0,0,my,14)
        b.line(bmp,0,0,mx,0,13)
        b.line(bmp,0,0,0,my,11)
        b.line(bmp,mx,my,mx,0,10)
        b.line(bmp,mx,my,0,my,9)
        b.line(bmp,cx,cy,cx,0,8)
        b.line(bmp,cx,cy,mx,cy,7)
        b.line(bmp,cx,cy,cx,my,6)
        b.line(bmp,cx,cy,0,cy,5)
        file='HelloLines.bmp' # file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



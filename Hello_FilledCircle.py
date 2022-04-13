#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of running script
        mx=512 # bitmap size x
        my=mx # bitmap size y = x square bitmap
        bmp=b.newBMP(mx,my,4) # 4 bit = 16 color
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        r=x-12 # radius
        c=11 # color
        b.filledcircle(bmp,x,y,r,c)
        # Python_BMP.BITMAPlib.filledcircle(bmp bytearray,x int ,y int, r int, c int)
        file='HelloFilledCirle.bmp' # file name 
        b.saveBMP(file,bmp) # save file 
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



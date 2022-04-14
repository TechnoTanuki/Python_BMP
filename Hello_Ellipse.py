#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as bm,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get pathof this script
        bmp=bm.newBMP(300,200,4) # 16 color 80 x 50 bmp
        (x,y)=bm.centercoord(bmp) # How to get center of the bitmap
        b=y # b axis = y
        a=x # a axis = x
        color=13
        bm.ellipse(bmp,x,y,b,a,color) # all unsigned ints
        file='HelloEllipse.bmp' #file name
        bm.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

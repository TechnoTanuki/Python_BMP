#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as bm,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=bm.newBMP(300,200,24) # 300 x 200 24 bit bitmap
        (x,y)=bm.centercoord(bmp) # How to get center of the bitmap
        b=y-40 # b axis = y-40
        a=x-40 # a axis = x-40
        lumrange=(255,0) # decreasing gradient from center uint bytes
        rgbfactors=(.8,.4,1)  # rgb triplet as values 0 to 1 unsigned float
        penradius=20 # radius of pen in pixels
        degrot=30 # rotation of ellipse in degrees
        bm.gradthickellipserot(bmp,x,y,b,a,degrot,penradius,lumrange,rgbfactors)
        file='HelloThickGradientEllipseRotated.bmp' # file name
        bm.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()






#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        mx,my=250,250 # bitmap size
        bmp=b.newBMP(mx,my,4) # 4 bit = 2^4 = 16 bits
        file='HelloBspline.bmp' # file name
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        step=5 # pixel interval between spiral turn
        growthfactor=1 # greater than 1 means exponential spiral
        turns=13 # number of turns of spiral
        vertlist = b.spiralcontrolpointsvert(x,y,step,growthfactor,turns) # list of (x,y) control points
        penradius=2 # radius of pen
        color=11 
        isclosed=True # closed curve
        curveback=True # do extra computation to curve back to origin
        b.bspline(bmp,vertlist,penradius,color,isclosed,curveback)
        b.saveBMP(file,bmp) # save bitmap
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



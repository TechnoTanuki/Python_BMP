#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get script path
        mx,my=250,250 # bitmap size
        bmp=b.newBMP(mx,my,4) # 16 color
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        file='HelloSquareSpiral.bmp' # file name
        step=5 # pixel interval between spiral turn
        growthfactor=1 # greater than 1 means exponential spiral
        turns=13 # number of turns of spiral
        vertlist = b.spiralcontrolpointsvert(x,y,step,growthfactor,turns) # list of (x,y) control points
        color=9
        b.plotlines(bmp,vertlist,color) # connect the dots with lines
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



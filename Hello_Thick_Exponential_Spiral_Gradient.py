#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.newBMP(300,300,24) # RGB bitmap 300 x 300
        (x,y)=b.centercoord(bmp) # How to get center of the bitmap
        step=7 # growth increment of spiral
        growthfactor=1.61803399 # Golden Ratio... 
        turns=5 # number of turns of the spiral
        vertlist=b.spiralcontrolpointsvert(x,y,step,growthfactor,turns) # compute points of control points 
        isclosed=False # closed or open curve
        curveback=False # do extra compute to trace back to origin
        pts=b.bsplinevert(vertlist,isclosed,curveback) # compute points of bspline 
        penradius=5 # radius of pen in pixel
        lumrange=(255,0) # brightness decrease from center of pen to edge <ubytes>
        rgbfactors=(.9,.5,.9) # color as (r,g,b) values between 1 and 0 <ufloat>
        b.gradvert(bmp,pts,penradius,lumrange,rgbfactors) # render the spiral
        file='HelloThickExpGradSpiral.bmp' #file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

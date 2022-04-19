#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        x=250
        y=500
        bmp=b.newBMP(x,y,4) # 16 color
        color=10 # color info
        #IFS(bmp,b.getIFSparams()['fern'],x1,y1,x2,y2,xscale,yscale,xoffset,yoffset,color,maxiter)
        b.IFS(bmp,b.getIFSparams()['fern'],0,0,x,y,40,55,125,80,color,80000)
        file='fern.bmp'
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

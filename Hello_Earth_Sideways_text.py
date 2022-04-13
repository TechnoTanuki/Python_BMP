#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') # load earth to memory wow.., it fits
        c=b.getcolorname2RGBdict() #friendly color names 2 rgb
        x,y=150,150
        fontsize=2
        pixspace=1 # space between bitmap font pixels (0 = default)
        charspace=0 # space bitmap font characters (0 = default)
        b.plotstringsideway(bmp,x,y,'Hello!!!',fontsize,pixspace,charspace,c['brightyellow'],b.font8x14)
        file='HelloEarthSidewayText.bmp' #file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



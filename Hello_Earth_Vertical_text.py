#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        c=b.getcolorname2RGBdict() #friendly color names 2 rgb
        fontsize=2 # uint font size multiplier
        pixspace=0 # uint space between bitmap font pixels (0 = default)
        charspace=0 # unit space bitmap font characters (0 = default)
        x,y=125,5 # text anchor x,y uint
        b.plotstringvertical(bmp,x,y,'Hello',fontsize,pixspace,charspace,c['brightred'],b.font8x14)
        pixspace=1 # uint space between bitmap font pixels (0 = default)
        charspace=14 # unint space bitmap font characters (0 = default)
        x,y=150,10 # text anchor x,y uint
        b.plotstringvertical(bmp,x,y,'Earth',fontsize,pixspace,charspace,c['brightyellow'],b.font8x8)
        file='HelloEarthVertText.bmp' # file name
        b.saveBMP(file,bmp) # save bitmap  to file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

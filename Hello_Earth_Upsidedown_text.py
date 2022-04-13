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
        fontsize=4 # font size
        pixspace=1 # space between bitmap font pixels (0 = default)
        charspace=0 # space bitmap font characters (0 = default)
        b.plotstring(bmp,5,25,'Hello',fontsize,pixspace,charspace,c['brightred'],b.font8x14)
        b.plotstringupsidedown(bmp,5,85,'World',fontsize,pixspace,charspace,c['brightyellow'],b.font8x8)
        file='HelloEarthDownUpsidedowntext.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



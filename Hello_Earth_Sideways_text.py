#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        c=b.getcolorname2RGBdict() #friendly color names 2 rgb
        b.plotstringsideway(bmp,150,150,'Hello!!!',2,0,0,c['brightyellow'],b.font8x14)
        file='HelloEarthSidewayText.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



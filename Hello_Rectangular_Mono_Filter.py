#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get the path of this script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') # load earth to memory
        b.monofilterto24bitregion(bmp,30,30,138,138) # monofilterto24bitregion(bmp,x1,y1,x2,y2)
        file='HelloRectangularMonoFilter.bmp' # file name
        b.saveBMP(file,bmp) # save the modified earth image to a file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

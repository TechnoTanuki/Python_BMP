#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get script path
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        buf=b.copyrect(bmp,3,3,60,60) # copy a rectangular region (x1,y1,x2,y2) to a buffer
        b.pasterect(bmp,buf,40,40) # paste buffer to a rectangular region at (x1,y1)
        file='HelloEarthCopyPaste.bmp' #file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get script path
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        buff=b.copyrect(bmp,5,5,63,63) # copy rectagular region (x1,y1,x2,y2) uint to buff
        nbmp=b.convertselection2BMP(buff)# convert buffer to bitmap
        file='HelloSaveSelection.bmp' #file name
        b.saveBMP(file,nbmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



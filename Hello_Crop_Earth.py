#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get script path
        existingfile=rootdir+'/assets/earth.bmp'
        newfile='HelloEarthCopyPaste.bmp' #file name
        b.cropBMPandsave(existingfile,newfile,5,5,60,60) # crop a rectangular region (x1,y1,x2,y2) to a file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+newfile) # replace with another editor if Unix

if __name__=="__main__": 
        main()



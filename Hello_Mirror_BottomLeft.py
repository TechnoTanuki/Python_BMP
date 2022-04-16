#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.loadBMP(rootdir+'/assets/Tanuki.bmp') # load to memory
        b.mirrorbottomright(bmp)
        file='HelloMirrorBottomLeft.bmp' # file name
        b.saveBMP(file,bmp) # save file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



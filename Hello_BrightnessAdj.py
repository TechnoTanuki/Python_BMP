#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get the path of this script
        bmp=b.loadBMP(rootdir+'/assets/somebody.bmp') #load to memory as byte array
        b.brightnesseadjto24bitimage(bmp,200) # 2nd param brightness adj percent + or -
        file='HelloBrightnessAdj.bmp' # file name <string>
        b.saveBMP(file,bmp) # a very simple memory dump of byte array bmp to a file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()

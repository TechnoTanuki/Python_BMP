#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') # load earth to memory
        #gammaadjto24bitregion(bmp,x1,y1,x2,y2,gammadj <ufloat>)
        b.gammaadjto24bitregion(bmp,30,30,138,138,4)
        b.gammaadjto24bitregion(bmp,50,50,118,118,.1)
        file='HelloRectangularGammaAdj.bmp' #file name
        b.saveBMP(file,bmp) # bmp<byte array in bitmap format> --> file
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



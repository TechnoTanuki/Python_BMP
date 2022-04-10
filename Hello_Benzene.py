#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        mx,my=250,250 #bitmap size
        bmp=b.newBMP(mx,my,24)
        b.gradvert(bmp,b.regpolygonvert(125,125,80,6,0),55,[255,0],[.4,.7,.3])
        file='HelloBenzene.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



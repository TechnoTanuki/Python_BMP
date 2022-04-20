#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get current dir of script
        file=rootdir+'/assets/somebody.bmp'
        newfile='8bitBMP.bmp'
        print(file)
        bits= 8 # valid values are 8,4,1
        threshold=4 # in computing new palette how far apart should colors be
        usemono=False # can apply a mono filter
        RGBfactors=[0.25,.5,1] # not used unless usemono filter is True
        b.reduce24bitimagebits(file,newfile,bits,threshold,usemono,RGBfactors) # magic takes time
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+newfile) # replace with another editor if Unix

if __name__=="__main__": 
        main()



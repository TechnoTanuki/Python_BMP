#Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com
#This graphics library outputs to a bitmap file

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0])
        file=rootdir+'/assets/somebody.bmp'
        newfile='1bitBMP.bmp'
        print(file)
        b.reduce24bitimagebits(file,newfile,1,0,False,[0.25,.5,1])
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+newfile) # replace with another editor if Unix

if __name__=="__main__": 
        main()



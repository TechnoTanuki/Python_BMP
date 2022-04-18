#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of this script
        existingfile=rootdir+'/assets/earth.bmp' # existing file
        newfile='Hello4timesbigger.bmp' # new file
        n=4 # unsigned int multiplier
        b.resizeNtimesbigger2file(existingfile,newfile,n) # make earth bigg by n times
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+newfile) # replace with another editor if Unix

if __name__=="__main__": 
        main()



#/--------------------------------------------------------------\
#| Copyright 2022 by Joel C. Alcarez /joelalcarez1975@gmail.com |
#| This graphics library outputs to a bitmap file               |
#\--------------------------------------------------------------/

import Python_BMP.BITMAPlib as b,subprocess as proc
from os import path,sys
        
def main():
        rootdir=path.abspath(sys.path[0]) # get path of script
        bmp=b.loadBMP(rootdir+'/assets/earth.bmp') #load earth to memory
        eraseeverynline,eraseNthline=4,3 # control line erase
        #if i%int_eraseeverynline==int_eraseNthline: bmp[s2:s2+bufsize]=blank
        bytepattern=0 # byte pattern for line erase
        b.erasealternatehorizontallines(bmp,eraseeverynline,eraseNthline,bytepattern)
        file='HelloTVEarth.bmp' #file name
        b.saveBMP(file,bmp)
        print('\nAll done close mspaint to finish')
        ret =proc.call('mspaint '+file) # replace with another editor if Unix

if __name__=="__main__": 
        main()



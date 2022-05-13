notice = """
  Resize image %i times bigger Demo
 -----------------------------------
| Copyright 2022 by Joel C. Alcarez |
| [joelalcarez1975@gmail.com]       |
|-----------------------------------|
|    We make absolutely no warranty |
| of any kind, expressed or implied |
|-----------------------------------|
|   This graphics library outputs   |
|   to a bitmap file.               |
 -----------------------------------
"""
from Python_BMP.BITMAPlib import(
        resizeNtimesbigger2file
)

import subprocess as proc
from os import path

def main():
        n = 4 # unsigned int multiplier
        print(notice % (n))
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        existingfile = rootdir + '/assets/earth.bmp' # existing file
        file = 'Hello4timesbigger.bmp' # new file
        resizeNtimesbigger2file(existingfile, file, n) # make earth bigg by n times
        print('All done close %s to finish' % (imgedt)) # tell user something happened
        ret = proc.call(imgedt + ' ' + file) # load the image

if __name__=="__main__":
        main()



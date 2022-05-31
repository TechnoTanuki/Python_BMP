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
        existingfile = f'{rootdir}/assets/earth.bmp'
        file = 'Hello4timesbigger.bmp' # new file
        resizeNtimesbigger2file(existingfile, file, n) # make earth bigg by n times
        print(f'All done close {imgedt} to finish')
        ret = proc.call(f'{imgedt} {file}')

if __name__=="__main__":
        main()



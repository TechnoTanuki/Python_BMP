notice = """
 Resize image %i times smaller Demo
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
        resizeNtimessmaller2file as f,
        getfuncmetastr as meta
        )

import subprocess as proc
from os import path


def main():
        n = 3 # unsigned int multiplier
        print(f'{notice % (n)}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        existingfile = f'{rootdir}/assets/tanuki.bmp'
        file = f'Hello{f.__name__}.bmp' # new file
        f(existingfile, file, n) # make earth smol by n times
        print(f'All done close {imgedt} to finish')
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()



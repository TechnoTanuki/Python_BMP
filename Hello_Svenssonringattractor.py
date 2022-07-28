notice = """
 Svensson ring Attractor Fractal Demo
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
    saveikedaattractor2file as f,
    getfuncmetastr as meta)
from Python_BMP.fractals import svenssonringattractorlist
import subprocess as proc
from os import path


def main():
        print(f'{notice}\n{meta(f)}')
        imgedt = 'mspaint'  # replace with another editor if Unix
        rootdir = path.dirname(__file__) #get path of running script
        file = f'hello{f.__name__}.bmp' # random file name
        f(file, # path to new file
        256, 256, # size of file
        24, # bit depth
        0.85, 0.9, 0.4, 7.7, # constants (float)
        100000 # number of iterations
        )
        l = svenssonringattractorlist(1.40, 1.56, 1.40, -6.56, 100000)
        print(l)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

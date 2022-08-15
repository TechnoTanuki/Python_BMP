notice = """
    Symmetric Icon Attractor Demo
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
    savesymmetriciconattractor2file as f,
    getfuncmetastr as meta)
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
        0.01, 0.01, 1.0, -0.1, 0.167, 0.0, -2.08, 7,# constants (float)
        30100 # number of iterations
        )
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, imgedt)) # tell user something happened
        ret = proc.call([imgedt, file])

if __name__=="__main__":
        main()

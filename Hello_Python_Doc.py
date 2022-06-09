notice = """
 Documentation Generator Py Version
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
Output to %s
"""
from Python_BMP.BITMAPlib import(
        getfuncmetastr as meta,
        )

from inspect import getmembers, isfunction
import Python_BMP.BITMAPlib as m

import subprocess as proc
from os import path


def savelist(mlist: list, filename: str):
    with open(filename,'w') as f:
        for m in mlist:
            f.write(f'{m}\n\n')
        f.close()


def main():
        edt = 'notepad' # change if Linux
        file = 'BitmapLib_Doc.py'
        rootdir = path.dirname(__file__) # get path of this script
        print(f'{notice % (file)}')
        l = [meta(m[1]) for m in getmembers(m, isfunction)]
        l = sorted(l, key = str.lower)
        savelist(l, file)
        print('Saved to %s in %s\nAll done close %s to finish' % \
                (file, rootdir, edt)) # tell user we are done
        ret = proc.call([edt, file])

if __name__=="__main__":
        main()


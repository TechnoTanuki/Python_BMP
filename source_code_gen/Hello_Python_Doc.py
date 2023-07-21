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
from pythonbmp.BITMAPlib import(
        getfuncmetastr as meta,
        )

import webbrowser as web
from inspect import getmembers, isfunction
import pythonbmp.BITMAPlib as m

import subprocess as proc
from os import path


def savelist(mlist: list, filename: str):
    with open(filename,'w') as f:
        for m in mlist:
            f.write(f'{m}\n\n')
        f.close()


def isPublic(s: str) -> bool:
        return s[0:5] != "def _"


def main():
        edt = 'notepad' # change if Linux
        file = 'BitmapLib_Doc.py'
        rootdir = path.dirname(__file__) # get path of this script
        file = f'{rootdir}/docs/{file}'
        print(f'{notice % (file)}')
        l = [meta(m[1]) for m in getmembers(m, isfunction)]
        l = sorted(l, key = str.lower)
        l = filter(isPublic, l)
        savelist(l, file)
        print('Saved to %s \nAll done close %s to finish' % \
                (file, edt)) # tell user we are done
        ret = proc.call([edt, file])

if __name__=="__main__":
        main()


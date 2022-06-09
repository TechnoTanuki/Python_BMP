notice = """
 Documentation Generator md Version
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

from typing import Callable
from inspect import getmembers, isfunction, signature
import Python_BMP.BITMAPlib as m
import webbrowser as web

import subprocess as proc
from os import path


def savelist(hdr: str, mlist: list, filename: str):
    with open(filename,'w') as f:
        f.write(f'# {hdr}\n\n')
        for m in mlist:
            f.write(f'{m}\n\n')
        f.close()


def isPublic(s: str) -> bool:
        return s[0:7] != "**def _"


def meta(f: Callable):
    _d= '"'*3
    return f'**def {f.__name__}{signature(f)}:**\n>{_d}{f.__doc__}{_d}\n'


def main():
        rootdir = path.dirname(__file__) # get path of this script
        file = f'{rootdir}/docs/BitmapLib_Doc.md'
        print(f'{notice % (file)}')
        l = sorted([meta(m[1]) for m in
                        getmembers(m, isfunction)],
                   key = str.lower)
        savelist("Python BMP Public API", filter(isPublic, l), file)
        print('Saved to %s\nAll done close brower to finish' % \
                (file)) # tell user we are done
        web.open_new(file)

if __name__=="__main__":
        main()


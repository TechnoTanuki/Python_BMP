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
from inspect import getdoc, getmembers, isfunction, signature
import Python_BMP.BITMAPlib as m
import webbrowser as web
from re import sub
import subprocess as proc
from os import path


def savelist(hdr: str, mlist: list, filename: str):
    with open(filename,'w') as f:
        f.write(f'# {hdr}\n\n')
        for m in mlist:
            f.write(f'{m}\n\n')
        f.close()


def isPublic(s: str) -> bool:
        return s[0:7] != "### [`_"


def isPrivate(s: str) -> bool:
        return s[0:7] == "### [`_"


def meta(f: Callable):
    fqname = ".".join((f.__module__, f.__qualname__))
    d = getdoc(f) or ""
    d1 = d.split("\n\n")[0]
    d2 = d[len(d1)+2:].replace("\n", "\n    ")
    return "\x0a".join([
      f"### [`{f.__qualname__}`](#{f.__qualname__})",
      "",
      "```py",
      f"def {f.__name__}{sub(r'<function ', '' ,sub(r' at 0x([0-9a-fA-F]+>)', '' , str(signature(f))))}:",
      "```",
      "",
      d1,
      "",
      f"    {d2}",
      "",
    ])



def main():
        rootdir = path.dirname(__file__) # get path of this script
        files = [f'{rootdir}/docs/BitmapLib_Doc.md',
                 f'{rootdir}/docs/BitmapLibInternals_Doc.md']
        print(f'{notice % (files)}')
        l = sorted([meta(m[1]) for m in
                        getmembers(m, isfunction)],
                   key = str.lower)
        savelist("Python BMP Public API", filter(isPublic, l), files[0])
        savelist("Python BMP Internal API", filter(isPrivate, l), files[1])
        print('Saved to %s\nAll done close browser to finish' % \
                (files)) # tell user we are done
        web.open_new(files[0])
        web.open_new(files[1])

if __name__=="__main__":
        main()

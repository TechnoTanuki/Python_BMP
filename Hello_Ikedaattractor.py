notice = """
          Hello World Demo
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
from Python_BMP.mathlib import getcomplexdomainbounds
from Python_BMP.fractals import ikedaattractor
import subprocess as proc
from os import path


def main():
    d = ikedaattractor(0.85, 0.9, 0.4, 7.7,1000000)
    domain = getcomplexdomainbounds(d)
    print (domain)

if __name__=="__main__":
        main()
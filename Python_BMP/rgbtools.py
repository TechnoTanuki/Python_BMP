from array import array
from .mathlib import addvectinlist,intscalarmulvect
from .buffersplit import altsplitbuf3way,altsplitbufnway
from .colors import makeBGRbuf

def resizesmaller24bitbuf(buflist: array):
    n,a,m,s=len(buflist),addvectinlist,intscalarmulvect,altsplitbufnway
    c,f=altsplitbuf3way(a(buflist)),1/(n*n)
    return  makeBGRbuf(m(a(s(c[0],n)),f),m(a(s(c[1],n)),f),m(a(s(c[2],n)),f))

#Factored discrete Fourier transform, or FFT, and its inverse iFFT */


from math import sin, cos, pi
from cmath import exp

"""
   fft(v,N):
   [0] If N==1 then return.
   [1] For k = 0 to N/2-1, let ve[k] = v[2*k]
   [2] Compute fft(ve, N/2);
   [3] For k = 0 to N/2-1, let vo[k] = v[2*k+1]
   [4] Compute fft(vo, N/2);
   [5] For m = 0 to N/2-1, do [6] through [9]
   [6]   Let w.re = cos(2*PI*m/N)
   [7]   Let w.im = -sin(2*PI*m/N)
   [8]   Let v[m] = ve[m] + w*vo[m]
   [9]   Let v[m+N/2] = ve[m] - w*vo[m]
"""
""" fftfn = lambda a: complex(cos(a), -sin(a))
ifftfn = lambda a: complex(cos(a), sin(a)) """

fftfn = lambda a: exp(a * -1j)
ifftfn = lambda a: exp(a * 1j)

def applyfft(fn, v: list[complex], tmp: list[complex]):
    n = len(v)
    if n > 1:
        l = n >> 1
        vo = [0] * l
        ve = [0] * l
        for k in range(l):
            _2k = k << 1
            ve[k] = v[_2k]
            vo[k] = v[_2k + 1]
        applyfft(fn, ve, v)
        applyfft(fn, vo, v)
        for m in range(l):
            w = fn(_2pi * m / n) * vo[m]
            vm = ve[m]
            v[m] = vm + w
            v[m + l] = vm - w


def fft(v: list[complex]):
    applyfft(fftfn, v, [])

def ifft(v: list[complex]):
    applyfft(ifftfn, v, [])


q = 3
N = 1 << q
_2pi = 2 * pi


def main():
    v = [0] * N
    v1 = [0] * N
    scratch = [0] * N
    for  k in range(0, N):
        a = _2pi * k / N
        v[k] = complex(0.125*cos(a), 0.125*sin(a))
        v1[k] = complex(0.3*cos(a), -0.3*sin(a))

    print("Orig", v)
    fft(v)
    print(" FFT", v)
    ifft(v)
    print("iFFT", v)

"""
    v1con = [x.conjugate() for x in v1]
    print("Orig", v1, N)
    fft(v1, N, scratch)

    print(" FFT", v1, N)
    ifft(v1, N, scratch)
    print("iFFT", v1, N)
    fft(v1con, N, scratch)
    print("iFFTvcon", v1con, N)
"""


main()
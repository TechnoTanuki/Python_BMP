#Factored discrete Fourier transform, or FFT, and its inverse iFFT */


from math import sin, cos, pi

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
fft = lambda a: complex(cos(a), -sin(a))
ifft = lambda a: complex(cos(a), sin(a))

def applyfft(fn, v: list[complex], n: int, tmp: list[complex]):
    if n > 1:
        l = n >> 1
        vo = [0] * l
        ve = [0] * l
        for k in range(0, l):
            _2k = k << 1
            ve[k] = v[_2k]
            vo[k] = v[_2k + 1]
        applyfft(fn, ve, l, v)
        applyfft(fn, vo, l, v)
        for m in range(0, l):
            w = fn(_2pi * m / n) * vo[m]
            vm = ve[m]
            v[m] = vm + w
            v[m + l] = vm - w

"""
   [0] If N==1 then return.
   [1] For k = 0 to N/2-1, let ve[k] = v[2*k]
   [2] Compute ifft(ve, N/2);
   [3] For k = 0 to N/2-1, let vo[k] = v[2*k+1]
   [4] Compute ifft(vo, N/2);
   [5] For m = 0 to N/2-1, do [6] through [9]
   [6]   Let w.re = cos(2*PI*m/N)
   [7]   Let w.im = sin(2*PI*m/N)
   [8]   Let v[m] = ve[m] + w*vo[m]
   [9]   Let v[m+N/2] = ve[m] - w*vo[m]
 */
"""
""" def ifft(v: list[complex], n: int,  tmp: list[complex]):
    if n > 1:
        halfn = n >> 1
        vo = [0] * halfn
        ve = [0] * halfn
        for k in range(0, halfn):
            _2k = k << 1
            ve[k] = v[_2k]
            vo[k] = v[_2k + 1]
        ifft(ve, halfn, v)
        ifft(vo, halfn, v)
        for m in range(0, halfn):
            a = _2pi * m / n
            w = complex(cos(a), sin(a)) * vo[m]
            vm = ve[m]
            v[m] = vm + w
            v[m + halfn] = vm - w
 """

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
    
    print("Orig", v, N)
    applyfft(fft,v, N, scratch)
    print(" FFT", v, N)
    applyfft(ifft, v, N, scratch)
    print("iFFT", v, N)


    """ v1con = [x.conjugate() for x in v1]
    print("Orig", v1, N)
    fft(v1, N, scratch)

    fft(v1con, N, scratch)
    print(" FFT", v1, N)
    ifft(v1, N, scratch)
    print("iFFT", v1, N)
    print("iFFTvcon", v1con, N)
 """
main()
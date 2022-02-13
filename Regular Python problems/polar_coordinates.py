import cmath

z = complex(input())
print(abs(complex(z.real, z.imag)))
print(cmath.phase(complex(z.real, z.imag)))

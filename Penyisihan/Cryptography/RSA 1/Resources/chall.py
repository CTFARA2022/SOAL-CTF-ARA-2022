from Crypto.Util.number import getPrime, bytes_to_long, GCD
from flag import FLAG
from math import isqrt

p = getPrime(512)
q = getPrime(512)
n = p * q

m = bytes_to_long(FLAG)
assert m * m < n
c = pow(n+1, m, n*n*n)
print(f'{n = }')
print(f'{c = }')

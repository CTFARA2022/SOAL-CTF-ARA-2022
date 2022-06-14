from Crypto.Util.number import bytes_to_long, GCD
from flag import FLAG
import random

def gen(n):
    W = [random.randrange(2, 69)]
    for i in range(n - 1):
        W.append(random.randrange(sum(W)+1, sum(W)*2))
        assert W[-1] > sum(W[:-1])
    q = random.randrange(sum(W)+1, sum(W)*2)
    r = random.randrange(2, q)
    while GCD(r, q) != 1:
        r = random.randrange(2, q)
    B = list(map(lambda x: (x * r) % q, W))
    return B, W, q, r

def encrypt(msg, key):
    assert msg.bit_length() <= len(key)
    ct = 0
    for i in key:
        ct += (msg & 1) * i
        msg >>= 1
    return ct

def decrypt(ct, W, q, r):
    rp = pow(r, -1, q)
    cp = (ct * rp) % q
    m = 0
    for i in range(len(W) - 1, -1, -1):
        if cp >= W[i]:
            m |= (1 << i)
            cp -= W[i]
    return m

m = bytes_to_long(FLAG)
n = m.bit_length() + 1
B, W, q, r = gen(n)
ct = encrypt(m, B)
assert decrypt(ct, W, q, r) == m
print(f'{B = }')
print(f'{ct = }')

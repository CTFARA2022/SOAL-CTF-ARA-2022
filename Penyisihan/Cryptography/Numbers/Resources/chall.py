from Crypto.Util.number import bytes_to_long
from flag import FLAG

f1, f2, f3, f4 = [bytes_to_long(FLAG[i:i+8]) for i in range(0, len(FLAG), 8)]

print(f'{f1**3 - f2**3 + f3 - f4 = }')
print(f'{-f1**3 * f2**3 + f1**3 * f3 - f2**3 * f3 - f1**3 * f4 + f2**3 * f4 - f3 * f4 = }')
print(f'{-f1**3 * f2**3 * f3 + f1**3 * f2**3 * f4 - f1**3 * f3 * f4 + f2**3 * f3 * f4 = }')
print(f'{f1**3 * f2**3 * f3 * f4 = }')

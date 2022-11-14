from pubcrypt.number.util import gcd, pow_mod, isqrt

"""
print (f"2^{j}-1 = {a} mod {n}, gcd(2^{j}1) mod {n} = {d}")
"""


# p-1 facto
def pollard(n):
	a = 2
	bound = isqrt(n)-1

	for j in range(2, bound):
		a = pow_mod(a, j, n)
		d = gcd(a-1, n)
		if 1 < d < n:
			return n//d, d
long long powmod(long long n, unsigned long long k, long long p) {
	if (k == 0)
		return 1;

	if (k % 2)
		return ((n % p) * powmod(n, k - 1, p)) % p;

	long long aux = powmod(n, k >> 1, p);

	return (aux * aux) % p;
}

/* Definition:
 * If n ** i % p yields a different result for each value of i in 1..P-1,
 * then n is called a primitive root modulo p.
 * Returns 1 if n is a primitive root modulo p and 0 otherwise.
 */
_Bool is_primitive_root(long long n, long long p) {
	_Bool table[p];

	for (long long i = 0; i < p; i++)
		table[i] = 0;

	for (long long i = 1; i < p; i++) {
		long long pos = powmod(n, i, p);

		if (table[pos])
			return 0;

		table[pos] = 1;
	}

	return 1;
}

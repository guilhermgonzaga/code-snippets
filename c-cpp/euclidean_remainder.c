/* Compute the remainder R of A / B according to Euclid's Division Theorem
 * (A = Q*B + R, Q being the quotient such that 0 <= R < |B|).
 */
unsigned euclidean_remainder(int A, int B) {
	int remainder = A % B;

	if (remainder < 0)
		remainder += (B < 0) ? -B : B;

	return remainder;
}

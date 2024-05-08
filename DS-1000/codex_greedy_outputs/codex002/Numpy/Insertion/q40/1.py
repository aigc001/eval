
# Find the greatest common divisor (gcd)
gcd = np.gcd(numerator, denominator)

# Divide both the numerator and denominator by the gcd
numerator = numerator // gcd
denominator = denominator // gcd

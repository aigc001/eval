
if denominator == 0:
    result = (np.nan, np.nan)
else:
    gcd = np.gcd(numerator, denominator)
    result = (numerator // gcd, denominator // gcd)
print(result)

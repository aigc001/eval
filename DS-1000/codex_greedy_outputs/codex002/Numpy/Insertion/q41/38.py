
    # Calculate the greatest common divisor (gcd)
    gcd = np.gcd(numerator, denominator)

    # Return the reduced fraction
    return (numerator // gcd, denominator // gcd)

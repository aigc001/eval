
def array_equal_nan(a, b):
    return np.allclose(a, b, equal_nan=True)

print(any(array_equal_nan(c, contour) for contour in CNTS))

def remove_contour(CNTS, c):
    return [contour for contour in CNTS if not array_equal_nan(c, contour)]

CNTS = remove_contour(CNTS, c)

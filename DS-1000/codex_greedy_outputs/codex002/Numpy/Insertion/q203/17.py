
def check_nan(lst):
    for arr in lst:
        if not np.isnan(arr).all():
            return False
    return True

print(check_nan(a))

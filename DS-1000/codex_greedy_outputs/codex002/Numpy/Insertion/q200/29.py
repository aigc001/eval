
# compare the two arrays with a tolerance of the machine precision
tol = np.finfo(float).eps
diff = np.abs(s1 - s2)
# print the number of times s1 and s2 are different up to the machine precision
print np.nonzero(diff > tol)[0].shape[0]

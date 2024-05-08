
# We use numpy's bincount function which is equivalent to MATLAB's accumarray
# We need to take care of negative indices.
# We add the maximum absolute index to all elements of accmap to make them non-negative
# Then we use bincount to accumulate the elements
result = np.bincount(accmap + np.abs(np.min(accmap)))
# We only keep the first n elements where n is the maximum absolute index
result = result[:np.max(accmap)+1]
print(result)


# Pad the array with a period of itself
a_padded = np.pad(a, (0, len(a)), mode='wrap')

# Perform the correlation
correlation = np.correlate(a_padded, b, mode='valid')

print(correlation)

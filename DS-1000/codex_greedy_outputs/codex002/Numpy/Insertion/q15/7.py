
# Create a new array with the same shape as the original array, filled with NaNs
shifted_a = np.full_like(a, np.nan)

# Assign the shifted values to the new array
if shift > 0:
    shifted_a[:, shift:] = a[:, :-shift]
elif shift < 0:
    shifted_a[:, :shift] = a[:, -shift:]

print(shifted_a)

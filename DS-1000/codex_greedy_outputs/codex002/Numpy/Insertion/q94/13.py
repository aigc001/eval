
# Reshape the array to 2D patches of size 2x2
patches = a.reshape(2, 2, -1, 2).transpose(2, 0, 1, 3)

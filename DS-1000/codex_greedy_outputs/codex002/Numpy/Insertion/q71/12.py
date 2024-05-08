
# We subtract 1 from each element in del_col because indexing in python starts from 0
# We also need to make sure that the indices are not out of bounds
del_col = del_col - 1
del_col = del_col[del_col < a.shape[1]]
# We delete the columns
a = np.delete(a, del_col, axis=1)

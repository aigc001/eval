
#iterate through columns
for Col in xrange(sa.shape[1]):
    #get the column
    Column = sa[:,Col].toarray().flatten()
    #normalize the column
    Column /= math.sqrt(np.sum(Column**2))
    #update the column in the sparse matrix
    sa[:,Col] = Column

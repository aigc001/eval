
#iterate through columns
for Col in xrange(sa.shape[1]):
   Column = sa[:,Col].toarray().flatten()
   List = [x**2 for x in Column]
   #get the column length
   Len = math.sqrt(sum(List))
   #scalar multiplication
   Column = Column/Len
   #update the column
   sa[:,Col] = sparse.csr_matrix(Column)

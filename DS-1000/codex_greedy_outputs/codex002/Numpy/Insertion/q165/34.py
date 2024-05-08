
from scipy.spatial.distance import cdist
dist_matrix = cdist(a, a, 'euclidean')
print(dist_matrix)

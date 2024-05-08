
from sklearn.preprocessing import PowerTransformer

# Initialize the PowerTransformer
pt = PowerTransformer(method='yeo-johnson')

# Fit and transform the data
data_transformed = pt.fit_transform(data)

# Output the transformed data
print(data_transformed)


import numpy as np

# Define the sigmoid function
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

# Apply the sigmoid function to each column and add the result to the dataframe
for col in df.columns:
    df[f"sigmoid_{col}"] = df[col].apply(sigmoid)

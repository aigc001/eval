
# Create an empty list to store the slopes
slopes = []

# Iterate over the columns
for col in df1.columns:
    # Drop the NaN values for the current column
    df2 = df1[~np.isnan(df1[col])]
    
    # Create a matrix with the 'Time' and the current column
    df3 = df2[['Time', col]]
    
    # Fit the linear regression model
    model = LinearRegression().fit(df3.iloc[:, :-1], df3.iloc[:, -1])
    
    # Get the slope and append it to the list
    slopes.append(model.coef_[0])

# Convert the list to a numpy array
slopes = np.array(slopes)

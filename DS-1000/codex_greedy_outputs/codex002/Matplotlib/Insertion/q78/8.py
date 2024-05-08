plt.figure()

# Create a list of x-coordinates and a list of y-coordinates
x_coords = [point[0] for point in points]
y_coords = [point[1] for point in points]

# Plot the points
plt.plot(x_coords, y_coords)

# Set the y-axis to log scale
plt.yscale('log')

# Show the plot
plt.show()

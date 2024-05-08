plt.figure(figsize=(10, 6))
ax = plt.gca()

# Hide the axes
ax.axis("off")

# Create a table from df
table = pd.plotting.table(ax, df, loc="center")

# Set the bbox of the table to [0, 0, 1, 1]
table.set_bbox([0, 0, 1, 1])

# Show the plot
plt.show()

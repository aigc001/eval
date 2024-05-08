plt.figure(figsize=(10,6))

# Create a bar plot for s1
plt.bar(df['celltype'], df['s1'], color='b', label='s1')

# Create a bar plot for s2
plt.bar(df['celltype'], df['s2'], color='r', alpha=0.5, label='s2')

# Add labels, title and legend
plt.xlabel('Cell Type')
plt.ylabel('Value')
plt.title('Bar Plot of Cell Types')
plt.legend()

# Rotate x-axis tick labels
plt.xticks(rotation=45)

# Show the plot
plt.show()

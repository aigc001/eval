plt.bar(range(len(blue_bar)), blue_bar, color='b', label='Blue Bar')
plt.bar(range(len(orange_bar)), orange_bar, color='orange', label='Orange Bar')

# Add labels and title
plt.xlabel('Index')
plt.ylabel('Value')
plt.title('Side-by-side Bar Plot')

# Add a legend
plt.legend()

# Show the plot
plt.show()

fig, axs = plt.subplots(1, 2, gridspec_kw={'width_ratios': [3, 1]})

# Plot the data on the first subplot
axs[0].plot(x, y)
axs[0].set_title('First Plot')

# Plot the data on the second subplot
axs[1].plot(x, y)
axs[1].set_title('Second Plot')

# Adjust the spacing between the subplots
plt.tight_layout()

# Show the plot
plt.show()

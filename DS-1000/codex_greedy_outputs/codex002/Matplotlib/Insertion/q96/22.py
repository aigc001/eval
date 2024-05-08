fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].plot(x, y)
axs[0].set_title('Plot 1')

axs[1].plot(x, y)
axs[1].set_title('Plot 2')

fig.suptitle('Figure')

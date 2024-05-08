fig, axs = plt.subplots(1, 2, figsize=(10, 5))

axs[0].plot(x, y)
axs[0].set_title('Y', fontsize=15)

axs[1].plot(a, z)
axs[1].set_title('Z', fontsize=15)
axs[1].title.set_position([0.5, 1.1])

plt.show()

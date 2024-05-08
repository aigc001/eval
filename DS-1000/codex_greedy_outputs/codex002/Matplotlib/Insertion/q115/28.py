fig, axs = plt.subplots(2)

axs[0].plot(x, y, label='Line 1')
axs[0].plot(x, z, label='Line 2')
axs[0].legend()

axs[1].plot(a, z)

plt.show()

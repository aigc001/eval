fig, axs = plt.subplots(2, 1, figsize=(10, 10))

axs[0].plot(x, y)
axs[0].set_title('Y over X')

axs[1].plot(a, z)
axs[1].set_title('Z over A')

fig.suptitle('Y and Z')
plt.show()

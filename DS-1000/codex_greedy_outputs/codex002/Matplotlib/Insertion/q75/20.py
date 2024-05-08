fig, axs = plt.subplots(1, 2, figsize=(10, 5))

# create a colorbar for the first subplot
im1 = axs[0].imshow(x, cmap='hot')
fig.colorbar(im1, ax=axs[0])

# create a colorbar for the second subplot
im2 = axs[1].imshow(y, cmap='cool')
fig.colorbar(im2, ax=axs[1])

plt.show()

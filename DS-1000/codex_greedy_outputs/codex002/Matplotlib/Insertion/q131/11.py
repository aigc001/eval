fig, axs = plt.subplots(2, 2, figsize=(15, 15))

for row in axs:
    for ax in row:
        ax.plot(x, y)

plt.show()

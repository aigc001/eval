fig, axs = plt.subplots(4, 4, figsize=(5,5), sharex=True, sharey=True)

for ax in axs.flatten():
    ax.plot(x, y)
    ax.tick_params(axis='both', which='major', labelsize=8)

plt.tight_layout()
plt.show()

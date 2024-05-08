gs = gridspec.GridSpec(nrow, ncol, wspace=0, hspace=0)

for i in range(nrow):
    for j in range(ncol):
        ax = fig.add_subplot(gs[i, j])
        ax.imshow(x, cmap='gray')
        ax.axis('off')

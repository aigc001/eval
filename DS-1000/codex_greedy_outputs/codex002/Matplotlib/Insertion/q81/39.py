for i, line in enumerate(lines):
    x = [point[0] for point in line]
    y = [point[1] for point in line]
    plt.plot(x, y, color=c[i])

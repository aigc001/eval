
# calculate the slope and y-intercept of the line passing through (a, b) and (c, d)
slope = (d - b) / (c - a)
y_intercept = b - slope * a

x = np.linspace(0, 5, 100)
y = slope * x + y_intercept

plt.plot(x, y, color='red')

plt.xlim(0, 5)
plt.ylim(0, 5)

plt.scatter([a, c], [b, d], color='blue')

plt.show()


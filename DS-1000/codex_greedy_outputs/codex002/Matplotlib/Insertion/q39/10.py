plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1)
plt.title('Sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([])  # remove x-axis ticks
plt.yticks([])  # remove y-axis ticks

plt.subplot(1, 2, 2)
plt.plot(x, y2)
plt.title('Cos(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.xticks([])  # remove x-axis ticks
plt.yticks([])  # remove y-axis ticks

plt.tight_layout()
plt.show()

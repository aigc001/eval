plt.figure(figsize=(10, 5))

plt.subplot(1, 2, 1)
plt.plot(x, y1, color='blue', label='sin(x)')
plt.xlabel('x')
plt.ylabel('y', color='blue')
plt.legend()

plt.subplot(1, 2, 2)
plt.plot(x, y2, color='red', label='cos(x)')
plt.xlabel('x')
plt.ylabel('y', color='red')
plt.legend()

plt.tight_layout()
plt.show()

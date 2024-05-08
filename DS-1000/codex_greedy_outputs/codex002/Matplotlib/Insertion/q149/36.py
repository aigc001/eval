plt.figure(figsize=(12, 6))

plt.subplot(1, 3, 1)
plt.plot(t, a, 'r')
plt.title('Sin(t)')

plt.subplot(1, 3, 2)
plt.plot(t, b, 'g')
plt.title('Cos(t)')

plt.subplot(1, 3, 3)
plt.plot(t, c, 'b')
plt.title('Sin(t) + Cos(t)')

plt.tight_layout()
plt.show()

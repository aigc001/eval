
def smoothstep(x, x_min, x_max, N):
    if N <= 0:
        return np.clip(x, x_min, x_max)
    else:
        x_N = (x - x_min) / (x_max - x_min)
        return x_min + (x_max - x_min) * x_N**N * (N + 1) / (N + 1 + N * x_N)

print(smoothstep(x, x_min, x_max, N))

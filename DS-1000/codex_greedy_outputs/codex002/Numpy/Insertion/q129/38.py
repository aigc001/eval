
def smooth_clamp(x, x_min, x_max):
    if x < x_min:
        return x_min + (x - x_min)**2 * (x_min + 2*(x_max - x_min) - x)
    elif x > x_max:
        return x_max - (x - x_max)**2 * (x_max - 2*(x_max - x_min) - x)
    else:
        return x

smooth_clamp(x, x_min, x_max)


interp = scipy.interpolate.LinearNDInterpolator(points, V)
result = interp(request)
print(result)

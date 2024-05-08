
def f(vars):
  a, b, c = vars
  return ((a+b-c)-2)**2 + ((3*a-b-c))**2 + sin(b) + cos(b) + 4

res = optimize.minimize(f, initial_guess)

print(res.x)

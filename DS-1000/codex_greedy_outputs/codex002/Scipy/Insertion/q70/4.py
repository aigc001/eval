
# The line_search function requires a function that takes a single argument,
# so we need to wrap our multivariable function in a lambda function.
# The lambda function takes a single argument, which is a list of x values.
# The function inside the lambda function calls our original test_func with the x values.
f = lambda x: test_func([x[0], x[1]])

# Similarly, we need to wrap our multivariable gradient function in a lambda function.
# The lambda function takes a single argument, which is a list of x values.
# The function inside the lambda function calls our original test_grad with the x values.
grad = lambda x: test_grad([x[0], x[1]])

# Now we can call the line_search function.
# The first argument is the function to minimize.
# The second argument is the gradient of the function.
# The third argument is the starting point for the line search.
# The fourth argument is the direction to search in.
alpha, fc, gc, new_fval, old_fval, new_slope = scipy.optimize.line_search(f, grad, starting_point, direction)

# The line_search function returns a tuple of values.
# The first value is the step size, alpha.
# The second value is the number of function calls made.
# The third value is the number of gradient calls made.
# The fourth value is the function value at the new point.
# The fifth value is the function value at the initial point.
# The sixth value is the dot product of the gradient at the new point and the search direction.

print("Step size:", alpha)
print("Function value at new point:", new_fval)
print("Function value at initial point:", old_fval)
print("Dot product of gradient at new point and search direction:", new_slope)

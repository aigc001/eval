
# Get the steps
steps = clf.named_steps

# Insert a new step
clf.steps.insert(1, ('poly', PolynomialFeatures()))

# Update the named steps
clf._named_steps = dict(estimators)

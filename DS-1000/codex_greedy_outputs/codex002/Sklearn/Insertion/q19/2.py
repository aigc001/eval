
# Get the steps
steps = clf.named_steps

# Insert a new step
steps['t1919810'] = PCA()

# Insert the new step at the correct position
clf.steps.insert(1, ('t1919810', steps['t1919810']))

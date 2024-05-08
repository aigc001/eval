
# Get the steps
steps = clf.named_steps
# Delete the 2nd step
del steps['pOly']
# Check the steps
clf

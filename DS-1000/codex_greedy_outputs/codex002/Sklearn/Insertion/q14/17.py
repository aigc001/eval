
# Get the steps
steps = clf.named_steps
# Delete the 'poly' step
del steps['poly']
# Recreate the pipeline
clf = Pipeline(steps.values())

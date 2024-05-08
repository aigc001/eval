
# Insert a new step at the beginning
estimators.insert(0, ('new_step', PCA()))
clf = Pipeline(estimators)

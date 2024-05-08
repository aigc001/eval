
# Delete 'dim_svm'
estimators = [est for est in clf.steps if est[0] != 'dim_svm']
clf = Pipeline(estimators)

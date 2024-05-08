
probs = []
for train, test in cv:
    logreg.fit(X[train], y[train])
    prob = logreg.predict_proba(X[test])
    probs.append(prob)

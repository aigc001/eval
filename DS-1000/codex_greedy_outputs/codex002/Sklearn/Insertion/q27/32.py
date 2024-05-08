
models = [model]
for model in models:
   scores = cross_val_score(model, X, y, cv=5)
   print(f'Name model: {model.__class__.__name__} , Mean score: {scores.mean()}')

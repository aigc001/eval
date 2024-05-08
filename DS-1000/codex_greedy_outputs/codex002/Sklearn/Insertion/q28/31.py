
models = [model]
model_names = [type(model).__name__]

cv_scores = []
for model, model_name in zip(models, model_names):
   scores = cross_val_score(model, X, y, cv=5)
   cv_scores.append(scores.mean())

df = pd.DataFrame({'Model': model_names, 'CV Score': cv_scores})
print(df)

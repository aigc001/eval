
model = xgb.XGBRegressor()
param_grid = {'max_depth': [3,4,5], 'learning_rate': [0.01,0.1,0.2]} # your hyperparameters
grid_search = GridSearchCV(model, param_grid, cv=TimeSeriesSplit(n_splits=5), verbose=2, n_jobs=-1)
grid_search.fit(trainX, trainY, early_stopping_rounds=42, eval_metric='mae', eval_set=[(testX, testY)])

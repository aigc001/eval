
param_grid = {
    'max_depth': [3, 5, 7, 9],
    'learning_rate': [0.01, 0.1, 0.2, 0.3],
    'subsample': [0.5, 0.7, 1.0],
    'colsample_bytree': [0.4, 0.6, 0.8, 1.0],
    'colsample_bylevel': [0.4, 0.6, 0.8, 1.0],
    'colsample_bynode': [0.4, 0.6, 0.8, 1.0]
}

model = xgb.XGBRegressor()

grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=TimeSeriesSplit(n_splits=3).get_n_splits([trainX, trainY]),
    scoring='neg_mean_squared_error',
    verbose=2,
    n_jobs=-1,
    iid=False
)

grid_search.fit(
    X=trainX,
    y=trainY,
    fit_params={
        "early_stopping_rounds": 42,
        "eval_metric" : "mae",
        "eval_set" : [[testX, testY]]
    }
)


cols = myData.columns[2:4]
myData[['new_A2', 'new_A3']] = myData[cols].apply(lambda x: scaler.fit_transform(x.values.reshape(-1,1)))

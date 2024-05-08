
start = pd.to_datetime(start)
end = pd.to_datetime(end)

# Create an array of equally spaced timestamps
timestamps = pd.date_range(start=start, end=end, periods=n)

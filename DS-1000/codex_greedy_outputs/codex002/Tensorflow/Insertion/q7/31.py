
def my_map_func(i):
  return [i, i+1, i+2]

ds = tf.data.Dataset.from_tensor_slices(input)
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(my_map_func(x)))

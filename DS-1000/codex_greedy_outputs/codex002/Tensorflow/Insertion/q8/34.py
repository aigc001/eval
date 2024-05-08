
  return [[i, i+1, i+2] for i in input]
ds = tf.data.Dataset.from_tensor_slices(example_input)
ds = ds.map(map_func=lambda input: tf.compat.v1.py_func(
  func=f, inp=[input], Tout=[tf.int64]
))
ds = ds.flat_map(lambda x: tf.data.Dataset.from_tensor_slices(x))
element = tf.compat.v1.data.make_one_shot_iterator(ds).get_next()
result = []
with tf.compat.v1.Session() as sess:
  while True:
    try:
      result.append(sess.run(element))
    except tf.errors.OutOfRangeError:
      break
print(result)

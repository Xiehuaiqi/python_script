import tensorflow as tf

v = tf.Variable(0,dtype=tf.float32,name="v")
ema = tf.train.ExponentialMovingAverage(0.99)
print (ema.variables_to_restore())

saver=tf.train.Saver(ema.variables_to_restore())

with tf.Session() as sess:
    saver.restore(sess,"./Model/model_ema.ckpt")
    print(sess.run(v))
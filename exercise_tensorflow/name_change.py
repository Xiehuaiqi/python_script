import tensorflow as tf

u1 = tf.Variable(tf.constant(1.0,shape=[1]),name = "other-v1")
u2 = tf.Variable(tf.constant(2.0,shape=[1]),name = "other-v2")
result = u1 + u2

saver = tf.train.Saver({"v1":u1,"v2":u2})

with tf.Session() as sess:
    saver.restore(sess,"./Model/model.ckpt")
    print(sess.run(result))
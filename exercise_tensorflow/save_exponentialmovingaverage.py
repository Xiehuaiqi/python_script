import tensorflow as tf

v= tf.Variable(0,dtype=tf.float32,name="v")
# v1= tf.Variable(5,1,dtype=tf.float32,name="v1")
for variables in tf.global_variables():
    print(variables.name)

ema = tf.train.ExponentialMovingAverage(0.99)
maintain_averages_op=ema.apply(tf.global_variables())
for variables in tf.global_variables():
    print(variables.name)

saver=tf.train.Saver()
with tf.Session() as sess:
    sess.run(tf.global_variables_initializer())
    sess.run(tf.assign(v,10))
    sess.run(maintain_averages_op)
    saver.save(sess,"Model/model_ema.ckpt")
    print(sess.run([v,ema.average(v)]))
import tensorflow as tf

saver = tf.train.import_meta_graph("Model/model.ckpt.meta")

with tf.Session() as sess:
        saver.restore(sess,tf.train.latest_checkpoint("./Model"))
        print(sess.run(tf.get_default_graph().get_tensor_by_name("add:0")))
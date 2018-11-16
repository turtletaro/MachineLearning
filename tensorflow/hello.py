import tensorflow as tf
import os 
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'

hello = tf.constant('Hello,world!')
sess = tf.Session()
result = sess.run(hello)
sess.close()
print(result)

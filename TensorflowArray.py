import numpy as np
import tensorflow as tf
matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype = 'int32')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype = 'int32')
tf1=tf.constant(matrix1)
tf2=tf.constant(matrix2)
print(tf1)
print(tf2)

import numpy as np
import tensorflow as tf
matrix1 = np.array([(2,2,2),(2,2,2),(2,2,2)],dtype = 'int32')
matrix2 = np.array([(1,1,1),(1,1,1),(1,1,1)],dtype = 'int32')
tf1=tf.constant(matrix1)
tf2=tf.constant(matrix2)
tf3=tf.matmul(tf1,tf2)
sum=tf.add(tf1,tf2)
matrixdet=np.linalg.det(matrix2)
print(tf3)
print(matrixdet)

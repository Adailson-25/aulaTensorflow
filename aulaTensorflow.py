#aula tensorflow

import tensorflow as tf
import numpy as np

frase = tf.constant('ola mundo')
with tf.Session() as sess:
	rodar = sess.run(frase)
print(rodar)
print(tf..Session().run(frase))


a = tf.constant(5)
b = tf.constant(3)
c = tf.constant(2)

d = tf.multiply(a,b)
e = tf.add(b,c)
f = tf.subtract(d,e)

s2 = tf.Session()
saida = s2.run(f)
s2.close()

print(saida)

a1 = tf.constant(2)
b1 = tf.constant([3,1,5,8,6])
c1 = tf.constant([[2,8,4],[3,5,7]])

s3 = tf.Session()
saida = s3.run(c1)
s2.close()

a2 = np.array(2)
b2 = np.array([3,1,5,8,6])
c2 = np.array([[2,8,4],[3,5,7]])

print(a1)
print(b1)
print(c1)

print(a1.shape)
print(b1.shape)
print(c1.shape)

print(a2.shape)
print(b2.shape)
print(c2.shape)

A = tf.constant([[1,2,3],[4,5,6]])
B = tf.constant([[0,0],[1,0],[0,1]])
R1 = tf.matmul(A,B)
print(tf.Session().run(R1))

X = tf.constant([0,1,0])
print(tf.Session().run(X))
print(X.shape)
X = tf.expand_dims(X,1)
R2 = tf.matmul(A,X)
print(tf.Session().run(R2))

tA = tf.transpose(A)
print(tf.Session().run(tA))

var1 = tf.Variable(2)
init = tf.global_variables_initializer()
print(tf.Session().run(var1))

matriz = tf.random.normal((3,5),0,1)
var2 = tf.Variable(matriz)

print(matriz)
print(var2)





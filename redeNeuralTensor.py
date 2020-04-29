import tensorflow as tf
import numpy as np
#parte 1
dados_x = np.random.randn(4,8)
dados_w = np.random.randn(8,2)

b = tf.random_normal((4,2),0,1)

x = tf.placeholder(tf.float32,shape=(4,8))
w = tf.placeholder(tf.float32,shape=(8,2))

operacao = tf.matmul(x,w) + b
maximo = tf.reduce_max(operacao)

with tf.Session() as sess:
	saida1 = sess.run(operacao, feed_dict={x:dados_x,w:dados_w})
	saida2 = sess.run(maximo, feed_dict={x:dados_x,w:dados_w})
print(saida2)

#parte 2
x1 = np.random.randn(4,8)
w1 = np.random.randn(8,2)
x2 = np.random.randn(4,8)
w2 = np.random.randn(8,2)
x3 = np.random.randn(10,3)
w3 = np.random.randn(3,1)
x4 = np.random.randn(4,8)
w4 = np.random.randn(8,2)
x5 = np.random.randn(4,8)
w5 = np.random.randn(8,2)

lista_x = [x1,x2,x3,x4,x5]
lista_w = [w1,w2,w3,w4,w5]
lista_saida = []

c = tf.random_normal((4,2),0,1)
x0 = tf.placeholder(tf.float32,shape=(None,None))
w0 = tf.placeholder(tf.float32,shape=(None,None))

operacao1 = tf.matmul(x0,w0) + c
maximo1 = tf.reduce_max(operacao1)

with tf.Session() as sess1:
	for i in range(5):
		saida = sess1.run(maximo,feed_dict = {x0:lista_x[i],w0:lista_w[i]})
		lista_saida.append(saida)
print(lista_saida)

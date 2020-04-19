import tensorflow as tf
import numpy as np

dados_x = np.randon(4,8)
dados_w = np.randon(8,2)

b = tf.randon_normal((4,2),0,1)

x = tf.placeholder(tf.float32,shape=(4,8)
w = tf.placeholder(tf.float32,shape=(8,2)

operacao = tf.matmult(x,w) + b
maximo = tf.reduce_max(operacao)

with tf.Session() as sess:
	saida1 = sess.run(operacao, feed_dict={x:dados_x,w:dados_w})
	saida2 = sess.run(maximo, feed_dict={x:dados_x,w:dados_w})
print(saida2)

x1 = tf.placeholder(tf.float32,shape=(4,8)
w1 = tf.placeholder(tf.float32,shape=(8,2)
x2 = tf.placeholder(tf.float32,shape=(4,8)
w2 = tf.placeholder(tf.float32,shape=(8,2)
x3 = tf.placeholder(tf.float32,shape=(4,8)
w3 = tf.placeholder(tf.float32,shape=(8,2)
x4 = tf.placeholder(tf.float32,shape=(4,8)
w4 = tf.placeholder(tf.float32,shape=(8,2)
x5 = tf.placeholder(tf.float32,shape=(4,8)
w5 = tf.placeholder(tf.float32,shape=(8,2)

lista_x = [x1,x2,x3,x4,x5]
lista_w = [w1,w2,w3,w4,w5]
lista_saida = []

x0 = tf.placeholder(tf.float32,shape=(None,None)
w0 = tf.placeholder(tf.float32,shape=(None,None)

operacao1 = tf.matmult(x0,w0) + c
maximo1 = tf.reduce_max(operacao1)

with tf.Session as sess1:
	for i in range(5):
		saida = sess1.run(maximo,feed_dict = {x0:lista_x[i],w0:lista_w[i]})
		lista_saida.append(saida)
print(lista_saida)

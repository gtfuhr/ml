from random import randint

N = 1000

lista_a = [randint(0,i) for i in range(N)]
lista_b = [randint(-i,0) for i in range(N)]

len_a = [i for i in range(len(lista_a))]
len_b = [i for i in range(len(lista_b))]

import matplotlib.pyplot as plt

fig = pyplot()
plot(lista_a,len_a,lista_b,len_b)
plot.title("Random variations")
plot.legend(["Quase crescente","Quase decrescente"])

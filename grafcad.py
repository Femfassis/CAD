import matplotlib.pyplot as plot
import numpy 

with open('saida.txt') as saida:
    dados = saida.read()

dados=numpy.array(dados.split("\n"))
Cijt = numpy.array(dados[2:162])
Cjit = numpy.array(dados[163:162+161])
Fortranijt = numpy.array(dados[162+161+1+1:162+161+161+1])
Fortranjit = numpy.array(dados[162+161+161+1+1+1:162+161+161+1+1+161])

Cij = numpy.zeros(len(Cijt))
Cji = numpy.zeros(len(Cijt))
Fortranij = numpy.zeros(len(Cijt))
Fortranji = numpy.zeros(len(Cijt))



for i in range(len(Cijt)):
    Cij[i] = Cijt[i].split(':')[1]
    Cji[i] = Cjit[i].split(':')[1]
    Fortranij[i] = Fortranijt[i].split(':')[1]
    Fortranji[i] = Fortranjit[i].split(':')[1]

xspace = numpy.array(range(100,16001,100))


plot.plot(xspace, Cij, label = 'Cij')
plot.plot(xspace, Cji, label = 'Cji')
plot.legend()
plot.title('Cij x Cji')
plot.xlabel('Tamanho de uma das dimensões da matriz quadrada')
plot.ylabel('Tempo em segundos')
plot.show()


plot.plot(xspace, Fortranij, label = 'Fortranij')
plot.plot(xspace, Fortranji, label = 'Fortranji')
plot.legend()
plot.title('Fortranij x Fortranji')
plot.xlabel('Tamanho de uma das dimensões da matriz quadrada')
plot.ylabel('Tempo em segundos')
plot.show()


plot.plot(xspace, Cij, label = 'Cij')
plot.plot(xspace, Fortranij, label = 'Fortranij')
plot.legend()
plot.title('Cij x Fortranij')
plot.show()


plot.plot(xspace, Cji, label = 'Cji')
plot.plot(xspace, Fortranji, label = 'Fortranji')
plot.legend()
plot.title('Cji x Fortranji')
plot.xlabel('Tamanho de uma das dimensões da matriz quadrada')
plot.ylabel('Tempo em segundos')
plot.show()


plot.plot(xspace, Cij, label = 'Cij')
plot.plot(xspace, Cji, label = 'Cji')
plot.plot(xspace, Fortranij, label = 'Fortranij')
plot.plot(xspace, Fortranji, label = 'Fortranji')
plot.legend()
plot.title('Cij x Cji x Fortranij x Fortranji')
plot.xlabel('Tamanho de uma das dimensões da matriz quadrada')
plot.ylabel('Tempo em segundos')
plot.show()








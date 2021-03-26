#Sabendo que a
#bactéria B se reproduz a cada 2 minutos, criando uma nova #bactéria. Sabendo que a cada geração apenas 80% das bactérias #sobrevivem
#para se reproduzir, responda: quantas bactérias
#existirão nesta colônia depois de 14 minutos? Sabendo que #inicialmente havia apenas 10 bactérias nesta
#colônia. 


import matplotlib.pyplot as plt
import numpy as np

def Populacao(bacterias,tempo):
  return bacterias * (2 * 0.8) ** (tempo/2)

bacterias = 10

bacterias = int(input("Insira as bactérias iniciais: "))

tempo = np.arange(0, 14.1, 0.1)

plt.grid(color='gray', linestyle='-.', linewidth=0.5)

plt.plot(tempo, Populacao(bacterias, tempo), linewidth=2.5, color='#ADF7B6', label=r'$População = bactéria \times  (2 * 0,8)^{(\frac{tempo}{2})}$')
plt.legend(loc='lower right')
plt.xlabel('Tempo')
plt.ylabel('População')
# mostar o gráfico
plt.show()
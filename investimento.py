#TDE pt 2
#
#Agora você precisa fazer um programa em Python, para calcular quanto terá investido 
#Se tiver uma taxa de juros de 1% ao mês
#partindo de R$1.000,00 
#investir R$100,00 todos os meses 
#por 35 anos.
#
#Só para lembrar, Em Python! Com Gráfico!
#
#Mande os links do Repl.it, ou Google Colab e não esqueça de colocar o nome dos integrantes dos grupos.  
import numpy as np
import matplotlib.pyplot as plt

Inicio = 1000 
InvestimentoMes = 100
Anos =  35
Meses = np.arange(1, Anos * 12, 1) # Anos * 12 + (35 % 4) pra incluir ano bissexto (imagino eu)
Juros = 0.01 #1%
def calculo():
    return Inicio + InvestimentoMes*Meses - (InvestimentoMes * Juros)*Meses

plt.grid(color='gray', linestyle='-.', linewidth=0.5)

plt.plot(Meses, calculo(), linewidth=2.5, color='#ADF7B6') #não entendi direito como latec funciona
plt.legend(loc='lower right')
plt.xlabel('Mês')
plt.ylabel('Rendimento')

# mostar o gráfico
plt.show()

#Teste com laço pra ver se ta certo
#Rendimento = Inicio
#contador = 0
#while(contador<Meses):
#    Rendimento = Rendimento + InvestimentoMes - (InvestimentoMes*Juros)
#    print(Rendimento)
#    contador += 1
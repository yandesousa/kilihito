
import pandas as pd
import matplotlib.pyplot as plt

# Carregar os dados do arquivo gasolina.csv
data = pd.read_csv('gasolina.csv')

# Criar o gráfico de linha
plt.plot(data['dia'], data['venda'], marker='o', color='b')

# Adicionar título e rótulos aos eixos
plt.title('Preço Médio da Gasolina em Julho de 2021 - São Paulo')
plt.xlabel('Dia')
plt.ylabel('Preço de Venda (R$/litro)')

# Adicionar grade ao fundo do gráfico
plt.grid(True)

# Salvar o gráfico no arquivo gasolina.png
plt.savefig('gasolina.png')

# Mostrar o gráfico
plt.show()
        
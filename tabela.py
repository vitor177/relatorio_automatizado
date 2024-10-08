import pandas as pd
from tabulate import tabulate

# Ler a tabela do Excel
df = pd.read_excel('RN06-2024-06_Relatório.xlsx', header=None)

# Selecionar o intervalo desejado (linhas 11-15, colunas B-E)
# Lembre-se que o Pandas utiliza indexação baseada em 0, por isso ajustamos as coordenadas
tabela_selecionada = df.iloc[10:15, 1:6]

# Converter o DataFrame selecionado para uma tabela no formato LaTeX
tabela_latex = tabulate(tabela_selecionada, headers='keys', tablefmt='latex', showindex=False)

# Exibir a tabela no formato LaTeX
print(tabela_latex)


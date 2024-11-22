import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# Caminho para o dataset principal
caminho_dataset = "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGData.csv"

# Carregar o dataset
dados = pd.read_csv(caminho_dataset)

# 1. Exibir informações básicas
print("Informações do dataset:")
print(dados.info())

# 2. Verificar valores ausentes
print("\nResumo de valores ausentes por coluna:")
print(dados.isnull().sum())

# 3. Remover colunas irrelevantes
colunas_irrelevantes = ["Unnamed: 66"]  # Ajuste se necessário
dados = dados.drop(columns=colunas_irrelevantes, errors="ignore")
print(f"\nColunas após remoção das irrelevantes: {dados.columns}")

# 3.1 Exploração de Outliers
# Analisar os valores mais altos para os anos de interesse
anos_interesse = ["1960", "1970", "1980", "1990", "2000", "2010", "2020"]

for ano in anos_interesse:
    if ano in dados.columns:
        print(f"\nValores mais altos para o ano {ano}:")
        print(dados[['Country Name', 'Country Code', ano]].sort_values(by=ano, ascending=False).head(10))

# 4. Verificar a distribuição dos dados (histograma para uma amostra de indicadores)
indicadores_para_visualizar = ["1960", "1970", "1980", "1990", "2000", "2010", "2020"]  # O ajuste é conforme os anos disponíveis

for indicador in indicadores_para_visualizar:
    if indicador in dados.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(dados[indicador].dropna(), kde=True, bins=30)
        plt.title(f"Distribuição de valores para o ano {indicador}")
        plt.xlabel("Valor")
        plt.ylabel("Frequência")
        plt.show()

# 5. Salvar o dataset limpo
caminho_saida = "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGData_clean.csv"
dados.to_csv(caminho_saida, index=False)
print(f"\nDataset limpo salvo em: {caminho_saida}")

# 6. Aplicar transformação logarítmica para anos específicos
anos_para_transformacao = ["1960", "1970", "1980", "1990", "2000", "2010", "2020"]

for ano in anos_para_transformacao:
    if ano in dados.columns:
        # Adicionar uma nova coluna com o sufixo '_log'
        coluna_log = f"{ano}_log"
        dados[coluna_log] = np.log1p(dados[ano])  # log1p para lidar com valores 0
        print(f"Transformação logarítmica aplicada para o ano {ano}")
        
# 7. Visualizar as distribuições transformadas
for ano in anos_para_transformacao:
    coluna_log = f"{ano}_log"
    if coluna_log in dados.columns:
        plt.figure(figsize=(10, 5))
        sns.histplot(dados[coluna_log].dropna(), kde=True, bins=30, color="blue")
        plt.title(f"Distribuição logarítmica de valores para o ano {ano}")
        plt.xlabel("Valor (log)")
        plt.ylabel("Frequência")
        plt.show()


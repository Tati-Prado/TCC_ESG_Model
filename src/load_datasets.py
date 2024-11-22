import pandas as pd
import os

# Caminhos para os arquivos
arquivos = {
    "ESGFootNote": "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGFootNote.csv",
    "ESGSeries-Time": "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGSeries-Time.csv",
    "ESGSeries": "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGSeries.csv",
    "ESGCountry-Series": "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGCountry-Series.csv",
    "ESGCountry": "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGCountry.csv",
    "ESGData": "/Users/tatiana.massoco/Desktop/TCC_ESG_Model/data/ESGData.csv"
}

# Verificar e carregar os arquivos
for nome, caminho in arquivos.items():
    print(f"Verificando o caminho: {caminho}")
    if os.path.exists(caminho):
        print(f"O arquivo {nome} existe. Carregando os dados...")
        try:
            dados = pd.read_csv(caminho)
            print(f"--- {nome} ---")
            print(f"Shape: {dados.shape}")
            print(f"Colunas: {list(dados.columns)}")
            print(f"Primeiras linhas:\n{dados.head()}\n")
        except Exception as e:
            print(f"Erro ao carregar {nome}: {e}")
    else:
        print(f"Erro: O arquivo {nome} não foi encontrado no caminho {caminho}.\n")


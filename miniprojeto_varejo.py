import pandas as pd

# Lendo a base de dados em formato CSV
df = pd.read_csv("Base Varejo.csv", sep=";")

# Informações gerais da base
print("=== INFORMAÇÕES GERAIS ===")
print("Quantidade de linhas e colunas:")
print(df.shape)

# Mostrando as colunas existentes
print("\nColunas da base:")
print(df.columns)

# Verificando os tipos de dados
print("\nTipos de dados:")
print(df.dtypes)

# Mostrando as primeiras linhas da base
print("\nPrimeiras linhas:")
print(df.head())

# Verificando valores nulos
print("\nValores nulos por coluna:")
print(df.isnull().sum())

# Verificando registros duplicados
print("\nQuantidade de linhas duplicadas:")
print(df.duplicated().sum())

# Removendo colunas totalmente vazias
df = df.drop(columns=["Unnamed: 10", "Unnamed: 11", "Unnamed: 12", "Unnamed: 13"])

# Removendo registros duplicados
df = df.drop_duplicates()

print("\nQuantidade de linhas após remover duplicatas:")
print(df.shape)

# Tratando categorias sem informação usando if/else
if "#N/D" in df["PR_CAT"].values:
    df["PR_CAT"] = df["PR_CAT"].replace("#N/D", "Sem Categoria")
    print("\nCategorias '#N/D' foram substituídas por 'Sem Categoria'.")
else:
    print("\nNão foram encontradas categorias '#N/D'.")

# Garantindo que nenhuma coluna Unnamed permaneça
df = df.loc[:, ~df.columns.str.contains("Unnamed")]

print("\nColunas após limpeza:")
print(df.columns)

# Convertendo a coluna DATA para formato de data
df["DATA"] = pd.to_datetime(df["DATA"], dayfirst=True)

print("\nTipo da coluna DATA:")
print(df["DATA"].dtype)

# Estatísticas da coluna CL_FHL
print("\n=== ESTATÍSTICAS DA COLUNA CL_FHL ===")

print("Média:", df["CL_FHL"].mean())
print("Mediana:", df["CL_FHL"].median())
print("Moda:", df["CL_FHL"].mode()[0])
print("Máximo:", df["CL_FHL"].max())
print("Mínimo:", df["CL_FHL"].min())
print("Desvio padrão:", df["CL_FHL"].std())
print("Contagem:", df["CL_FHL"].count())

# Quartis
print("\nQuartis:")
print(df["CL_FHL"].quantile([0.25, 0.50, 0.75]))

# Agrupamento por gênero
print("\n=== AGRUPAMENTO POR GÊNERO ===")
print(df.groupby("CL_GENERO").size())

# Agrupamento por categoria de produto
print("\n=== AGRUPAMENTO POR CATEGORIA DE PRODUTO ===")
print(df.groupby("PR_CAT").size().sort_values(ascending=False))

# Salvando a base limpa
df.to_csv("df_limpo.csv", index=False)

print("\nArquivo df_limpo.csv gerado com sucesso!")
# Mini Projeto - Análise Exploratória de Dados de Varejo

## Sobre o Projeto

Este projeto foi desenvolvido com o objetivo de aplicar na prática conceitos de Análise de Dados utilizando Python e a biblioteca Pandas.

A proposta consistiu em realizar uma análise exploratória de uma base de dados de varejo, passando pelas etapas de importação, identificação de problemas, limpeza, tratamento e análise dos dados.

## Tecnologias Utilizadas

- Python
- Pandas
- Visual Studio Code
- GitHub

## Etapas Desenvolvidas

### Importação da Base de Dados

- Leitura do arquivo CSV utilizando Pandas.
- Verificação da estrutura da base.
- Identificação da quantidade de registros e colunas.

### Análise Inicial

Foram realizadas verificações para identificar possíveis problemas nos dados:

- Quantidade de linhas e colunas.
- Tipos de dados de cada coluna.
- Valores nulos por coluna.
- Registros duplicados.
- Possíveis inconsistências nas categorias de produtos.

### Limpeza e Tratamento dos Dados

Durante a análise foram identificadas quatro colunas totalmente vazias:

- Unnamed: 10
- Unnamed: 11
- Unnamed: 12
- Unnamed: 13

Como essas colunas não possuíam informações úteis para a análise, foi realizada a remoção delas em vez do preenchimento dos valores.

Também foram encontrados 96.553 registros duplicados, que foram removidos para evitar distorções nos resultados.

Outra inconsistência identificada foi a presença de 3.228 registros classificados como "#N/D" na categoria de produto. Esses registros foram tratados utilizando uma estrutura condicional, sendo substituídos por "Sem Categoria".

Além disso, a coluna DATA estava armazenada como texto e foi convertida para o formato datetime.

### Estatísticas Descritivas

Foi realizada uma análise estatística da coluna CL_FHL, que representa a quantidade de filhos dos clientes.

Resultados encontrados:

- Média: 1,15
- Mediana: 0
- Moda: 0
- Valor mínimo: 0
- Valor máximo: 4
- Desvio padrão: 1,42
- Contagem: 733.447 registros

Quartis:

- Q1: 0
- Q2: 0
- Q3: 2

### Agrupamentos Realizados

#### Distribuição por Gênero

- Feminino: 382.427 registros
- Masculino: 351.020 registros

#### Distribuição por Categoria de Produto

- Alimentos: 384.197 registros
- Higiene: 137.702 registros
- Limpeza: 128.632 registros
- Bebidas: 38.264 registros
- Pet: 28.553 registros
- Acessórios: 12.871 registros
- Sem Categoria: 3.228 registros

## Resultados Obtidos

### Situação Inicial da Base

- Registros: 830.000
- Colunas: 14

### Situação Após a Limpeza

- Registros válidos: 733.447
- Colunas úteis: 10
- Duplicatas removidas: 96.553

## Principais Conclusões

- A categoria Alimentos apresentou a maior quantidade de registros na base analisada.
- Foram encontrados 96.553 registros duplicados, mostrando a importância da limpeza dos dados antes das análises.
- A maior parte dos clientes cadastrados não possui filhos, conforme indicado pela mediana e moda iguais a zero.
- Houve uma quantidade ligeiramente maior de registros do gênero feminino.
- O tratamento das inconsistências e a remoção de dados desnecessários contribuíram para uma análise mais confiável.
- A qualidade dos dados influencia diretamente os resultados obtidos em qualquer processo analítico.s 
 
## Aprendizados

Este projeto foi muito importante para o meu aprendizado, principalmente por estar iniciando meus estudos na área de Análise de Dados.

Durante o desenvolvimento tive contato com etapas que fazem parte do processo de ETL: extração, transformação e carga de dados. A base foi carregada a partir de um arquivo CSV, passou por etapas de limpeza e transformação dos dados e, ao final, foi gerada uma nova versão tratada da base.

Também pude compreender melhor a importância da qualidade dos dados, percebendo como colunas vazias, registros duplicados e informações inconsistentes podem impactar diretamente os resultados de uma análise.

Além do aprendizado técnico, o projeto contribuiu para desenvolver meu raciocínio analítico, atenção aos detalhes e interesse pela área de dados.
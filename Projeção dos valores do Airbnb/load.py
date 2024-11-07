# Databricks notebook source
# MAGIC %md
# MAGIC ### Lendo o arquivo csv e transformando em dataframe (df)

# COMMAND ----------

df = pd.read_csv('Dados detalhados de listings do RJ.csv')

# COMMAND ----------

#Verificando como ficou os dados
display(df)

# COMMAND ----------

# MAGIC %md
# MAGIC ### Removendo as colunas do dataframe
# MAGIC
# MAGIC - axis = 1 é para as colunas 
# MAGIC - axis = 0 é para as linhas
# MAGIC - inplace = True é para manter o mesmo nome dessa variável 

# COMMAND ----------

df.drop(["neighbourhood_group","reviews_per_month","calculated_host_listings_count","number_of_reviews_ltm","license"],axis = 1, inplace =True)

# COMMAND ----------

#Verificando o novo dataframe
df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Renomeando as colunas

# COMMAND ----------

df.rename(columns={
    "id":"ID_Imóvel",
    "name":"Descrição",
    "host_id":"ID_Anfitrião",
    "host_name":"Nome_Anfitrião",
    "neighbourhood":"Bairro",
    "latitude":"Latitude",
    "longitude":"Longitude",
    "room_type":"Tipo",
    "price":"Preço",
    "minimum_nights":"Mínimo_noites",
    "number_of_reviews":"Nº_revisões",
    "last_review":"Última_revisão",
    "availability_365":"Disponibilidade_anual"
 }, inplace= True)

# COMMAND ----------

df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC ### Redefinindo os tipos das colunas

# COMMAND ----------

df['ID_Imóvel'] = df['ID_Imóvel'].astype(str)
df['ID_Anfitrião'] = df['ID_Anfitrião'].astype(str)
df['Latitude'] = df['Latitude'].astype(float)
df['Longitude'] = df['Longitude'].astype(float)
df['Mínimo_noites'] = df['Mínimo_noites'].astype(int)
df['Última_revisão'] = pd.to_datetime(df['Última_revisão'])

# COMMAND ----------

# Deixando no dataframe as estadias mais ativas de acordo com a última revisão, com uma data inicial de 01-01-2023 até atualmente. 
datas = (df['Última_revisão'] >= '2023-01-01')

df_filtrado = df[datas]

# COMMAND ----------

print("A quantidade de linhas filtradas são:",df.shape[0] - df_filtrado.shape[0])

# COMMAND ----------

df_filtrado.dropna(inplace= True)

# COMMAND ----------

df.head()
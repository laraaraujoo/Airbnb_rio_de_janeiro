# Databricks notebook source
# MAGIC %md
# MAGIC Soma dos valores ausentes ou null nas colunas 

# COMMAND ----------

df.isnull().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC Removi as linhas null do dataframe

# COMMAND ----------

df.dropna(subset=["Preço","Última_revisão"], inplace =True)

# COMMAND ----------

# MAGIC %md
# MAGIC Verificando se realmente foi removido as linhas null da coluna Preço e Última_revisão

# COMMAND ----------

df.isnull().sum()

# COMMAND ----------

# MAGIC %md
# MAGIC Agrupar os bairros, mostrando a latitude e longitude, assim vejo o preço por bairro

# COMMAND ----------

df.groupby(['Latitude','Longitude']).sum()

# COMMAND ----------

# MAGIC %md
# MAGIC Limitando a quantidade de números em cada coluna.

# COMMAND ----------

df.round(4).head()
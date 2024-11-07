# Databricks notebook source
df.info()

# COMMAND ----------

# MAGIC %md
# MAGIC Separação do feature e target

# COMMAND ----------

label_encoder = LabelEncoder()
X = label_encoder.fit_transform(df['Bairro'])
y = df['Preço']

# COMMAND ----------

# MAGIC %md
# MAGIC Separando o conjunto de dados com treino e teste 

# COMMAND ----------

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y,random_state=42) 

# COMMAND ----------

# MAGIC %md
# MAGIC Criação do dummyregressor, essa lib vai considerar a média
# MAGIC - media 
# MAGIC - mediana
# MAGIC - quartil 
# MAGIC - constante

# COMMAND ----------

from sklearn.dummy import DummyRegressor

model_dummy = DummyRegressor()

model_dummy.fit(X_train, y_train)

# COMMAND ----------

y_pred_dummy = model_dummy.predict(X_test)

# COMMAND ----------

# MAGIC %md
# MAGIC Essa é a média do nosso conjunto de treinamneto

# COMMAND ----------

y_pred_dummy

# COMMAND ----------

# MAGIC %md
# MAGIC Métricas para saber se nosso modelo está se ajustando
# MAGIC - Quando esse parametro é TRUE (squared=True) o MSe vai retornar e se for TRUE (squared=False) vai retornar RMSE
# MAGIC

# COMMAND ----------

from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

def calcular_metrica_regressao(y_test, y_pred):
  rmse = mean_squared_error(y_test, y_pred, squared=False)
  mae = mean_absolute_error(y_test, y_pred)
  r2 = r2_score(y_test, y_pred)

  metricas = {
    'Raiz do Erro Quadrático Médio': round(rmse,4),
    'Erro Médio Absoluto': round(mae,4),
    'R2 score': round(r2,4)
    }
  
  return metricas

# COMMAND ----------

df['bairro_codificado'] = label_encoder.fit_transform(df['Bairro'])
 

# COMMAND ----------

df['Tipo_airbnb'] = label_encoder.fit_transform(df['Tipo'])
 

# COMMAND ----------

# MAGIC %md
# MAGIC Em média o modelo ta errando ... 

# COMMAND ----------

calcular_metrica_regressao(y_test, y_pred_dummy)

# COMMAND ----------

# MAGIC %md
# MAGIC ------
# MAGIC

# COMMAND ----------

X = label_encoder.fit_transform(df['Bairro'])

# COMMAND ----------

X_train, X_test, y_train, y_test = train_test_split(X, y,test_size=0.3, random_state=0) 

# COMMAND ----------

X_train

# COMMAND ----------

#definindo o algoritmo utilizado
LinearRegressionModel = LinearRegression()

# COMMAND ----------

# #treinando o algoritmo com a base de treino
y_train = y_train.values.reshape(-1, 1) 

# COMMAND ----------

# MAGIC %md
# MAGIC ####Removi as colunas que não irei utilizar

# COMMAND ----------

df.drop(["Descrição","Nome_Anfitrião","Nº_revisões","Última_revisão","Disponibilidade_anual"], axis = 1, inplace = True)

# COMMAND ----------

# MAGIC %md
# MAGIC ####Mostrando como ficou

# COMMAND ----------

df.head()

# COMMAND ----------

# MAGIC %md
# MAGIC Criando uma matriz, colunas será o id do imóvel, o index será os bairros e os preços será os valores (os resultados dentro da matriz). Então, no bairro 0 temos todos esses Id de imóveis com os seus respectivos preços. 

# COMMAND ----------

df_pivot =  df.pivot(columns="ID_Imóvel", index="bairro_codificado", values="Preço") 

# COMMAND ----------

df_pivot.head()

# COMMAND ----------

# MAGIC %md
# MAGIC Para esse ML vamos trocar o NaN por ZERO (0)

# COMMAND ----------

df_pivot.fillna(0,inplace = True)

# COMMAND ----------

# MAGIC %md
# MAGIC Verificando como ficou...

# COMMAND ----------

df_pivot.head(30)

# COMMAND ----------

# MAGIC %md
# MAGIC Criarmos uma matriz sparse e vamos transformar o nosso dataframe 

# COMMAND ----------

from scipy.sparse import csr_matrix
df_sparse = csr_matrix(df_pivot)

# COMMAND ----------

# MAGIC %md
# MAGIC Crinado e treinado o nosso modelo preditivo

# COMMAND ----------

from sklearn.neighbors import NearestNeighbors
modelo = NearestNeighbors(algorithm='brute')
modelo.fit(df_sparse)

# COMMAND ----------

df_pivot.head()

# COMMAND ----------

df_pivot.dropna(inplace = True)

# COMMAND ----------

df_pivot.isna().sum()

# COMMAND ----------

valores_airbnb = df_pivot.loc[df_pivot['1000145542988583943'] > 100 ]

# COMMAND ----------

valores_airbnb
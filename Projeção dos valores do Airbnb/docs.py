# Databricks notebook source
# MAGIC %md
# MAGIC ### Instalação e importação das LIBS 

# COMMAND ----------

pip install wget

# COMMAND ----------

pip install lightfm

# COMMAND ----------

pip install scikit-surprise

# COMMAND ----------

import wget
import pandas as pd
import matplotlib.pyplot as plt
import os
import numpy as np
import seaborn as sns
import lightfm
import surprise
import sklearn as sl
from datetime import datetime
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error
from surprise import Dataset, Reader
from surprise.prediction_algorithms.matrix_factorization import SVD
from surprise import accuracy
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
from sklearn.dummy import DummyRegressor
from sklearn.ensemble import RandomForestRegressor

# COMMAND ----------

# MAGIC %md
# MAGIC ### Download do arquivo

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Arquivo da internet
# MAGIC
# MAGIC Fazendo o download de um arquivo da internet
# MAGIC
# MAGIC - Primeiro eu informo o link e em seguida utilizo o recurso wget.download para fazer o download do arquivo que preciso
# MAGIC - Wget pode ser utilizado para baixar arquivos : PDF, CSV, JPG, TXT, PNG

# COMMAND ----------

if os.path.exists('Dados detalhados de listings do RJ.csv') == True:
    """ Fazendo um download csv de um site """
    print('O arquivo já existe')
else:
    link = 'https://data.insideairbnb.com/brazil/rj/rio-de-janeiro/2024-06-27/visualisations/listings.csv'
    wget.download(link,'Dados detalhados de listings do RJ.csv')
    """Verificando se o download foi realizado com sucesso"""
    print ('Download realizado com sucesso!')


# COMMAND ----------

# Local que foi salvo o arquivo
caminho = os.getcwd()
print(f'Esse é o caminho que está o arquivo: {caminho}')

# COMMAND ----------

# MAGIC %md
# MAGIC
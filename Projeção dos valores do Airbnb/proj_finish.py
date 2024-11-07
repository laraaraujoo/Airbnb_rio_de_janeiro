# Databricks notebook source
# MAGIC %md
# MAGIC ###Informações do projeto

# COMMAND ----------

# MAGIC %md
# MAGIC ##### Descrição de cada coluna
# MAGIC
# MAGIC - id = identificação
# MAGIC - name = nome
# MAGIC - host_id = identificação do anfitrião
# MAGIC - host_name = nome de anfitrião
# MAGIC - neighbourhood_group = bairro_grupo
# MAGIC - neighbourhood = vizinhança
# MAGIC - latitude = latitude
# MAGIC - longitude = longitude
# MAGIC - room_type = tipo de sala
# MAGIC - price = preço
# MAGIC - minimum_nights = mínimo_noites
# MAGIC - number_of_reviews = número_de_revisões
# MAGIC - last_review = última_revisão
# MAGIC - reviews_per_month = avaliações_por_mês
# MAGIC - calculated_host_listings_count = calculado_host_listings_count
# MAGIC - availability_365 = disponibilidade_365
# MAGIC - number_of_reviews_ltm = número_de_avaliações_em_meses
# MAGIC - license = licença

# COMMAND ----------

# MAGIC %md
# MAGIC ###Qual o objetivo do projeto ?

# COMMAND ----------

# MAGIC %md
# MAGIC O objetivo inicial é saber qual o valor do m² em cada região para alugar imóveis de temporada.

# COMMAND ----------

# MAGIC %md
# MAGIC ####Quais dados são necessários ?

# COMMAND ----------

# MAGIC %md
# MAGIC Os dados necessários estão sendo extraido de um site Airbnb, são eles:
# MAGIC - Valores 
# MAGIC - Bairros
# MAGIC - Latitude
# MAGIC - Longitude
# MAGIC - Descrição
# MAGIC - Imóvel
# MAGIC - ID
# MAGIC - Nome
# MAGIC - Avaliações

# COMMAND ----------

# MAGIC %md
# MAGIC ####Qual é a média do mínimo de noites na cidade do Rio de Janeiro?

# COMMAND ----------

min = df['Mínimo_noites'].mean().round()

# COMMAND ----------

print(f'O mínimo de noite para alugar um imóvel de temporada no RJ é de {int(min)} noites')

# COMMAND ----------

# MAGIC %md
# MAGIC ####Quais bairros tem mais imóveis para alugar?

# COMMAND ----------

city = df['Bairro'].mode()

# COMMAND ----------

estadias = df.groupby('Bairro').size().reset_index(name='Quantidade')

estadias = estadias.sort_values(by='Quantidade', ascending=False)

qtd_estadia = estadias.set_index('Bairro') 

# COMMAND ----------

qtd_estadia

# COMMAND ----------

print(f'O bairro {qtd_estadia.index[0]} no RJ é a região com {qtd_estadia["Quantidade"][0]} para locação de estadias')

# COMMAND ----------

#plt.figure(figsize=(17,5))
ax = qtd_estadia.head(15).plot.bar(color='g', ec='k', alpha=0.4)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('',fontsize =12)
plt.ylabel('Estadias', fontsize= 12)

def add_labels(ax):
    for p in ax.patches:   # retorna todos os retângulos das barras no gráfico.
        height = p.get_height() # obtém a altura de cada barra.
        width = p.get_width() # obtém a largura de cada barra
        x = p.get_x() + width / 2 # Calcula a posição horizontal central da barra.
        y = p.get_y() + height / 2 # Calcula a posição vertical central da barra.

        if height > 0:
            # Ajustar a posição do texto dentro da barra
            ax.annotate(f'{int(height)}',
                        (x, y),
                        ha='center', va='center', # Centraliza o texto dentro da barra.
                        fontsize=7,
                        color='black'
            )
add_labels(ax)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Existe uma correlação entre latitude e longitude com preço?

# COMMAND ----------

correlação = df.corr()

# COMMAND ----------

sns.heatmap(correlação)
ax.set_xticks([]) #remover o axes que estava aparecendo encima do gráfico
ax.set_yticks([])
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Quais são os 10 principais ID dos anfitriões com mais listagens?

# COMMAND ----------

df

# COMMAND ----------

registros_id = df.groupby('ID_Anfitrião').size().reset_index(name='Imóvel')
registros_id = registros_id.sort_values(by='Imóvel', ascending=False)
registros_id.set_index('ID_Anfitrião', inplace=True)

# COMMAND ----------

registros_id.head(10).plot.bar(color='b', ec='k', alpha=1.0)
plt.xticks(rotation=90, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('ID',fontsize =12)
plt.ylabel('Quantidade', fontsize= 12)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Qual a porcentagem do tipo de quarto nos anúncios do Airbnb?

# COMMAND ----------

#Convertendo em porcentual
qtdtipo = df['Tipo'].value_counts(normalize=True)*100

# COMMAND ----------

plt.figure(figsize=(9,6))
qtdtipo.plot.bar(color='c',ec='k', alpha=1.0)
for index, value in enumerate(qtdtipo):
    plt.text(index, value, f'{value:.2f}', ha='center', va='bottom', fontsize=8)

plt.xticks(rotation=360, fontsize=12)
plt.yticks(fontsize=12)
plt.xlabel('Tipo de quarto',fontsize =12)
plt.ylabel('Percentual', fontsize= 12)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Histogramas

# COMMAND ----------

df.hist(bins=15, figsize=(15,10))
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Ranking dos preços por bairros

# COMMAND ----------

# MAGIC %md
# MAGIC Agrupamos os bairros e fizemos a mediana dos preços de cada bairro. 

# COMMAND ----------

median_preco = df.groupby(['Bairro'])['Preço'].median()

# COMMAND ----------

median_preco=median_preco.sort_values(ascending=False).round(2)

# COMMAND ----------

fig, ax = plt.subplots(figsize=(8, 8))
bars = ax.barh(median_preco[0:15].index, median_preco[0:15].values)
for bar in bars:
    width = bar.get_width()
    label = f'{int(width)}'  # Formato do valor; ajuste conforme necessário
    ax.text(width - (width * 0.50), bar.get_y() + bar.get_height()/2, label,
            va='center', ha='left')
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Top 10 dos preços médios por bairro 

# COMMAND ----------

medio_preco = df.groupby(['Bairro'])['Preço'].mean()

# COMMAND ----------

medio_preco = medio_preco.head(10)

# COMMAND ----------

fig, ax = plt.subplots(figsize=(15, 5))
plt.plot(medio_preco.index, medio_preco.values, marker='o')
plt.title('Preço Médio por Bairro')
plt.xticks(rotation=45)
plt.show()

# COMMAND ----------

# MAGIC %md
# MAGIC ####Quais as medianas dos preços dos aluguéis para cada tipo de imóvel?

# COMMAND ----------

median_entire = df[df['Tipo'] == 'Entire home/apt']['Preço'].median()
median_private = df[df['Tipo'] == 'Private room']['Preço'].median()
median_shared = df[df['Tipo'] == 'Shared room']['Preço'].median()
median_hotel = df[df['Tipo'] == 'Hotel room']['Preço'].median()

# COMMAND ----------

print('Preços medianos')

print(f'Casa/apartamento R$ {median_entire}')

print(f'Quarto privado R$ {median_private}')

print(f'Quarto compartilhado R$ {median_shared}')

print(f'Quarto de hotel R$ {median_hotel}')
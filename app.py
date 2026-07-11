from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import streamlit as st

st.set_page_config(page_title='EDA Veículos', layout='wide')

BASE_DIR = Path(__file__).resolve().parent
DATA_PATH = BASE_DIR / 'vehicles.csv'

if not DATA_PATH.exists():
    raise FileNotFoundError(f'Arquivo de dados não encontrado: {DATA_PATH}')


@st.cache_data
def load_data():
    return pd.read_csv(DATA_PATH)


data = load_data()


st.header('Análise Exploratória de Dados (EDA) - Conjunto de Dados de Anúncios de Vendas de Carros')
st.write('Este aplicativo realiza uma análise exploratória de dados (EDA) no conjunto de dados de anúncios de vendas de carros. O objetivo é fornecer insights sobre a distribuição dos preços dos veículos e outras informações relevantes.')
st.write('Gabriel Taujiro - Projeto Final - Sprint 5 - Data Analysis')

hist_button = st.button('Criar histograma') # criar um botão
        
if hist_button: # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    # criar um histograma
    plt.figure(figsize=(12, 7))
    sns.histplot(data['price'], bins=50)
    plt.title('Distribuição Geral dos Preços dos Veículos')
    plt.xlabel('Preço (USD)')
    plt.ylabel('Frequência')
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    plt.show()
    # exibir um gráfico Plotly interativo
    st.pyplot(plt.gcf())


analysis0_button = st.button('Relação entre Odômetro e Preço') # criar um botão

if analysis0_button: # se o botão for clicado
    plt.figure(figsize=(12, 7))
    sns.scatterplot(x='odometer', y='price', data=data, alpha=0.6)
    plt.title('Relação entre Odômetro e Preço do Veículo')
    plt.xlabel('Odômetro (Milhas)')
    plt.ylabel('Preço (USD)')
    plt.grid(True, linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt.gcf())


analysis1_button = st.button('Distribuição de Preço por Tipo de Veículo') # criar um botão

if analysis1_button: # se o botão for clicado
    st.write('Criando um gráfico de distribuição de preço por tipo de veículo')
    mean_price_by_type = data.groupby('type')['price'].mean().reset_index()
    plt.figure(figsize=(12, 7))
    sns.barplot(x='type', y='price', data=mean_price_by_type)
    plt.title('Distribuição de Preço por Tipo de Veículo')
    plt.xlabel('Tipo de Veículo')
    plt.ylabel('Preço (USD)')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt.gcf())


analysis2_button = st.button('Contagem de Veículos por Condição') # criar um botão

if analysis2_button: # se o botão for clicado
    plt.figure(figsize=(10, 6))
    sns.countplot(y='condition', data=data, order=data['condition'].value_counts().index)
    plt.title('Contagem de Veículos por Condição')
    plt.xlabel('Número de Veículos')
    plt.ylabel('Condição')
    plt.grid(axis='x', linestyle='--', alpha=0.7)
    plt.tight_layout()
    st.pyplot(plt.gcf())
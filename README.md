# sprint_5

# Projeto de Análise de Dados de Veículos

Este projeto realiza uma análise exploratória de dados de anúncios de veículos, focando em visualizações para entender as características e tendências do mercado automotivo.

## Conjunto de Dados

O dataset utilizado é `vehicles.csv`, contendo informações diversas sobre veículos anunciados, como preço, tipo, odômetro, condição, etc.

## Análises Realizadas

Foram desenvolvidas as seguintes análises visuais:

1.  **Distribuição de Preço por Tipo de Veículo:** Gráfico de barras que mostra o preço médio para diferentes tipos de veículos, identificando variações de preço entre categorias.
2.  **Relação entre Odômetro e Preço:** Gráfico de dispersão para explorar a correlação entre a quilometragem (odômetro) e o preço de venda do veículo, buscando padrões de desvalorização.
3.  **Contagem de Veículos por Condição:** Gráfico de contagem que apresenta a frequência de veículos em diferentes estados de conservação (e.g., 'good', 'excellent', 'like new').
4.  **Distribuição Geral dos Preços:** Histograma que ilustra a distribuição total dos preços dos veículos no dataset, revelando as faixas de preço mais comuns.

## Ferramentas e Bibliotecas

O projeto utiliza as seguintes bibliotecas Python:

*   `pandas`: Para manipulação e análise de dados.
*   `seaborn` e `matplotlib.pyplot`: Para a criação de visualizações estatísticas.
*   `streamlit`: Para compatibilidade e futura integração em um aplicativo web interativo.

## Execução

Os gráficos foram adaptados para serem compatíveis com o Streamlit, utilizando `st.pyplot(plt.gcf())`. Para executar e visualizar este projeto:

1.  Certifique-se de ter o `streamlit` instalado (`!pip install streamlit`).
2.  Execute as células do notebook sequencialmente. Os gráficos serão gerados no formato compatível com o Streamlit.

## Links

Repositório: https://github.com/Taujiro/sprint_5/
Render: https://sprint-5-og3x.onrender.com

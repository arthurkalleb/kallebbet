import streamlit as st
import pandas as pd
from datetime import datetime

if "data" not in st.session_state:
    df_data = pd.read_csv("datasets/CLEAN_FIFA23_official_data.csv", index_col=0)
    df_data = df_data[df_data["Contract Valid Until"] >= datetime.today().year]
    df_data = df_data[df_data["Value(£)"] > 0]
    df_data = df_data.sort_values(by="Overall", ascending=False)
    st.session_state["data"] = df_data

st.title('_Kalleb_:blue[BET] ⚽')
st.sidebar.markdown("Desenvolvido por: Arthur Kalleb")

st.link_button("Acesse as informações no Kaggle", "https://www.kaggle.com/datasets/stefanoleone992/fifa-23-complete-player-dataset")

st.markdown(
    """
Os conjuntos de dados fornecidos incluem os dados dos jogadores do Modo Carreira do FIFA 15 ao FIFA 23. Os dados permitem comparações múltiplas para os mesmos jogadores nas últimas 9 versões do videogame.
Algumas ideias de possíveis análises:

Comparação histórica entre Messi e Ronaldo (quais atributos de habilidade mudaram mais ao longo do tempo - em comparação com estatísticas da vida real);

Orçamento ideal para criar uma equipa competitiva (ao nível das melhores n equipas da Europa) e altura em que o orçamento não permite comprar jogadores significativamente melhores para a escalação de 11 homens. Um extra é a mesma comparação com o atributo Potencial para a escalação em vez do atributo Geral;

Análise de amostra dos n% melhores jogadores (por exemplo, os 5% melhores jogadores) para ver se alguns atributos importantes como Agilidade, Controle de Bola ou Força foram populares ou não nas versões FIFA.
"""
)
import streamlit as st
import pandas as pd
import time
from core.storage import carregar

st.set_page_config(page_title="Votação em Tempo Real", layout="centered")
st.title("📊 Votação dos Alunos")

placeholder = st.empty()

while True:
    dados = carregar()

    totais = dados["totais"]
    alunos = dados["por_aluno"]

    df = pd.DataFrame(
        list(totais.items()),
        columns=["Alternativa", "Votos"]
    )

    with placeholder.container():
        st.subheader("Totais por alternativa")
        st.bar_chart(df.set_index("Alternativa"))

        st.subheader("Respostas por aluno")
        st.table(pd.DataFrame(
            alunos.items(),
            columns=["Aluno", "Resposta"]
        ))

    time.sleep(1)

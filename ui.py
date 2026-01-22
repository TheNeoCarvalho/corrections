import streamlit as st

class UI:
    def __init__(self):
        st.set_page_config(page_title="Votação em Tempo Real")
        st.title("📊 Votação dos Alunos")

    def atualizar(self, votos, percentuais):
        st.subheader("Votos")
        st.bar_chart(votos)

        st.subheader("Percentuais")
        st.write(percentuais)

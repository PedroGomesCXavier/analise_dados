import streamlit as st
import pandas as pd

st.write("Ola munde")

nome = "Pedro"
idade = 19
soma = 0
st.write(nome,idade)



st.title("Meu Primeiro Dash")
st.subheader(" Eustáquio Martins ASAMAGALHAE")


df = pd.DataFrame({
   'first column': ["Portugues","Matematica","Python","Frame"],
   'second column': [5, 9, 7, 10]
 })  

st.write(df)

st.text_input("oi")

supermercado = {
    "Leite": 40,
    "Carne": 20,
    "Ovo": 1,
    "Abobora": 20,
    "Panana": 30,
    "Mânga": 21,
}


produtos_escolhidos = st.multiselect(
    "Selecione os produtos para ver o preço total:",
    options=list(supermercado.keys())
)


def calcularPreco(itens_selecionados):
    soma = 0
    for produto in itens_selecionados:
        soma += supermercado[produto]  
    return soma


total = calcularPreco(produtos_escolhidos)

st.title(f"O total do preço é R$ {total}")
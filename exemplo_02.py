import streamlit as st

image = st.file_uploader("Uma imagem", type=["jpg", "jpeg"])
text = st.text_input("Sua marca dágua")
color = st.selectbox(
    'Cor da sua marca dagua', ['black', 'white', 'red', 'green']
)
font_size = st.number_input('Tamanho da Fonte', min_value=50)

if image:
    result = st.button(
        "Aplicar", type='primary'
    )
else:
    st.warning("Ainda não temos imagem")
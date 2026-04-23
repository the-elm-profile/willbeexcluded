import streamlit as st

with st.sidebar:
    st.header('Exemplo')
    escolha = st.checkbox('Escolha aluno', ['Gian Li', 'Felipinho'])
if escolha = 'Gian Li':
    st.title('Gian Li')
    st.info('Alguma inforcao se necessario')
    st.info('Apareceria um quadrado com as informacoes do rapaz em questao')
    st.button('Gerar relatorio')
else:
    st.title('Felipinho')
    st.info('Inforcao do Felipe')
    st.info('Area com as inforcacoes do aluno, para ser visualizada, editada, etc')
    st.button('Gerar relatorio')

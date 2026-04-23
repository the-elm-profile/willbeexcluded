import streamlit as st
st.title('None do aplicativo - ainda nao pensei sobre')
with st.sidebar:
    st.header('Exemplo')
    escolha = st.selectbox('Escolha aluno', ['Aluno', 'Gian Li', 'Felipinho'])
if escolha == 'Aluno':
    st.info('Selectione um aluno para visualizar seus dados.')
    st.warning('Cuido com o fogo Felipe')
elif escolha == 'Gian Li':
    st.title('Gian Li')
    st.info('Alguma inforcao se necessario')
    st.info('Apareceria um quadrado com as informacoes do rapaz em questao')
    st.button('Gerar relatorio')
else:
    st.title('Felipinho')
    st.info('Inforcao do Felipe')
    st.info('Area com as inforcacoes do aluno, para ser visualizada, editada, etc')
    st.button('Gerar relatorio')

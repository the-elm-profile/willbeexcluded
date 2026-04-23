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
    st.info('Apareceria um quadrado com as informacoes do rapaz em questao:')
    st.info('Compareceu na aula:')
    dia1 = st.selectbox('Terca-feira - 07/04/2026', False)
    dia2 = st.selectbox('Quinta-feita - 09/04/2026', False)
    if st.button('Gerar relatorio'):
        if dia1 is True and dia2 is True:
            st.write('Ele veio dia 07/04/2026 e 09/04/2026')
        if dia2 is True and dia1 is False:
            st.write('Ele veio so dia 09/04/2026')
        if dia1 is True and dia2 is False:
            st.write('Ele veio so dia 07/04/2026')
        else:
            st.error('ele nao veio nenhum dia')
else:            
    st.title('Felipinho')
    st.info('Inforcao do Felipe')
    st.info('Area com as inforcacoes do aluno, para ser visualizada, editada, etc')
    st.button('Gerar relatorio')

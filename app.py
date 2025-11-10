from controller.usuario_controller import cadastrar_usuario, obter_usuario
import streamlit as st
from controller.livro_controller import cadastrar_livro, obter_livros
from dados.database import criar_tabela

# Cria tabela na inicialização
criar_tabela()

st.title("Cadastro de Livros")

# Formulário
st.subheader("Adicionar novo livro")
with st.form ("form_livro"):
    isbn = st.text_input("ISBN")
    titulo = st.text_input("Título")
    submitted = st.form_submit_button("Cadastrar")

    if submitted:
        mensagem = cadastrar_livro(isbn, titulo)
        st.success(mensagem) 

#Listagem
st. subheader ("Livros cadastrados") 
livros = obter_livros()

if livros:
    for L in livros:
        st.write(f"**ISBN:** {L[0]} | ** Título:**{L[1]}")
else:        
        st.info("Nenhum livro cadastrado ainda.")


st.title("Gestão de usuario")

# Formulário Usuário
st.subheader("Adicionar novo usuário")
with st.form("form_usuario"):
    cpf = st.text_input("CPF do Usuário")
    nome_usuario = st.text_input("Nome do Usuário")
    submitted_usuario = st.form_submit_button("Cadastrar Usuário")

    if submitted_usuario:
         mensagem =  cadastrar_usuario(cpf, nome_usuario)
         st.success(mensagem)

# Listagem Usuários
st.subheader("Usuários cadastrados")
usuarios =obter_usuario()

if usuarios:
    for U in usuarios:
        st.write(f"**CPF:** {U[0]} | **Nome:** {U[1]}")
else:
    st.info("Nenhum usuário cadastrado ainda.")
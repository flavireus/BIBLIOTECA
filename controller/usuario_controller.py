from model.usuario_modelo import Usuario
from service.usuario_service import salvar_usuario, listar_usuario

def cadastrar_usuario(cpf,nome):
     if not cpf or not nome:
          return "Preencha todos os campos"
     usuario = Usuario(cpf,nome)
     try:
         salvar_usuario(usuario)
         return f" Usuario '{nome}' cadastrado com sucesso!"
     except Exception as e:
          return f" Erro ao cadastrar: {e}"
def obter_usuario():
     return listar_usuario()     
     








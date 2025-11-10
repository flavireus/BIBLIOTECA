from dados.database import conectar

def salvar_usuario(usuario):
    conn = conectar ()
    cursor = conn.cursor()
    cursor.execute ("INSERT INTO usuario (cpf,nome) values (?,?)",
                    (usuario.cpf,usuario.nome))
    conn.commit()
    conn.close()

def listar_usuario():
    conn = conectar()
    cursor = conn.cursor()
    cursor.execute("SELECT cpf,nome FROM usuario")
    usuario = cursor.fetchall() 
    conn.close()
    return usuario



 



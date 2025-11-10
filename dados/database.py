import sqlite3

#constantes
DB_NAME = "livros.db"

def criar_tabela():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS livros (
            isbn TEXT PRIMARY KEY,
            titulo TEXT NOT NULL
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario (
            cpf TEXT PRIMARY KEY,
            nome TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def conectar():
    return sqlite3.connect(DB_NAME)
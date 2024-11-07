import sqlite3

DATABASE = "app.db"

def setup_database():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS config (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave TEXT UNIQUE,
            valor TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS chaves (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT UNIQUE,
            num_copias INTEGER,
            descricao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS reservas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave TEXT,
            aluno TEXT,
            professor TEXT,
            data_hora TEXT,
            em_uso INTEGER,
            termo TEXT,
            devolvido INTEGER,
            data_devolucao TEXT
        )
    """)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS relatorio (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            chave TEXT,
            aluno TEXT,
            professor TEXT,
            data_hora TEXT,
            data_devolucao TEXT,
            tempo_com_chave TEXT,
            termo TEXT
        )
    """)
    conn.commit()
    conn.close()

def salvar_chave_no_banco(nome, num_copias, descricao):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO chaves (nome, num_copias, descricao) VALUES (?, ?, ?)",
                   (nome, num_copias, descricao))
    conn.commit()
    conn.close()

def carregar_chaves_do_banco():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT nome, num_copias, descricao FROM chaves")
    chaves = {row[0]: {"num_copias": row[1], "descricao": row[2], "reservas": [], "status": "green"} for row in cursor.fetchall()}
    conn.close()
    return chaves

def deletar_chave_do_banco(nome):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM chaves WHERE nome = ?", (nome,))
    conn.commit()
    conn.close()

def salvar_reserva_no_banco(chave, reserva):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO reservas (chave, aluno, professor, data_hora, em_uso, termo, devolvido, data_devolucao)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        chave,
        reserva["aluno"],
        reserva["professor"],
        reserva["data"].strftime("%d/%m/%Y %H:%M:%S"),
        int(reserva["em_uso"]),
        reserva["termo"],
        int(reserva.get("devolvido", False)),
        reserva.get("data_devolucao", "").strftime("%d/%m/%Y %H:%M:%S") if reserva.get("data_devolucao") else None
    ))
    conn.commit()
    conn.close()

def atualizar_reserva_no_banco(chave, reserva):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        UPDATE reservas
        SET em_uso = ?, termo = ?, devolvido = ?, data_devolucao = ?
        WHERE chave = ? AND aluno = ? AND professor = ? AND data_hora = ?
    """, (
        int(reserva["em_uso"]),
        reserva["termo"],
        int(reserva.get("devolvido", False)),
        reserva.get("data_devolucao", "").strftime("%d/%m/%Y %H:%M:%S") if reserva.get("data_devolucao") else None,
        chave,
        reserva["aluno"],
        reserva["professor"],
        reserva["data"].strftime("%d/%m/%Y %H:%M:%S")
    ))
    conn.commit()
    conn.close()

def deletar_reserva_do_banco(chave, aluno, professor, data_hora):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        DELETE FROM reservas WHERE chave = ? AND aluno = ? AND professor = ? AND data_hora = ?
    """, (chave, aluno, professor, data_hora.strftime("%d/%m/%Y %H:%M:%S")))
    conn.commit()
    conn.close()

def carregar_reservas_do_banco():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT chave, aluno, professor, data_hora, em_uso, termo, devolvido, data_devolucao FROM reservas")
    reservas = cursor.fetchall()
    conn.close()
    return reservas

def salvar_relatorio_no_banco(relatorio):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO relatorio (chave, aluno, professor, data_hora, data_devolucao, tempo_com_chave, termo)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        relatorio["chave"],
        relatorio["aluno"],
        relatorio["professor"],
        relatorio["data_hora"].strftime("%d/%m/%Y %H:%M:%S"),
        relatorio["data_devolucao"].strftime("%d/%m/%Y %H:%M:%S") if relatorio["data_devolucao"] else None,
        relatorio["tempo_com_chave"],
        relatorio["termo"]
    ))
    conn.commit()
    conn.close()

def carregar_relatorios_do_banco():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT chave, aluno, professor, data_hora, data_devolucao, tempo_com_chave, termo FROM relatorio")
    relatorios = cursor.fetchall()
    conn.close()
    return relatorios

def salvar_caminho_importacao(chave, caminho):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("INSERT OR REPLACE INTO config (chave, valor) VALUES (?, ?)", (chave, caminho))
    conn.commit()
    conn.close()

def ler_caminho_importacao(chave):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute("SELECT valor FROM config WHERE chave = ?", (chave,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
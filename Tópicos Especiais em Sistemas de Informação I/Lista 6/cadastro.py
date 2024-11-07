from cadastro_aluno import create_cadastro_alunos_window
from cadastro_professor import create_cadastro_professores_window
from cadastro_chaves import create_cadastro_chaves_window

def create_cadastro_window(app, title, default_file=None):
    if title == "Cadastro de Alunos":
        create_cadastro_alunos_window(app)
    elif title == "Cadastro de Professores":
        create_cadastro_professores_window(app)
    elif title == "Cadastro de Chaves":
        create_cadastro_chaves_window(app)
    else:
        raise ValueError(f"Tipo de cadastro desconhecido: {title}")
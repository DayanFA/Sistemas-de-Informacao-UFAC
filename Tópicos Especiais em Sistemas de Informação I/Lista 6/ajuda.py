import tkinter as tk
import webbrowser
import os

def create_ajuda_window(app):
    ajuda_window = tk.Toplevel(app.root)
    ajuda_window.title("Sobre")
    ajuda_window.geometry("700x600")
    ajuda_window.resizable(False, False)

    frame = tk.Frame(ajuda_window, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)

    # Título
    title_label = tk.Label(frame, text="Sistema de Gerenciamento de Chaves", font=("Helvetica", 16, "bold"))
    title_label.pack(pady=10)

    # Objetivo do Projeto
    objetivo_label = tk.Label(frame, text="O objetivo do projeto é desenvolver um sistema de gerenciamento de chaves para coordenação de medicina.", wraplength=660, justify="left")
    objetivo_label.pack(pady=5)

    # Versão
    versao_label = tk.Label(frame, text="Versão", font=("Helvetica", 12, "bold"))
    versao_label.pack(pady=5)
    versao_text = tk.Label(frame, text="1.0", wraplength=660, justify="left")
    versao_text.pack(pady=5)

    # Licença
    licenca_label = tk.Label(frame, text="Licença", font=("Helvetica", 12, "bold"))
    licenca_label.pack(pady=5)
    licenca_text = tk.Label(frame, text="Este projeto está licenciado sob a [Ainda vamos colocar o nome aqui]", wraplength=660, justify="left")
    licenca_text.pack(pady=5)

    # Manual de Usuário
    manual_label = tk.Label(frame, text="Manual de Usuário", font=("Helvetica", 12, "bold"))
    manual_label.pack(pady=5)
    manual_link = tk.Label(frame, text="Clique aqui para abrir o manual de usuário", fg="blue", cursor="hand2", wraplength=660, justify="left")
    manual_link.pack(pady=5)
    manual_link.bind("<Button-1>", lambda e: abrir_manual())

    # Contato
    contato_label = tk.Label(frame, text="Contato", font=("Helvetica", 12, "bold"))
    contato_label.pack(pady=5)
    contato_text = tk.Label(frame, text="Qualquer dúvida contate os desenvolvedores:", wraplength=660, justify="left")
    contato_text.pack(pady=5)

    # Função para abrir o cliente de email
    def abrir_email(email):
        webbrowser.open(f"mailto:{email}")

    # Função para abrir o manual de usuário
    def abrir_manual():
        manual_path = os.path.join(os.path.dirname(__file__), 'manual_de_usuario.pdf')
        webbrowser.open(manual_path)

    # Nomes e emails dos desenvolvedores
    dev_andre_label = tk.Label(frame, text="André Ferreira", wraplength=660, justify="left")
    dev_andre_label.pack(pady=5)
    email_andre = tk.Label(frame, text="ferreira.andre@sou.ufac.br", fg="blue", cursor="hand2", wraplength=660, justify="left")
    email_andre.pack(pady=5)
    email_andre.bind("<Button-1>", lambda e: abrir_email("ferreira.andre@sou.ufac.br"))

    dev_dayan_label = tk.Label(frame, text="Dayan FA", wraplength=660, justify="left")
    dev_dayan_label.pack(pady=5)
    email_dayan = tk.Label(frame, text="contatodayanfa@gmail.com", fg="blue", cursor="hand2", wraplength=660, justify="left")
    email_dayan.pack(pady=5)
    email_dayan.bind("<Button-1>", lambda e: abrir_email("contatodayanfa@gmail.com"))

    # Botão de Fechar
    fechar_button = tk.Button(frame, text="Fechar", command=ajuda_window.destroy)
    fechar_button.pack(pady=10)
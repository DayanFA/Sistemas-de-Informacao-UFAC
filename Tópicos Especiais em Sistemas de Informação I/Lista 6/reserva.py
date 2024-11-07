import tkinter as tk
from tkinter import messagebox
from datetime import datetime
from autocomplete_combobox import AutocompleteCombobox

def create_reserva_window(app):
    reserva_window = tk.Toplevel(app.root)
    reserva_window.title("Fazer Reserva")
    reserva_window.geometry("600x400")
    reserva_window.resizable(True, True)

    frame = tk.Frame(reserva_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    label = tk.Label(frame, text="Fazer Reserva", font=("Helvetica", 14))
    label.pack(pady=10)

    # Seleção de Chave
    tk.Label(frame, text="Chave:").pack(pady=5)
    app.chave_var = tk.StringVar()
    app.chave_combobox = AutocompleteCombobox(frame, textvariable=app.chave_var)
    app.chave_combobox.set_completion_list(list(app.chave_info.keys()))
    app.chave_combobox.pack(pady=5)

    # Seleção de Aluno
    tk.Label(frame, text="Aluno:").pack(pady=5)
    app.aluno_var = tk.StringVar()
    app.aluno_combobox = AutocompleteCombobox(frame, textvariable=app.aluno_var)
    app.aluno_combobox.set_completion_list(app.get_alunos())
    app.aluno_combobox.pack(pady=5)

    # Seleção de Professor
    tk.Label(frame, text="Professor:").pack(pady=5)
    app.professor_var = tk.StringVar()
    app.professor_combobox = AutocompleteCombobox(frame, textvariable=app.professor_var)
    app.professor_combobox.set_completion_list(app.get_professores())
    app.professor_combobox.pack(pady=5)

    # Campo para Data e Hora
    tk.Label(frame, text="Data e Hora:").pack(pady=5)
    app.data_hora_var = tk.StringVar(value=datetime.now().strftime("%d/%m/%Y %H:%M:%S"))
    tk.Entry(frame, textvariable=app.data_hora_var).pack(pady=5)

    # Botão para confirmar reserva
    reservar_button = tk.Button(frame, text="Reservar", command=lambda: reservar_chave(app))
    reservar_button.pack(pady=10)

def reservar_chave(app):
    chave = app.chave_var.get()
    aluno = app.aluno_var.get()
    professor = app.professor_var.get()
    data_hora_str = app.data_hora_var.get()
    if chave and (aluno or professor):
        try:
            data_hora_dt = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M:%S")
            reserva = {"aluno": aluno, "professor": professor, "data": data_hora_dt, "em_uso": False, "termo": ""}
            app.chave_info[chave]["reservas"].append(reserva)
            app.chave_info[chave]["status"] = app.get_status_color(chave)
            app.salvar_reserva_no_banco(chave, reserva)
            messagebox.showinfo("Reserva", f"Chave {chave} reservada por {aluno if aluno else professor} em {data_hora_str}")
            app.update_chaves_ui()
        except ValueError:
            messagebox.showerror("Erro", "Erro ao registrar a reserva. Verifique o formato da data e hora.")
    else:
        messagebox.showerror("Erro", "Por favor, selecione uma chave e um aluno ou professor.")
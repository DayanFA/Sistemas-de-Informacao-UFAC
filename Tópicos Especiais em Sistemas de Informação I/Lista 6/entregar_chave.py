import tkinter as tk
from tkinter import messagebox, ttk, filedialog
from datetime import datetime
import os
import pandas as pd
from autocomplete_combobox import AutocompleteCombobox
from ui_helpers import create_treeview_with_scrollbars

def create_entregar_chave_window(app):
    entregar_window = tk.Toplevel(app.root)
    entregar_window.title("Entregar Chave")
    entregar_window.geometry("600x600")
    entregar_window.resizable(True, True)

    frame = tk.Frame(entregar_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    label = tk.Label(frame, text="Entregar Chave", font=("Helvetica", 14))
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

    # Checkbutton para indicar se algum item está sendo emprestado
    app.item_emprestado_var = tk.BooleanVar()
    item_emprestado_check = tk.Checkbutton(frame, text="Algum item está sendo emprestado", variable=app.item_emprestado_var, command=lambda: toggle_item_emprestado(app))
    item_emprestado_check.pack(pady=5)

    # Campo para importar arquivo PDF do termo de compromisso
    tk.Label(frame, text="Termo de Compromisso (PDF):").pack(pady=5)
    app.termo_var = tk.StringVar()
    termo_entry = tk.Entry(frame, textvariable=app.termo_var, state='readonly')
    termo_entry.pack(pady=5)
    app.termo_button = tk.Button(frame, text="Importar Termo", command=lambda: importar_termo(app))
    app.termo_button.pack(pady=5)
    app.termo_button.config(state='disabled')

    # Botão para confirmar entrega
    entregar_button = tk.Button(frame, text="Entregar", command=lambda: entregar_chave(app))
    entregar_button.pack(pady=10)

    # Botão para ver entregas
    ver_entregas_button = tk.Button(frame, text="Ver Entregas", command=lambda: ver_entregas(app))
    ver_entregas_button.pack(pady=10)

def importar_termo(app):
    file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
    if file_path:
        app.termo_var.set(file_path)

def toggle_item_emprestado(app):
    if app.item_emprestado_var.get():
        app.termo_button.config(state='normal')
    else:
        app.termo_var.set("")
        app.termo_button.config(state='disabled')

def entregar_chave(app):
    chave = app.chave_var.get()
    aluno = app.aluno_var.get()
    professor = app.professor_var.get()
    termo = app.termo_var.get()
    item_atribuido = "Sim" if termo else "Não"
    data = datetime.now().strftime("%d/%m/%Y")
    hora = datetime.now().strftime("%H:%M:%S")
    if chave and (aluno or professor):
        try:
            data_hora_str = f"{data} {hora}"
            data_hora_dt = datetime.strptime(data_hora_str, "%d/%m/%Y %H:%M:%S")
            entrega = {
                "aluno": aluno,
                "professor": professor,
                "data": data_hora_dt,
                "em_uso": True,
                "termo": termo,
                "item_atribuido": item_atribuido
            }
            app.chave_info[chave]["reservas"].append(entrega)
            if data_hora_dt.date() == datetime.now().date():
                app.chave_info[chave]["status"] = "yellow"
            else:
                app.chave_info[chave]["status"] = "green"
            app.salvar_reserva_no_banco(chave, entrega)
            messagebox.showinfo("Entrega", f"Chave {chave} entregue por {aluno if aluno else professor} em {data_hora_str}")
            app.update_chaves_ui()
            app.update_chaves_combobox()
        except ValueError:
            messagebox.showerror("Erro", "Erro ao registrar a entrega.")
    else:
        messagebox.showerror("Erro", "Por favor, selecione uma chave e um aluno ou professor.")

def ver_entregas(app):
    entregas_window = tk.Toplevel(app.root)
    entregas_window.title("Entregas")
    entregas_window.geometry("800x400")
    entregas_window.resizable(True, True)

    frame = tk.Frame(entregas_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tree = create_treeview_with_scrollbars(frame)
    tree["columns"] = ("Chave", "Aluno", "Professor", "Data e Hora", "Status", "Item Atribuído", "Termo de Compromisso")
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    for chave, info in app.chave_info.items():
        for reserva in info["reservas"]:
            aluno = reserva.get("aluno", "")
            professor = reserva.get("professor", "")
            termo = reserva.get("termo", "")
            item_atribuido = "Sim" if termo else "Não"
            status = "Em Uso" if reserva.get("em_uso", False) else "Reservado"
            tree.insert("", tk.END, values=(chave, aluno, professor, reserva["data"].strftime("%d/%m/%Y %H:%M:%S"), status, item_atribuido, termo))

    def abrir_termo(event):
        selected_item = tree.selection()
        if selected_item:
            valores = tree.item(selected_item[0], "values")
            termo = valores[6]
            if termo:
                os.startfile(termo)

    tree.bind("<Double-1>", abrir_termo)

    def marcar_devolvido(app, tree):
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showerror("Erro", "Por favor, selecione uma entrega para marcar como devolvida.")
            return

        selected_item = selected_items[0]
        valores = tree.item(selected_item, "values")
        chave = valores[0]
        aluno = valores[1]
        professor = valores[2]
        data_hora = valores[3]
        termo = valores[6]
        data_hora_dt = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")

        for reserva in app.chave_info[chave]["reservas"]:
            if reserva["aluno"] == aluno and reserva["professor"] == professor and reserva["data"] == data_hora_dt:
                reserva["devolvido"] = True
                reserva["em_uso"] = False
                reserva["data_devolucao"] = datetime.now()
                data_devolucao = reserva["data_devolucao"].strftime("%d/%m/%Y %H:%M:%S")
                tempo_com_chave = reserva["data_devolucao"] - reserva["data"]
                tempo_com_chave_str = str(tempo_com_chave).split('.')[0]
                relatorio = {
                    "chave": chave,
                    "aluno": aluno,
                    "professor": professor,
                    "data_hora": data_hora_dt,
                    "data_devolucao": reserva["data_devolucao"],
                    "tempo_com_chave": tempo_com_chave_str,
                    "termo": termo
                }
                app.salvar_relatorio_no_banco(relatorio)
                app.deletar_reserva_do_banco(chave, aluno, professor, data_hora_dt)
                app.chave_info[chave]["reservas"].remove(reserva)
                app.relatorio.append(relatorio)
                break

        tree.delete(selected_item)
        app.update_chaves_ui()

    devolvido_button = tk.Button(frame, text="Marcar como Devolvido", command=lambda: marcar_devolvido(app, tree))
    devolvido_button.pack(side=tk.LEFT, padx=5, pady=10)

    def editar_entrega():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showerror("Erro", "Por favor, selecione uma entrega para editar.")
            return

        selected_item = selected_items[0]
        valores = tree.item(selected_item, "values")
        chave = valores[0]
        aluno = valores[1]
        professor = valores[2]
        data_hora = valores[3]
        status = valores[4]
        termo_atual = valores[6]
        data_hora_dt = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")

        def importar_termo():
            file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
            if file_path:
                app.termo_var.set(file_path)

        def toggle_importar_termo():
            if app.atualizar_termo_var.get():
                app.termo_button.config(state='normal')
            else:
                app.termo_var.set("")
                app.termo_button.config(state='disabled')

        def save():
            new_status = status_var.get()
            new_termo = app.termo_var.get() if app.atualizar_termo_var.get() else termo_atual
            item_atribuido = "Sim" if new_termo else "Não"
            for reserva in app.chave_info[chave]["reservas"]:
                if reserva["aluno"] == aluno and reserva["professor"] == professor and reserva["data"] == data_hora_dt:
                    if new_status == "Em Uso":
                        reserva["devolvido"] = False
                        reserva["em_uso"] = True
                    elif new_status == "Reservado":
                        reserva["devolvido"] = False
                        reserva["em_uso"] = False
                    reserva["termo"] = new_termo
                    reserva["item_atribuido"] = item_atribuido
                    app.atualizar_reserva_no_banco(chave, reserva)
                    break
            tree.item(selected_item, values=(chave, aluno, professor, data_hora, new_status, item_atribuido, new_termo))
            app.update_chaves_ui()
            edit_window.destroy()

        edit_window = tk.Toplevel(app.root)
        edit_window.title("Editar Entrega")
        edit_window.geometry("400x300")

        tk.Label(edit_window, text="Status:").pack(pady=5)
        status_var = tk.StringVar(value=status)
        status_combobox = ttk.Combobox(edit_window, textvariable=status_var)
        status_combobox['values'] = ("Em Uso", "Reservado")
        status_combobox.pack(pady=5)

        app.atualizar_termo_var = tk.BooleanVar()
        atualizar_termo_check = tk.Checkbutton(edit_window, text="Atualizar novo termo de compromisso", variable=app.atualizar_termo_var, command=toggle_importar_termo)
        atualizar_termo_check.pack(pady=5)

        app.termo_var = tk.StringVar()
        termo_entry = tk.Entry(edit_window, textvariable=app.termo_var, state='readonly')
        termo_entry.pack(pady=5)
        app.termo_button = tk.Button(edit_window, text="Importar Termo", command=importar_termo)
        app.termo_button.pack(pady=5)
        app.termo_button.config(state='disabled')

        tk.Button(edit_window, text="Salvar", command=save).pack(pady=10)

    editar_button = tk.Button(frame, text="Editar", command=editar_entrega)
    editar_button.pack(side=tk.LEFT, padx=5, pady=10)

    def excluir_entrega(app, tree):
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showerror("Erro", "Por favor, selecione uma entrega para excluir.")
            return

        selected_item = selected_items[0]
        valores = tree.item(selected_item, "values")
        chave = valores[0]
        aluno = valores[1]
        professor = valores[2]
        data_hora = valores[3]
        data_hora_dt = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")
        for reserva in app.chave_info[chave]["reservas"]:
            if reserva["aluno"] == aluno and reserva["professor"] == professor and reserva["data"] == data_hora_dt:
                app.chave_info[chave]["reservas"].remove(reserva)
                app.deletar_reserva_do_banco(chave, aluno, professor, data_hora_dt)
                break
        tree.delete(selected_item)
        app.update_chaves_ui()

    excluir_button = tk.Button(frame, text="Excluir", command=lambda: excluir_entrega(app, tree))
    excluir_button.pack(side=tk.LEFT, padx=5, pady=10)

    def mostrar_mais_info():
        selected_items = tree.selection()
        if not selected_items:
            messagebox.showerror("Erro", "Por favor, selecione uma entrega para ver mais informações.")
            return

        selected_item = selected_items[0]
        valores = tree.item(selected_item, "values")
        chave = valores[0]
        aluno = valores[1]
        professor = valores[2]
        data_hora = valores[3]
        status = valores[4]

        info_window = tk.Toplevel(app.root)
        info_window.title(f"Informações da {chave}")
        info_window.geometry("800x400")
        info_window.resizable(True, True)

        frame = tk.Frame(info_window)
        frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        tree_info = create_treeview_with_scrollbars(frame)
        colunas_fixas = ["Chave", "Aluno", "Professor", "Data e Hora", "Tempo com a Chave", "Número de Cópias da Chave",
                         "Descrição da Chave"]
        colunas_adicionais = set()

        info = app.chave_info.get(chave, {})
        caminho_alunos = app.ler_caminho_importacao("caminho_alunos") or "cadastro_alunos.xlsx"
        caminho_professores = app.ler_caminho_importacao("caminho_professores") or "cadastro_professores.xlsx"

        for reserva in info.get("reservas", []):
            aluno = reserva.get("aluno", "")
            professor = reserva.get("professor", "")

            if aluno:
                df = pd.read_excel(caminho_alunos)
                linha_info = df[df.iloc[:, 0] == aluno].iloc[0]
                for col in linha_info.index:
                    if col != linha_info.index[0]:
                        colunas_adicionais.add(col)

            if professor:
                df = pd.read_excel(caminho_professores)
                linha_info = df[df.iloc[:, 0] == professor].iloc[0]
                for col in linha_info.index:
                    if col != linha_info.index[0]:
                        colunas_adicionais.add(col)

        # Configurar colunas no Treeview
        todas_colunas = colunas_fixas + list(colunas_adicionais)
        tree_info["columns"] = todas_colunas
        for col in todas_colunas:
            tree_info.heading(col, text=col)
            tree_info.column(col, width=150)

        # Adicionar informações ao Treeview
        for reserva in info.get("reservas", []):
            aluno = reserva.get("aluno", "")
            professor = reserva.get("professor", "")
            data_hora = reserva["data"].strftime("%d/%m/%Y %H:%M:%S")
            tempo_com_chave = datetime.now() - reserva["data"]
            tempo_com_chave_str = str(tempo_com_chave).split('.')[0]

            valores = [chave, aluno, professor, data_hora, tempo_com_chave_str, info["num_copias"], info["descricao"]]

            if aluno:
                df = pd.read_excel(caminho_alunos)
                linha_info = df[df.iloc[:, 0] == aluno].iloc[0]
                valores.extend([linha_info[col] for col in colunas_adicionais if col in linha_info.index])

            if professor:
                df = pd.read_excel(caminho_professores)
                linha_info = df[df.iloc[:, 0] == professor].iloc[0]
                valores.extend([linha_info[col] for col in colunas_adicionais if col in linha_info.index])

            tree_info.insert("", tk.END, values=valores)

    mais_info_button = tk.Button(frame, text="Mais Info", command=mostrar_mais_info)
    mais_info_button.pack(side=tk.LEFT, padx=5, pady=10)
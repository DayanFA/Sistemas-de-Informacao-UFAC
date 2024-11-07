import sqlite3
import tkinter as tk
from tkinter import filedialog, messagebox
import os
import pandas as pd
from openpyxl.styles import Font
from ui_helpers import create_treeview_with_scrollbars

def create_relatorio_window(app):
    relatorio_window = tk.Toplevel(app.root)
    relatorio_window.title("Relatórios")
    relatorio_window.geometry("800x400")
    relatorio_window.resizable(True, True)

    frame = tk.Frame(relatorio_window)
    frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

    tree = create_treeview_with_scrollbars(frame)
    tree["columns"] = (
        "Chave", "Aluno", "Professor", "Data e Hora", "Data de Devolução", "Tempo com a Chave",
        "Termo de Compromisso")
    for col in tree["columns"]:
        tree.heading(col, text=col)
        tree.column(col, width=150)

    for item in app.relatorio:
        tree.insert("", tk.END, values=(
            item["chave"], item["aluno"], item["professor"], item["data_hora"].strftime("%d/%m/%Y %H:%M:%S"),
            item["data_devolucao"].strftime("%d/%m/%Y %H:%M:%S") if item["data_devolucao"] else "",
            item["tempo_com_chave"], item["termo"]))

    def abrir_termo(event):
        selected_item = tree.selection()
        if selected_item:
            valores = tree.item(selected_item[0], "values")
            termo = valores[6]
            if termo:
                os.startfile(termo)

    tree.bind("<Double-1>", abrir_termo)

    exportar_button = tk.Button(frame, text="Exportar Relatório", command=lambda: exportar_relatorio(app))
    exportar_button.pack(pady=10)

def exportar_relatorio(app):
    # Recuperar os dados do banco de dados de relatórios
    conn = sqlite3.connect("app.db")  
    cursor = conn.cursor()
    cursor.execute(
        "SELECT chave, aluno, professor, data_hora, data_devolucao, tempo_com_chave, termo FROM relatorio")
    relatorios = cursor.fetchall()
    conn.close()

    if not relatorios:
        messagebox.showerror("Erro", "Não há dados no relatório para exportar.")
        return

    # Converter os dados para um DataFrame do pandas
    df = pd.DataFrame(relatorios, columns=["Chave", "Aluno", "Professor", "Data e Hora", "Data de Devolução",
                                           "Tempo com a Chave", "Termo de Compromisso"])

    # Adicionar coluna "Item Atribuído"
    df["Item Atribuído"] = df["Termo de Compromisso"].apply(lambda x: "Sim" if x else "Não")

    # Pedir ao usuário para escolher onde salvar o arquivo
    file_path = filedialog.asksaveasfilename(defaultextension=".xlsx", filetypes=[("Excel files", "*.xlsx")])
    if not file_path:
        return

    # Salvar o DataFrame em um arquivo Excel
    with pd.ExcelWriter(file_path, engine='openpyxl') as writer:
        df.to_excel(writer, sheet_name="Relatório", index=False)

        # Adicionar links para PDFs
        workbook = writer.book
        worksheet = workbook["Relatório"]
        for idx, row in df.iterrows():
            termo_path = row["Termo de Compromisso"]
            if termo_path and os.path.exists(termo_path):
                cell = worksheet.cell(row=idx + 2, column=7)
                cell.value = "Abrir PDF"
                cell.hyperlink = termo_path
                cell.font = Font(color="0000FF", underline="single")

    messagebox.showinfo("Exportação", f"Relatório exportado com sucesso para '{file_path}'.")
import tkinter as tk
from tkinter import filedialog, messagebox
from datetime import datetime
import pandas as pd
from configuracoes import create_configuracoes_window
from cadastro import create_cadastro_window
from entregar_chave import create_entregar_chave_window
from relatorio import create_relatorio_window
from ajuda import create_ajuda_window
from reserva import create_reserva_window
from banco import (
    setup_database,
    salvar_chave_no_banco,
    carregar_chaves_do_banco,
    deletar_chave_do_banco,
    salvar_reserva_no_banco,
    atualizar_reserva_no_banco,
    deletar_reserva_do_banco,
    carregar_reservas_do_banco,
    salvar_relatorio_no_banco,
    carregar_relatorios_do_banco,
    salvar_caminho_importacao,
    ler_caminho_importacao
)

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Empréstimo de Chaves")
        self.root.geometry("800x600")
        self.root.resizable(False, False)

        # Configurar o banco de dados
        setup_database()

        self.style = None

        # Inicializar chave_info com valores padrão
        self.chave_info = carregar_chaves_do_banco()
        self.carregar_reservas()

        # Inicializar relatorio
        self.relatorio = []
        self.carregar_relatorios()

        # Menu
        self.menu = tk.Menu(self.root)
        self.root.config(menu=self.menu)

        self.cadastro_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Cadastro", menu=self.cadastro_menu)
        self.cadastro_menu.add_command(label="Cadastro de Alunos", command=lambda: self.cadastro("Cadastro de Alunos"))
        self.cadastro_menu.add_command(label="Cadastro de Professores", command=lambda: self.cadastro("Cadastro de Professores"))
        self.cadastro_menu.add_command(label="Cadastro de Chaves", command=lambda: self.cadastro("Cadastro de Chaves"))

        self.reserva_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Reserva", menu=self.reserva_menu)
        self.reserva_menu.add_command(label="Fazer Reserva", command=self.fazer_reserva)

        self.chave_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Chave", menu=self.chave_menu)
        self.chave_menu.add_command(label="Entregar Chave", command=self.entregar_chave)

        self.relatorio_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Relatório", menu=self.relatorio_menu)
        self.relatorio_menu.add_command(label="Ver Relatórios", command=self.ver_relatorios)

        self.configuracoes_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Configurações", menu=self.configuracoes_menu)
        self.configuracoes_menu.add_command(label="Configurações Gerais", command=self.configuracoes)

        self.ajuda_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="Ajuda", menu=self.ajuda_menu)
        self.ajuda_menu.add_command(label="Sobre", command=self.sobre)

        # Tela Inicial
        self.main_frame = tk.Frame(self.root, bg="saddlebrown")
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        self.label_chaves = tk.Label(self.main_frame, text="Chaves Disponíveis:", bg="saddlebrown", fg="white",
                                     font=("Helvetica", 16))
        self.label_chaves.pack(pady=10)

        self.chaves_frame = tk.Frame(self.main_frame, bg="saddlebrown")
        self.chaves_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

        self.chaves = [f"Chave {i}" for i in range(1, 25)]
        self.statuses = ["green", "yellow", "red"]

        self.create_chaves_ui()

        # Outros
        self.status_popup = None

    def cadastro(self, title):
        create_cadastro_window(self, title)

    def configuracoes(self):
        create_configuracoes_window(self)

    def sobre(self):
        create_ajuda_window(self)

    def ver_relatorios(self):
        create_relatorio_window(self)

    def carregar_reservas(self):
        reservas = carregar_reservas_do_banco()
        for row in reservas:
            chave, aluno, professor, data_hora, em_uso, termo, devolvido, data_devolucao = row
            data_hora_dt = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")
            reserva = {
                "aluno": aluno,
                "professor": professor,
                "data": data_hora_dt,
                "em_uso": bool(em_uso),
                "termo": termo,
                "devolvido": bool(devolvido),
                "data_devolucao": datetime.strptime(data_devolucao, "%d/%m/%Y %H:%M:%S") if data_devolucao else None
            }
            if chave in self.chave_info:
                self.chave_info[chave]["reservas"].append(reserva)
                self.chave_info[chave]["status"] = self.get_status_color(chave)

    def carregar_relatorios(self):
        relatorios = carregar_relatorios_do_banco()
        for row in relatorios:
            chave, aluno, professor, data_hora, data_devolucao, tempo_com_chave, termo = row
            data_hora_dt = datetime.strptime(data_hora, "%d/%m/%Y %H:%M:%S")
            data_devolucao_dt = datetime.strptime(data_devolucao, "%d/%m/%Y %H:%M:%S") if data_devolucao else None
            relatorio = {
                "chave": chave,
                "aluno": aluno,
                "professor": professor,
                "data_hora": data_hora_dt,
                "data_devolucao": data_devolucao_dt,
                "tempo_com_chave": tempo_com_chave,
                "termo": termo
            }
            self.relatorio.append(relatorio)

    def create_chaves_ui(self):
        for widget in self.chaves_frame.winfo_children():
            widget.destroy()

        for i, (chave, info) in enumerate(self.chave_info.items()):
            frame = tk.Frame(self.chaves_frame, borderwidth=1, relief="solid", bg="burlywood")
            frame.grid(row=i // 6, column=i % 6, padx=10, pady=10)

            label = tk.Label(frame, text=chave, bg="burlywood", font=("Helvetica", 12))
            label.pack(pady=5)

            status_color = self.get_status_color(chave)
            status_text = self.get_status_text(status_color)
            status = tk.Label(frame, text=status_text, bg=status_color, width=10, font=("Helvetica", 10))
            status.pack(pady=5)

            status.bind("<Enter>", self.create_show_status_info_callback(chave))
            status.bind("<Leave>", self.hide_status_info)

    def get_status_color(self, chave):
        info = self.chave_info[chave]
        today = datetime.now().date()
        for reserva in info["reservas"]:
            if not reserva.get("devolvido", False):
                if reserva.get("em_uso", False):
                    return "red"
                elif reserva["data"].date() == today:
                    return "yellow"
        return "green"

    def get_status_text(self, status_color):
        if status_color == "green":
            return "Disponível"
        elif status_color == "yellow":
            return "Reservado"
        elif status_color == "red":
            return "Em Uso"

    def create_show_status_info_callback(self, chave):
        def callback(event):
            self.show_status_info(event, chave)
        return callback

    def show_status_info(self, event, chave):
        info = self.chave_info[chave]
        status = self.get_status_color(chave)
        reservas = info["reservas"]

        status_text = "Disponível" if status == "green" else "Reservado" if status == "yellow" else "Em Uso"
        reservas_text = "\n".join([f"{reserva['aluno']} - {reserva['data'].strftime('%d/%m/%Y %H:%M:%S')}" for reserva in reservas])

        status_info = f"Status: {status_text}\nReservas:\n{reservas_text}"
        x, y, _, _ = event.widget.bbox("insert")
        x += event.widget.winfo_rootx() + 25
        y += event.widget.winfo_rooty() + 25

        self.status_popup = tk.Toplevel(self.root)
        self.status_popup.wm_overrideredirect(True)
        self.status_popup.wm_geometry(f"+{x}+{y}")

        label = tk.Label(self.status_popup, text=status_info, background="lightyellow", relief="solid", borderwidth=1)
        label.pack()

    def hide_status_info(self, event):
        if hasattr(self, 'status_popup'):
            self.status_popup.destroy()

    def fazer_reserva(self):
        create_reserva_window(self)

    def entregar_chave(self):
        create_entregar_chave_window(self)

    def get_alunos(self):
        try:
            caminho_alunos = self.ler_caminho_importacao("caminho_alunos")
            if not caminho_alunos:
                caminho_alunos = "cadastro_alunos.xlsx"
            df = pd.read_excel(caminho_alunos)
            return df.iloc[:, 0].tolist()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados de alunos: {e}")
            return []

    def get_professores(self):
        try:
            caminho_professores = self.ler_caminho_importacao("caminho_professores")
            if not caminho_professores:
                caminho_professores = "cadastro_professores.xlsx"
            df = pd.read_excel(caminho_professores)
            return df.iloc[:, 0].tolist()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados de professores: {e}")
            return []

    def update_chaves_ui(self):
        for widget in self.chaves_frame.winfo_children():
            widget.destroy()
        self.create_chaves_ui()

    def update_chaves_list(self):
        self.chaves = list(self.chave_info.keys())

    def update_chaves_combobox(self):
        if hasattr(self, 'chave_combobox') and self.chave_combobox.winfo_exists():
            self.chave_combobox.set_completion_list(list(self.chave_info.keys()))

    def load_data(self, tree, file_path):
        try:
            df = pd.read_excel(file_path)
            tree["columns"] = list(df.columns)
            for col in df.columns:
                tree.heading(col, text=col)
                tree.column(col, width=100)
            for index, row in df.iterrows():
                tree.insert("", tk.END, values=tuple(row))
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao carregar dados: {e}")

    def import_data(self, tree, default_file, chave):
        file_path = filedialog.askopenfilename(filetypes=[("Excel files", "*.xlsx")])
        if file_path:
            try:
                df = pd.read_excel(file_path)
                tree.delete(*tree.get_children())
                tree["columns"] = list(df.columns)
                for col in df.columns:
                    tree.heading(col, text=col)
                    tree.column(col, width=100)
                for index, row in df.iterrows():
                    tree.insert("", tk.END, values=tuple(row))
                # Salvar o caminho do arquivo importado
                self.salvar_caminho_importacao(chave, file_path)
                messagebox.showinfo("Importação", f"Dados importados com sucesso de {file_path}")
            except Exception as e:
                messagebox.showerror("Erro", f"Erro ao importar dados: {e}")

    def salvar_caminho_importacao(self, chave, caminho):
        salvar_caminho_importacao(chave, caminho)

    def ler_caminho_importacao(self, chave):
        return ler_caminho_importacao(chave)

    def salvar_chave_no_banco(self, nome, num_copias, descricao):
        salvar_chave_no_banco(nome, num_copias, descricao)

    def carregar_chaves_do_banco(self):
        return carregar_chaves_do_banco()

    def deletar_chave_do_banco(self, nome):
        deletar_chave_do_banco(nome)

    def salvar_reserva_no_banco(self, chave, reserva):
        salvar_reserva_no_banco(chave, reserva)

    def atualizar_reserva_no_banco(self, chave, reserva):
        atualizar_reserva_no_banco(chave, reserva)

    def deletar_reserva_do_banco(self, chave, aluno, professor, data_hora):
        deletar_reserva_do_banco(chave, aluno, professor, data_hora)

    def salvar_relatorio_no_banco(self, relatorio):
        salvar_relatorio_no_banco(relatorio)

    def atribuir_item(self, chave, aluno, professor, data_hora):
        reserva = next((r for r in self.chave_info[chave]["reservas"] if
                        r["aluno"] == aluno and r["professor"] == professor and r["data"] == data_hora), None)
        if reserva:
            reserva["em_uso"] = True
            reserva["item_atribuido"] = True
            self.atualizar_reserva_no_banco(chave, reserva)
            self.update_chaves_ui()
            messagebox.showinfo("Atribuição", f"Item atribuído com sucesso para {aluno if aluno else professor}.")

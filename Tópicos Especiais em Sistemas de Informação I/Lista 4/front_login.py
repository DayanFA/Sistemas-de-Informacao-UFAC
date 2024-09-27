import tkinter as tk
from tkinter import messagebox, ttk
from front_app import BancoApp


class TelaLogin:
    def __init__(self, master):
        self.janela = master
        self.janela.title('Login')
        self.janela.geometry('450x500')
        self.janela.resizable(False, False)

        # self.abrir_sistema_bancario()

        # Pré-cadastro
        self.admin_nome = 'admin'
        self.admin_senha = '123'

        self.logo_frame = ttk.Frame(self.janela)
        self.logo_frame.place(relx=0.5, rely=0.3, anchor='center')

        self.logo = tk.PhotoImage(file='Logo.png')
        lbl_logo = ttk.Label(self.logo_frame, image=self.logo)
        lbl_logo.pack()

        self.form_frame = ttk.Frame(self.janela)
        self.form_frame.place(relx=0.5, rely=0.5, anchor='center')

        lbl_usuario = ttk.Label(self.form_frame, text='Usuário', font=('Arial', 10, 'bold'))
        lbl_usuario.grid(row=0, column=0, padx=5, pady=5)
        self.ent_usuario = ttk.Entry(self.form_frame)
        self.ent_usuario.grid(row=0, column=1, padx=5, pady=5)

        lbl_senha = ttk.Label(self.form_frame, text='Senha', font=('Arial', 10, 'bold'))
        lbl_senha.grid(row=1, column=0, padx=5, pady=5)
        self.ent_senha = ttk.Entry(self.form_frame, show='*')
        self.ent_senha.grid(row=1, column=1, padx=5, pady=5)

        self.btn_login = tk.Button(self.form_frame, text='Login', command=self.verificar_login,
                                   font=('Arial', 11, 'bold'), bg='#003594', fg='white')
        self.btn_login.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

        self.janela.bind('<Return>', self.verificar_login)

    def verificar_login(self, event=None):
        usuario = self.ent_usuario.get()
        senha = self.ent_senha.get()

        if usuario == self.admin_nome and senha == self.admin_senha:
            messagebox.showinfo('Login bem-sucedido', f'Bem-vindo, {usuario}!')
            self.abrir_sistema_bancario()
        else:
            messagebox.showerror('Erro de login', 'Usuário ou senha incorretos.')

    def abrir_sistema_bancario(self):
        self.janela.destroy()
        nova_janela = tk.Tk()
        BancoApp(nova_janela)
        nova_janela.mainloop()


janela = tk.Tk()
app = TelaLogin(janela)
janela.mainloop()

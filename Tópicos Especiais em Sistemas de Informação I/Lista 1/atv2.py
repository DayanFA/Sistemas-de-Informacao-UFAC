import tkinter as tk

class PreferenciasCadastro:
	def __init__(self, master):
		self.janela = master
		self.janelaPreferencias()

	def janelaPreferencias(self):
		self.chk_var = tk.IntVar()
		self.chk_receber_email = tk.Checkbutton(self.janela, text="Deseja receber conteúdo por e-mail?", variable=self.chk_var, command=self.atualizarOpcoes)
		self.chk_receber_email.pack()

		self.opcoes_conteudo = ["Python", "JavaScript", "Data Science", "Machine Learning", "DevOps"]
		self.selecoes = []
		for opcao in self.opcoes_conteudo:
			var = tk.IntVar()
			chk = tk.Checkbutton(self.janela, text=opcao, variable=var)
			chk.pack()
			self.selecoes.append((opcao, var, chk))
			chk.config(state=tk.DISABLED)

		self.btn_mostrar_conteudo = tk.Button(self.janela, text="Mostrar Conteúdo Selecionado", command=self.mostrarConteudo)
		self.btn_mostrar_conteudo.pack()

		self.lbl_conteudo_selecionado = tk.Label(self.janela, text="Conteúdo Selecionado: Nenhum")
		self.lbl_conteudo_selecionado.pack()

	def atualizarOpcoes(self):
		if self.chk_var.get() == 1:
			for _, _, chk in self.selecoes:
				chk.config(state=tk.NORMAL)
		else:
			for _, _, chk in self.selecoes:
				chk.config(state=tk.DISABLED)

	def mostrarConteudo(self):
		conteudos = [opcao for opcao, var, _ in self.selecoes if var.get() == 1]
		conteudo_str = ", ".join(conteudos) if conteudos else "Nenhum"
		self.lbl_conteudo_selecionado.config(text=f"Conteúdo Selecionado: {conteudo_str}")

janela_preferencias = tk.Tk()
app_preferencias = PreferenciasCadastro(janela_preferencias)
janela_preferencias.mainloop()
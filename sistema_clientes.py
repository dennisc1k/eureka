import tkinter as tk
from tkinter import ttk, messagebox

clientes = []

def salvar_cliente():
    nome = entry_nome.get()
    email = entry_email.get()
    telefone = entry_telefone.get()
    if nome and email and telefone:
        clientes.append({"nome": nome, "email": email, "telefone": telefone})
        entry_nome.delete(0, tk.END)
        entry_email.delete(0, tk.END)
        entry_telefone.delete(0, tk.END)
        atualizar_lista()
        messagebox.showinfo("Sucesso", "Cliente cadastrado com sucesso!")
    else:
        messagebox.showwarning("Atenção", "Preencha todos os campos.")

def atualizar_lista():
    lista_clientes.delete(*lista_clientes.get_children())
    for cliente in clientes:
        lista_clientes.insert("", tk.END, values=(cliente["nome"], cliente["email"], cliente["telefone"]))

def buscar_clientes():
    termo = entry_busca.get().lower()
    lista_busca.delete(*lista_busca.get_children())
    for cliente in clientes:
        if termo in cliente["nome"].lower():
            lista_busca.insert("", tk.END, values=(cliente["nome"], cliente["email"], cliente["telefone"]))

janela = tk.Tk()
janela.title("Sistema de Clientes")
janela.geometry("900x600")

abas = ttk.Notebook(janela)
abas.pack(expand=True, fill="both")

aba_cadastro = tk.Frame(abas)
abas.add(aba_cadastro, text="Cadastro de Clientes")

tk.Label(aba_cadastro, text="Nome:").pack(pady=5)
entry_nome = tk.Entry(aba_cadastro, width=50)
entry_nome.pack(pady=5)

tk.Label(aba_cadastro, text="Email:").pack(pady=5)
entry_email = tk.Entry(aba_cadastro, width=50)
entry_email.pack(pady=5)

tk.Label(aba_cadastro, text="Telefone:").pack(pady=5)
entry_telefone = tk.Entry(aba_cadastro, width=50)
entry_telefone.pack(pady=5)

btn_salvar = tk.Button(aba_cadastro, text="Salvar Cliente", command=salvar_cliente)
btn_salvar.pack(pady=10)

aba_lista = tk.Frame(abas)
abas.add(aba_lista, text="Lista de Clientes")

colunas = ("Nome", "Email", "Telefone")
lista_clientes = ttk.Treeview(aba_lista, columns=colunas, show="headings")
for col in colunas:
    lista_clientes.heading(col, text=col)
lista_clientes.pack(expand=True, fill="both", padx=10, pady=10)

aba_busca = tk.Frame(abas)
abas.add(aba_busca, text="Busca de Clientes")

tk.Label(aba_busca, text="Buscar por nome:").pack(pady=5)
entry_busca = tk.Entry(aba_busca, width=50)
entry_busca.pack(pady=5)

btn_buscar = tk.Button(aba_busca, text="Buscar", command=buscar_clientes)
btn_buscar.pack(pady=5)

lista_busca = ttk.Treeview(aba_busca, columns=colunas, show="headings")
for col in colunas:
    lista_busca.heading(col, text=col)
lista_busca.pack(expand=True, fill="both", padx=10, pady=10)

janela.mainloop()

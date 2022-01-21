import tkinter as tk
from tkinter import ttk
from datetime import date
from tkinter import messagebox
from webbrowser import get

# Variaveis
hoje = date.today().strftime("%d/%m/%Y")


# Funções
def valor_cbx(event):
    if cbxBanco.get() == "Pedidos":
        lblStatus['text'] = 'Status = Pronto'
        lblOrdens['text'] = 'Favor informar a OP:'
    else:
        lblStatus['text'] = 'Status = Finalizado'
        lblOrdens['text'] = 'Favor informar o ID:'


def sql_Finalizar():
    if txtOrdens == "":
        messagebox.showwarning("Favor informar um item válido!")
        return
    if cbxBanco.get() == "":
        messagebox.showwarning("Favor selecionar um banco!")
        return
    if cbxBanco.get() == 'Pedidos':        
        sql_gerado = 'update '+cbxBanco.get()+' set ' + \
            lblStatus['text']+' , Termino = ' + str(date.today())+\
                " where OP_MAQ =  '"+txtOrdens.get()+ "';"
        txtFinalizados.insert(tk.END,"Ordem: "+txtOrdens.get()+"\n")
        return print(sql_gerado)
    else:
        sql_gerado = 'update '+cbxBanco.get()+' set ' + \
            lblStatus['text']+' , Termino = ' + str(date.today())+\
                " where seq =  "+txtOrdens.get()+ ";"
        txtFinalizados.insert(tk.END,"Item: "+txtOrdens.get()+"\n")
        return print(sql_gerado)


# Recursos da Janela
janela = tk.Tk()
janela.title('Finalizar processos')
lblBanco = tk.Label(janela, text='Informe o Banco que deseja finalizar um processo!')
tblFrame = tk.Frame(janela, relief='groove', borderwidth=2)
lblTabela = tk.Label(tblFrame, text='Selecione a Tabela:')
lblStatus = tk.Label(tblFrame, text='Status = ')
lblData = tk.Label(tblFrame, text='Data = '+hoje)
lblOrdens = tk.Label(tblFrame, text='Favor informar o ID!')
cbxBanco = ttk.Combobox(tblFrame, values=["Pedidos", "Laser"])
txtOrdens = tk.Entry(tblFrame)
btnFinalizar = tk.Button(janela, text='Finalizar',command=sql_Finalizar)
txtFinalizados = tk.Text(janela, width=30, height=10)


# layout da janela
lblBanco.grid(row=0, column=0, sticky='', pady=5)
tblFrame.grid(row=1, column=0)
lblTabela.grid(row=0, column=0, sticky='w', pady=5, padx=5)
cbxBanco.grid(row=0, column=1, sticky='w', padx=5)
lblStatus.grid(row=1, column=0, sticky='w', pady=5, padx=5)
lblData.grid(row=1, column=1, sticky='w', padx=5)
lblOrdens.grid(row=2, column=0, padx=5, pady=5)
txtOrdens.grid(row=2, column=1, sticky='w', padx=5)
btnFinalizar.grid(row=5, column=0, sticky='w', padx=5, pady=10)
txtFinalizados.grid(row=6, column=0, columnspan=2, pady=5)

cbxBanco.bind("<<ComboboxSelected>>", valor_cbx)


janela.mainloop()

import tkinter as tk
from tkinter import ttk
import interface_Finalizar as iff 
import interface_estado as ife


#def aba_update():


#Janelas
janela = tk.Tk()
janela.title("Atualizações Metabase")
janela.columnconfigure(1,minsize=50,weight=1)
janela.rowconfigure(1,minsize=50,weight=1)
janela.geometry("350x200")

aba_notebook = ttk.Notebook(janela)
aba1= ttk.Frame(aba_notebook)
aba2= ttk.Frame(aba_notebook)
aba3= ttk.Frame(aba_notebook)
aba_notebook.add(aba1, text='Finalizar')
aba_notebook.add(aba2, text='Estado')
aba_notebook.add(aba3, text='Delete')

iff.interface_finalizar(aba1,janela)
ife.interface_estado(aba2,janela)


#Recursos Janela
aba_notebook.grid(column=0)






janela.mainloop()



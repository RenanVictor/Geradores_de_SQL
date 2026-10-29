import tkinter as tk
from tkinter import ttk
import bancos
from interface_Finalizar import tabelas
import Conexao

def interface_comentario(root, mainRoot):
# funções
    def coluna_selecionada(event):
        if cbx_coluna.current() ==-1:
            lbl_campo_selecionado.grid_forget()
            txt_valor.grid_forget()
        else: 
            lbl_campo_selecionado.grid(row=3,column=0,sticky='w',padx=5)
            lbl_campo_selecionado['text'] = cbx_coluna.get()
            txt_valor.grid(row=3,column=1,sticky='w', padx=5)

        
    
    def update_estado():
        dict_banco = bancos.find_dict(cbx_banco.get())
        dict_banco['col_change'] = [cbx_coluna.get()]
        
        dicionario = {}
        if txt_valor.get()=='':
            dicionario[cbx_coluna.get()] = None
        else:
            if cbx_coluna.get()=='Previsao':
                from datetime import datetime as dt
                dicionario[cbx_coluna.get()] = dt.strptime(txt_valor.get(),"%d-%m-%Y").date()
            else:
                dicionario[cbx_coluna.get()] = txt_valor.get()
        if txt_item.get()!='':
            dicionario['item'] = txt_item.get()
            dict_banco['col_validacao'] = Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0]
        print(Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0])
        Conexao.validacao_update(dict_banco,dicionario)


    def update_alterar():
        update_estado()
        
        

#Recursos Janela
    mainRoot.title('Incluir valor')
    tblFrame = tk.Frame(root, relief='groove', borderwidth=2)
    tblBotoes = tk.Frame(root)
    lblTabela = tk.Label(tblFrame, text='Selecione a Tabela:')
    lblColuna = tk.Label(tblFrame, text='Selecione a coluna:')
    lbl_item = tk.Label(tblFrame, text='Informar a OP ou ID:')
    lbl_campo_selecionado = tk.Label(tblFrame,text='Valor atual:')
    lbl_info = tk.Label(tblFrame,text="Para datas, utilizar o formato DD-MM-YYYY")
    cbx_banco = ttk.Combobox(tblFrame, width=17, values=tabelas(bancos.dict_tabelas()))
    cbx_coluna = ttk.Combobox(tblFrame, width=17, values=['Previsao','Complemento'])
    txt_item = tk.Entry(tblFrame)
    txt_valor = tk.Entry(tblFrame)

    btnEstado = tk.Button(tblBotoes, text='Alterar', command=update_alterar)
    
#Layout da Janela
    tblFrame.grid(row=1, column=0)
    lblTabela.grid(row=0, column=0, sticky='w', pady=5, padx=5)
    cbx_banco.grid(row=0, column=1, sticky='w', padx=5)
    lblColuna.grid(row=1, column=0, sticky='w',pady=5, padx=5)
    cbx_coluna.grid(row=1, column=1, sticky='w', padx=5)
    lbl_item.grid(row=2, column=0, sticky='w',pady=5, padx=5)
    txt_item.grid(row=2, column=1, sticky='w', padx=5)
    
    tblBotoes.grid(row=2, column=0)
    btnEstado.grid(row=0, column=0, sticky='w',pady=10, padx=5)

    cbx_coluna.bind("<<ComboboxSelected>>",coluna_selecionada)

janela = tk.Tk()
interface_comentario(janela,janela)
janela.mainloop()
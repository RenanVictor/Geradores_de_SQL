import tkinter as tk
from tkinter import ttk
import bancos
from interface_Finalizar import tabelas
import Conexao

def interface_estado(root, mainRoot):
# funções
    def estados_cbx(event):
        dict_banco = bancos.find_dict(cbx_banco.get())
        valores = Conexao.select_status(dict_banco['banco'])
        cbx_estado['values'] =valores
        return valores
    
    def update_estado():
        dict_banco = bancos.find_dict(cbx_banco.get())
        dict_banco['col_change'] = ['Status']
        
        dicionario = {}
        dicionario['status'] = cbx_estado.get()
        if txtInfo.get()!='':
            dicionario['item'] = txtInfo.get()
            dict_banco['col_validacao'] = Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0]
        print(Conexao.atualiza_banco('select',dict_banco,dicionario['item'])['retorno'][0])
        Conexao.validacao_update(dict_banco,dicionario)


    def update_alterar():
        update_estado()
        
        

#Recursos Janela
    mainRoot.title('Alterar Estado')
    tblFrame = tk.Frame(root, relief='groove', borderwidth=2)
    tblBotoes = tk.Frame(root)
    lblTabela = tk.Label(tblFrame, text='Selecione a Tabela:')
    lblEstado = tk.Label(tblFrame, text='Slecione o Estado:')
    lblinfo = tk.Label(tblFrame, text='Favor informar o ID:')
    cbx_banco = ttk.Combobox(tblFrame, width=17, values=tabelas(bancos.dict_tabelas()))
    cbx_estado = ttk.Combobox(tblFrame, width=17, values='')
    txtInfo = tk.Entry(tblFrame)
    btnEstado = tk.Button(tblBotoes, text='Alterar', command=update_alterar)
    
#Layout da Janela
    tblFrame.grid(row=1, column=0)
    lblTabela.grid(row=0, column=0, sticky='w', pady=5, padx=5)
    cbx_banco.grid(row=0, column=1, sticky='w', padx=5)
    lblEstado.grid(row=1, column=0, sticky='w',pady=5, padx=5)
    cbx_estado.grid(row=1, column=1, sticky='w', padx=5)
    lblinfo.grid(row=2, column=0, sticky='w',pady=5, padx=5)
    txtInfo.grid(row=2, column=1, sticky='w', padx=5)
    tblBotoes.grid(row=2, column=0)
    btnEstado.grid(row=0, column=0, sticky='w',pady=10, padx=5)

    cbx_banco.bind("<<ComboboxSelected>>",estados_cbx)

'''janela = tk.Tk()
interface_estado(janela,janela)
janela.mainloop()'''
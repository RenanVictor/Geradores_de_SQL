import tkinter as tk
from tkinter import ttk
from datetime import date
import Mensagens
import log_usuario 
import bancos
import Conexao



# Variaveis
hoje = date.today().strftime("%d/%m/%Y")
dict_banco = {}
list_valores = {}

def tabelas(registros):
    list_tabela=[]
    for registro in registros:
        list_tabela.append(registro['nome'])
    return list_tabela

# Funções
def interface_finalizar(root, mainRoot):
    

    def valor_cbx(event):
        global dict_banco
        dict_banco = bancos.find_dict(cbxBanco.get())
        if cbxBanco.get() == "Pedidos":
            lblStatus['text'] = "Status = 'Pronto'"
            lblOrdens['text'] = 'Favor informar a OP:'
            lbl_maquina.grid_forget()
            cbx_maquina.grid_forget()
            dict_banco['status'] = 'Pronto'
            dict_banco['cancelar'] = 'Montagem'
        elif cbxBanco.get() == "Comp.":
            lblStatus['text'] = "Status = 'Reportada'"
            lblOrdens['text'] = 'Favor informar o ID:'
            lbl_maquina.grid_forget()
            cbx_maquina.grid_forget()
            dict_banco['status'] = 'Reportada'
            dict_banco['cancelar'] = 'Primários'
        else:
            lbl_maquina.grid(row=3, column=0, sticky='w', padx=5, pady=5)
            lblStatus['text'] = "Status = 'Finalizado'"
            lblOrdens['text'] = 'Favor informar o ID:'
            lbl_maquina.grid(row=3, column=0, sticky='w', padx=5, pady=5)
            cbx_maquina.grid(row=3, column=1, sticky='w', padx=5, pady=5)
            dict_banco['status'] = 'Finalizado'
            dict_banco['cancelar'] = 'Programado'

    def update_finalizar():    
        global dict_banco
        dicionario = {}
        dicionario['status'] = dict_banco['status']
        dicionario['Termino'] = date.today()
        dicionario['maquina'] = cbx_maquina.get()
        dicionario['item'] = txtOrdens.get()
        return dicionario
        
    def update_cancelar():    
        global dict_banco
        dicionario = {}
        dicionario['status'] = dict_banco['cancelar']
        dicionario['Termino'] = ''
        dicionario['maquina'] = cbx_maquina.get()
        dicionario['item'] = txtOrdens.get()
        return dicionario

    def btn_finalizar():
        global dict_banco
        log = log_usuario.usuario(dict_banco,update_finalizar())
        log.insert_usuario()
        upgrade_register()
        return Conexao.validacao_update(dict_banco,update_finalizar())
        
    def sql_Cancelar():
        return

    def upgrade_register():
        txtFinalizados.delete('1.0',tk.END)
        registros = log_usuario.return_last_register()
        txtFinalizados.insert(tk.END,'BANCOS |   INFO   | DATA \n')
        for lista in registros:
            for item in lista:
                if isinstance(item,date):
                    txtFinalizados.insert(tk.END,item)
                else:
                    txtFinalizados.insert(tk.END,item[0:9])
                    txtFinalizados.insert(tk.END,'|')
            txtFinalizados.insert(tk.END,'\n')


# Recursos da Janela
    mainRoot.title('Finalizar')
    mainRoot.geometry("275x400")
    
    #janela = tk.Tk()
    #janela.title('Finalizar processos')
    lblBanco = tk.Label(
        root, text='Informe o Banco que deseja finalizar um processo!')
    tblFrame = tk.Frame(root, relief='groove', borderwidth=2)
    tblBotoes = tk.Frame(root)
    lblTabela = tk.Label(tblFrame, text='Selecione a Tabela:')
    lblStatus = tk.Label(tblFrame, text='Status = ')
    lblData = tk.Label(tblFrame, text='Data = '+hoje)
    lblOrdens = tk.Label(tblFrame, text='Favor informar o ID!')
    cbxBanco = ttk.Combobox(tblFrame, width=17, values=tabelas(bancos.dict_tabelas()))
    txtOrdens = tk.Entry(tblFrame)
    btnFinalizar = tk.Button(tblBotoes, text='Finalizar', command=btn_finalizar)
    btnCancelar = tk.Button(tblBotoes, text='Cancelar', command=sql_Cancelar)
    txtFinalizados = tk.Text(root, width=30, height=10)
    lbl_maquina = tk.Label(tblFrame, text='Máquina')
    cbx_maquina = ttk.Combobox(tblFrame, width=17, values=[
                            'DOBRA-1','DOBRA-2','LASER-1', 'LASER-2', 'LASER-3', 'PLASMA','PRENSA','PUNC.','TUBE'])

    # layout da janela
    lblBanco.grid(row=0, column=0, sticky='', pady=5)
    tblFrame.grid(row=1, column=0)
    lblTabela.grid(row=0, column=0, sticky='w', pady=5, padx=5)
    cbxBanco.grid(row=0, column=1, sticky='w', padx=5)
    lblStatus.grid(row=1, column=0, sticky='w', pady=5, padx=5)
    lblData.grid(row=1, column=1, sticky='w', padx=5)
    lblOrdens.grid(row=2, column=0, padx=5, pady=5)
    txtOrdens.grid(row=2, column=1, sticky='w', padx=5)
    tblBotoes.grid(row=5, column=0, sticky='w')
    btnFinalizar.grid(row=0, column=0, sticky='w', padx=5, pady=10)
    btnCancelar.grid(row=0, column=1, sticky='w', padx=5, pady=10)
    txtFinalizados.grid(row=6, column=0, columnspan=2, pady=5)

    cbxBanco.bind("<<ComboboxSelected>>", valor_cbx)
    upgrade_register()


'''janela = tk.Tk()
interface_finalizar(janela,janela)
janela.mainloop()'''

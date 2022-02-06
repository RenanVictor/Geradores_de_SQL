import tkinter as tk
from tkinter import ttk
from datetime import date
import Mensagens


# Variaveis
hoje = date.today().strftime("%d/%m/%Y")


# Funções
def valor_cbx(event):
    if cbxBanco.get() == "Pedidos":
        lblStatus['text'] = "Status = 'Pronto'"
        lblOrdens['text'] = 'Favor informar a OP:'
        lbl_maquina.grid_forget()
        cbx_maquina.grid_forget()
    else:
        lbl_maquina.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        lblStatus['text'] = "Status = 'Finalizado'"
        lblOrdens['text'] = 'Favor informar o ID:'
        lbl_maquina.grid(row=3, column=0, sticky='w', padx=5, pady=5)
        cbx_maquina.grid(row=3, column=1, sticky='w', padx=5, pady=5)


def sql_finalizar_pedidos():
    sql_gerado = 'update '+cbxBanco.get()+' set ' + \
        lblStatus['text']+" , Termino = '" + str(date.today()) +\
        "' where OP_MAQ =  '"+txtOrdens.get() + "';"
    return sql_gerado

def sql_finalizar_laser():
    sql_gerado = "update plan_laser set " + \
        lblStatus['text']+" , Termino = '" + str(date.today()) + "', maquina = '"+cbx_maquina.get() +\
        "' where seq =  "+txtOrdens.get() + ";"
    return sql_gerado


def btn_finalizar():
    import Conexao as updates
    if txtOrdens.get() == "":
        return Mensagens.item_invalido()
    if cbxBanco.get() == "":
        return Mensagens.banco_invalido()
    if cbxBanco.get() == 'Pedidos':
        txtFinalizados.insert(tk.END, "Ordem: "+txtOrdens.get()+"\n")
        print(sql_finalizar_pedidos())
        return updates.status_montagem(updates.retorna_status(txtOrdens.get(),cbxBanco.get()),sql_finalizar_pedidos())
    else:
        if cbx_maquina.get() !='':
            txtFinalizados.insert(tk.END, "Item: "+txtOrdens.get()+"\n")
            print(sql_finalizar_laser())
            return updates.status_programado(updates.retorna_status(txtOrdens.get(),cbxBanco.get()),sql_finalizar_laser())
        else:
            return Mensagens.sem_maquina()


def sql_Cancelar():
    import Conexao as updates
    if cbxBanco.get() == "":
        return Mensagens.banco_invalido()
    if txtOrdens.get() == "":
        return Mensagens.item_invalido()
    if cbxBanco.get() == 'Pedidos':
        sql_gerado = 'update '+cbxBanco.get() +" set status = 'Montagem', Termino = null where OP_MAQ =  '"+txtOrdens.get()+"';"
        txtFinalizados.insert(tk.END, "Cancelado Ordem: "+txtOrdens.get()+"\n")
        print(sql_gerado)
        return updates.terminado(updates.retorna_termino(txtOrdens.get()),sql_gerado)
    else:
        sql_gerado = "update plan_laser set status = 'Programado', Termino = null where seq =  "+txtOrdens.get() + ";"
        txtFinalizados.insert(tk.END, "Cancelado Item: "+txtOrdens.get()+"\n")
        print(sql_gerado)
        return updates.status_finalizado(updates.retorna_status(txtOrdens.get(),cbxBanco.get()),sql_gerado)


# Recursos da Janela
janela = tk.Tk()
janela.title('Finalizar processos')
lblBanco = tk.Label(
    janela, text='Informe o Banco que deseja finalizar um processo!')
tblFrame = tk.Frame(janela, relief='groove', borderwidth=2)
tblBotoes = tk.Frame(janela)
lblTabela = tk.Label(tblFrame, text='Selecione a Tabela:')
lblStatus = tk.Label(tblFrame, text='Status = ')
lblData = tk.Label(tblFrame, text='Data = '+hoje)
lblOrdens = tk.Label(tblFrame, text='Favor informar o ID!')
cbxBanco = ttk.Combobox(tblFrame, width=17, values=["Pedidos", "Laser"])
txtOrdens = tk.Entry(tblFrame)
btnFinalizar = tk.Button(tblBotoes, text='Finalizar', command=btn_finalizar)
btnCancelar = tk.Button(tblBotoes, text='Cancelar', command=sql_Cancelar)
txtFinalizados = tk.Text(janela, width=30, height=10)
lbl_maquina = tk.Label(tblFrame, text='Máquina')
cbx_maquina = ttk.Combobox(tblFrame, width=17, values=[
                           'LASER-1', 'LASER-2', 'LASER-3', 'PLASMA', 'PUNC.'])

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

janela.mainloop()

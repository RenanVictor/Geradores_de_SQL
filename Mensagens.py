import tkinter.messagebox as msx

def retorna_status_finalizado(number):
    if number==0:
        return msx.showerror(title='Item não encontrado!',message='Favor verificar o item informado!')
    if number==1:
        return msx.showinfo(title='Finalizado',message='Item finalizado com sucesso!')
    return 

def item_invalido():
    return msx.showwarning(title='Item inválido!',message='Favor informar um item válido!')
    
def banco_invalido():
    return msx.showwarning(title='Banco de Inválido',message='Favor selecionar um banco!')


def nao_montagem():
    return msx.showwarning(title='Não Finalizado',message='O item informado não está no status de montagem!')

def nao_programado():
    return msx.showwarning(title='Não Finalizado',message='O item informado não está no status de programado!')

def nao_terminado():
    return msx.showwarning(title='Não Terminado',message='O item informado não está finalizado e não pode ser cancelado!')
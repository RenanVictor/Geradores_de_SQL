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


    
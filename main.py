from tkinter import *
from tkinter import messagebox
from tkinter.ttk import Treeview

from tkcalendar import DateEntry
from view import *

cor_preta = "#f0f3f5"
cor_branca = "#feffff"
cor_verde = "#4fa882"
cor_letra = "#403d3d"
cor_azul = "#038cfc"
cor_vermelha = "#ef5350"
cor_verde_forte = "#263238"
cor_azul_claro = "#e9edf5"

janela = Tk()
janela.geometry("1043x453")
janela.configure(background=cor_azul_claro)

frame_esquerda_cima = Frame(janela, width=310, height=50, bg=cor_verde, relief='flat')
frame_esquerda_cima.grid(row=0, column=0)
frame_esquerda_baixo = Frame(janela, width=310, height=403, bg=cor_branca, relief='flat')
frame_esquerda_baixo.grid(row=1, column=0, sticky='NSEW', padx=0, pady=1)
frame_direita = Frame(janela, width=588, height=403, bg=cor_branca, relief='flat')
frame_direita.grid(row=0, column=1, sticky='NSEW', padx=1, pady=0, rowspan=2)
nome_do_app = Label(frame_esquerda_cima, text='Controlador de estudos', anchor=NW, font='Ivy 13 bold', bg=cor_verde,
                    fg=cor_branca, relief='flat')
nome_do_app.place(x=10, y=20)

# Matéria
label_materia = Label(frame_esquerda_baixo, text='Matéria *', anchor=NW, font='Ivy 10 bold', bg=cor_branca,
                      fg="#403d3d", relief='flat')
label_materia.place(x=10, y=10)
entry_materia = Entry(frame_esquerda_baixo, width=45, justify='left', relief='solid')
entry_materia.place(x=15, y=40)
# Assunto
label_assunto = Label(frame_esquerda_baixo, text='Assunto *', anchor=NW, font='Ivy 10 bold', bg=cor_branca,
                      fg="#403d3d", relief='flat')
label_assunto.place(x=10, y=70)
entry_assunto = Entry(frame_esquerda_baixo, width=45, justify='left', relief='solid')
entry_assunto.place(x=15, y=100)
# minutos
label_minutos = Label(frame_esquerda_baixo, text='Minutos estudados *', anchor=NW, font='Ivy 10 bold', bg=cor_branca,
                      fg="#403d3d", relief='flat')
label_minutos.place(x=10, y=130)
entry_minutos = Entry(frame_esquerda_baixo, width=12, justify='left', relief='solid')
entry_minutos.place(x=15, y=160)
# data
label_data = Label(frame_esquerda_baixo, text='Data (mm/dd/yy)*', anchor=NW, font='Ivy 10 bold', bg=cor_branca,
                   fg="#403d3d", relief='flat')
label_data.place(x=160, y=130)
entry_data = DateEntry(frame_esquerda_baixo, width=12, background="dark blue", foreground="white", borderwidth=2,
                       year=2024)
entry_data.place(x=160, y=160)
# descricao
label_descricao = Label(frame_esquerda_baixo, text='Descrição *', anchor=NW, font='Ivy 10 bold', bg=cor_branca,
                        fg="#403d3d", relief='flat')
label_descricao.place(x=10, y=190)
entry_descricao = Entry(frame_esquerda_baixo, width=45, justify='left', relief='solid')
entry_descricao.place(x=15, y=220)

global tree


def insert():
    materia = entry_materia.get()
    assunto = entry_assunto.get()
    minutos = entry_minutos.get()
    data = entry_data.get()
    descricao = entry_descricao.get()

    lista = [materia, assunto, minutos, data, descricao]

    if materia == '':
        messagebox.showerror("Campo 'materia' não pode ser vazio")
    else:
        insert_info(lista)
        messagebox.showinfo("Dados inseridos com sucesso")
        entry_materia.delete(0, 'end')
        entry_assunto.delete(0, 'end')
        entry_minutos.delete(0, 'end')
        entry_data.delete(0, 'end')
        entry_descricao.delete(0, 'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    show()


def update():
    try:
        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']

        valor_id = tree_lista[0]

        entry_materia.delete(0, 'end')
        entry_assunto.delete(0, 'end')
        entry_minutos.delete(0, 'end')
        entry_data.delete(0, 'end')
        entry_descricao.delete(0, 'end')

        entry_materia.insert(0, tree_lista[1])
        entry_assunto.insert(0, tree_lista[2])
        entry_minutos.insert(0, tree_lista[3])
        entry_data.insert(0, tree_lista[4])
        entry_descricao.insert(0, tree_lista[5])

        def up():
            materia = entry_materia.get()
            assunto = entry_assunto.get()
            minutos = entry_minutos.get()
            data = entry_data.get()
            descricao = entry_descricao.get()

            lista = [materia, assunto, minutos, data, descricao, valor_id]

            if materia == '':
                messagebox.showerror("Campo 'materia' não pode ser vazio")
            else:
                update_info(lista)
                messagebox.showinfo("Dados atualizados com sucesso")
                entry_materia.delete(0, 'end')
                entry_assunto.delete(0, 'end')
                entry_minutos.delete(0, 'end')
                entry_data.delete(0, 'end')
                entry_descricao.delete(0, 'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            show()
        botao_confirmar = Button(frame_esquerda_baixo, command=up, text='Confirmar', width=10,
                                 font='Ivy 9 bold', bg=cor_verde_forte, fg=cor_branca,
                                 relief='raised', overrelief='ridge')
        botao_confirmar.place(x=105, y=310)
    except IndexError:
        messagebox.showerror("Selecione uma das linhas na tabela")


def show():

    global tree

    lista = show_info()
    tabela_head = ['ID', 'Matéria', 'Assunto', 'Minutos', 'Data', 'Descrição']
    tree = Treeview(frame_direita, selectmode="extended", columns=tabela_head, show="headings")
    vsb = Scrollbar(frame_direita, orient="vertical", command=tree.yview)
    hsb = Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')

    frame_direita.grid_rowconfigure(0, weight=12)

    hd = ["nw", "nw", "nw", "nw", "nw", "center"]
    h = [30, 170, 140, 100, 120, 145]
    n = 0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        tree.column(col, width=h[n], anchor=hd[n])

        n += 1

    for item in lista:
        tree.insert('', 'end', values=item)


def delete():
    try:
        tree_dados = tree.focus()
        tree_dicionario = tree.item(tree_dados)
        tree_lista = tree_dicionario['values']

        valor_id = [tree_lista[0]]
        delete_info(valor_id)
        messagebox.showinfo("Dados deletados com sucesso")

        for widget in frame_direita.winfo_children():
            widget.destroy()
        show()

    except IndexError:
        messagebox.showerror("Selecione uma das linhas na tabela")


botao_inserir = Button(frame_esquerda_baixo, command=insert, text='Inserir', width=10, font='Ivy 9 bold',
                       bg=cor_azul, fg=cor_branca, relief='raised', overrelief='ridge')
botao_inserir.place(x=15, y=280)
botao_atualizar = Button(frame_esquerda_baixo, command=update, text='Atualizar', width=10, font='Ivy 9 bold',
                         bg=cor_verde_forte, fg=cor_branca, relief='raised', overrelief='ridge')
botao_atualizar.place(x=105, y=280)
botao_deletar = Button(frame_esquerda_baixo, command= delete, text='Deletar', width=10, font='Ivy 9 bold', bg=cor_vermelha,
                       fg=cor_branca, relief='raised', overrelief='ridge')
botao_deletar.place(x=195, y=280)

show()

janela.mainloop()

########## Importando o Tkinter ##########
from tkinter import *
from tkinter import font

from tkinter import ttk

from tkinter import messagebox

########## Importando tkcalendar ##########
from tkcalendar import Calendar, DateEntry

########## Importando Views ##########
from view import *


########## Cores ##########

co0 = "#f0f3f5"
co1 = "#feffff"
co2 = "#4fa882"
co3 = "#38576b"
co4 = "#403d3d" 
co5 = "#e06636"
co6 = "#038cfc"
co7 = "#ef5350"
co8 = "#263238"
co9 = "#e9edf5"

########## Criando a janela ##########

janela = Tk()
janela.title("")
janela.geometry('1043x600')
janela.configure(background=co9)
janela.resizable(width=False, height=False)

########## Divindo a janela ##########

frame_cima = Frame(janela, width=310, height=50, bg=co2, relief='flat')
frame_cima.grid (row=0, column=0)

frame_baixo = Frame(janela, width=310, height=540, bg=co1, relief='flat')
frame_baixo.grid (row=1, column=0, sticky=NSEW, padx=0,pady=1)

frame_direita = Frame(janela, width=588, height=403, bg=co1, relief='flat')
frame_direita.grid (row=0, column=1, rowspan=2,padx=1,pady=0, sticky=NSEW)

########## Label Cima ##########

app_nome = Label(frame_cima,text='Formulário de Consultoria', anchor=NW, font=('Ivy 13 bold'), bg=co2, fg=co1, relief='flat')
app_nome.place(x=10, y=20)

########## tree ##########
global tree

########## Função inserir ##########

def inserir():
    cpf = e_cpf.get()
    nome = e_nome.get()
    sexo = e_sexo.get()
    idade = e_idade.get()
    nasc = e_nasc.get()
    av1 = e_av1.get()
    av2 = e_av2.get()
    # media = e_media.get()

    

    if nome == '' and cpf == '':
        messagebox.showerror('Erro','O nome ou cpf não pode ser vazio')
    else:
        # Calcular a média
        media = (float(av1) + float(av2)) / 2
        lista = [cpf, nome, sexo, idade, nasc, av1, av2, media]

        inserir_info(lista)
        messagebox.showinfo('Sucesso', 'Os dados foram inseridos com sucesso')

        e_cpf.delete(0,'end')
        e_nome.delete(0,'end')
        e_sexo.delete(0,'end')
        e_idade.delete(0,'end')
        e_nasc.delete(0,'end')
        e_av1.delete(0,'end')
        e_av2.delete(0,'end')
        e_media.delete(0,'end')

    for widget in frame_direita.winfo_children():
        widget.destroy()

    mostrar()

########## Função Atualizar ##########

def atualizar():
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        tree_lista = treev_dicionario['values']

        valor_cpf = tree_lista[0]

        e_cpf.delete(0, 'end')
        e_nome.delete(0,'end')
        e_sexo.delete(0,'end')
        e_idade.delete(0,'end')
        e_nasc.delete(0,'end')
        e_av1.delete(0,'end')
        e_av2.delete(0,'end')
        e_media.delete(0,'end')

        e_cpf.insert(0,tree_lista[0])
        e_nome.insert(0,tree_lista[1])
        e_sexo.insert(0,tree_lista[2])
        e_idade.insert(0,tree_lista[3])
        e_nasc.insert(0,tree_lista[4])
        e_av1.insert(0,tree_lista[5])
        e_av2.insert(0,tree_lista[6])
        e_media.insert(0,tree_lista[7])
        
        ########## Função update ##########

        def update():
            cpf = e_cpf.get()
            nome = e_nome.get()
            sexo = e_sexo.get()
            idade = e_idade.get()
            nasc = e_nasc.get()
            av1 = e_av1.get()
            av2 = e_av2.get()
            # media = e_media.get()

            if nome == '' and cpf == '':
                messagebox.showerror('Erro','O nome não pode ser vazio')
            else:
                
                media = (float(av1) + float(av2)) / 2
                lista = [cpf, nome, sexo, idade, nasc, av1, av2, media, valor_cpf]

                atualizar_info(lista)
                messagebox.showinfo('Sucesso', 'Os dados foram atualizados com sucesso')

                e_cpf.delete(0,'end')
                e_nome.delete(0,'end')
                e_sexo.delete(0,'end')
                e_idade.delete(0,'end')
                e_nasc.delete(0,'end')
                e_av1.delete(0,'end')
                e_av2.delete(0,'end')
                e_media.delete(0,'end')

            for widget in frame_direita.winfo_children():
                widget.destroy()

            mostrar()

########## Botão Atualizar ##########
        b_confirmar = Button(frame_baixo,command=update, text='Atualizar', width=10, font=('Ivy 7 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
        b_confirmar.place(x=115, y=470)
        #(x=110, y=500)

    except IndexError:
      messagebox.showerror('Erro','Selecione um dos dados da tabela')
  
########## Função atualizar ##########
def deletar():
    try:
      treev_dados = tree.focus()
      treev_dicionario = tree.item(treev_dados)
      tree_lista = treev_dicionario['values']

      valor_cpf = [tree_lista[0]]

      deletar_info(valor_cpf)
      messagebox.showinfo('Sucesso', 'Os dados foram deletados da tabela com sucesso')

      for widget in frame_direita.winfo_children():
            widget.destroy()

      mostrar()

      
    except IndexError:
      messagebox.showerror('Erro','Selecione um dos dados da tabela')

########## Configurando Frame baixo ##########

########## CPF ##########
l_cpf = Label(frame_baixo,text='CPF *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_cpf.place(x=10, y=35)
e_cpf = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_cpf.place(x=15, y=65)

########## Nome ##########
l_nome = Label(frame_baixo,text='Nome *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nome.place(x=10, y=95)
e_nome = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_nome.place(x=15, y=125)

########## Sexo ##########
l_sexo = Label(frame_baixo,text='Sexo *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_sexo.place(x=10, y=155)
e_sexo = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_sexo.place(x=15, y=185)

########## idade ##########
l_idade = Label(frame_baixo,text='Idade *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_idade.place(x=10, y=215)
e_idade = Entry(frame_baixo, width=45, justify='left', relief='solid')
e_idade.place(x=15, y=245)

########## Data de Nascimento ##########
l_nasc = Label(frame_baixo,text='Data de nascimento *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_nasc.place(x=10, y=275)
e_nasc = DateEntry(frame_baixo, background='darkblue', foreground='white', borderwidth=2, year=2023)
e_nasc.place(x=15, y=305)

########## AV1 ##########
l_av1 = Label(frame_baixo,text='AV1 *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_av1.place(x=10, y=335)
e_av1 = Entry(frame_baixo, width=12, justify='left', relief='solid')
e_av1.place(x=15, y=365)

########## AV2 ##########
l_av2 = Label(frame_baixo,text='AV2 *', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
l_av2.place(x=160, y=335)
e_av2 = Entry(frame_baixo, width=21, justify='left', relief='solid')
e_av2.place(x=140, y=365)

########## Média ##########
l_media = Label(frame_baixo,text='Média ', anchor=NW, font=('Ivy 10 bold'), bg=co1, fg=co4, relief='flat')
# l_media.place(x=15, y=410)
l_media.place(x=15, y=1000)

e_media = Entry(frame_baixo, width=45, justify='left', relief='solid')
# e_media.place(x=15, y=440)
e_media.place(x=15, y=1000)

########## Botão inserir ##########
b_inserir = Button(frame_baixo,command=inserir, text='Inserir', width=10, anchor=NW, font=('Ivy 9 bold'), bg=co6, fg=co1, relief='raised', overrelief='ridge')
b_inserir.place(x=15, y=500)

########## Botão Atualizar ##########
b_atualizar = Button(frame_baixo,command=atualizar, text='Selecionar', width=10, anchor=NW, font=('Ivy 9 bold'), bg=co2, fg=co1, relief='raised', overrelief='ridge')
b_atualizar.place(x=110, y=500)

########## Botão deletar ##########
b_deletar = Button(frame_baixo,command=deletar, text='Deletar', width=10, anchor=NW, font=('Ivy 9 bold'), bg=co7, fg=co1, relief='raised', overrelief='ridge')
b_deletar.place(x=205, y=500)

########## Frame direita ##########

def mostrar():

  global tree

  lista = mostrar_info()

########## Lista para cabeçario ##########
  tabela_head = ['CPF', 'Nome', 'sexo', 'idade','Data Nascimento', 'AV1', 'AV2', 'Media']

########## Criando a tabela ##########
  tree = ttk.Treeview(frame_direita, selectmode="extended",
                      columns=tabela_head, show="headings")
########## Vertical scrollbar ##########
  vsb = ttk.Scrollbar(frame_direita, orient="vertical", command=tree.yview)

########## Horizontal scrollbar ##########
  hsb = ttk.Scrollbar(frame_direita, orient="horizontal", command=tree.xview)

  tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
  tree.grid(column=0, row=0, sticky='nsew')
  vsb.grid(column=1, row=0, sticky='ns')
  hsb.grid(column=0, row=1, sticky='ew')

  frame_direita.grid_rowconfigure(0, weight=12)

  hd=["nw","nw","nw","nw","nw", "center", "center", "center"]
  h=[150, 150, 80, 50, 120, 50, 50, 50]
  n=0

  for col in tabela_head:
      tree.heading(col, text=col.title(), anchor=CENTER)
      # adjust the column's width to the header string
      tree.column(col, width=h[n], anchor=hd[n])

      n+=1

     

  for item in lista:
      tree.insert('', 'end', values=item)

########## chamando a função mostrar

mostrar()

janela.mainloop()
from tkinter import *
import os

caminho=os.path.dirname(__file__)
namearchiver=caminho+"\\nomes.txt"
def printdados():
    archiver=open(namearchiver,"a")
    
    archiver.write("Nome:{}".format(vnome.get()))
    archiver.write("\nTelefone:{}".format(vtelefone.get()))
    archiver.write("\nEmail:{}".format(vemail.get()))
    archiver.write("\nInformações Adicionais :{}".format(vinfoadicionais.get("1.0",END)))
    archiver.write("\n\n")
    archiver.close()
janela=Tk()
janela.title("RELATÓRIO :")
janela.geometry("500x500")
janela.configure(background="#dde")
Label(janela,text="Nome:",background="#dde",foreground="#009",anchor=W).place(x=10,y=10,width=100,height=20)
vnome=Entry(janela)
vnome.place(x=70,y=10,width=200,height=20)
Label(janela,text="Telefone:",background="#dde",foreground="#009",anchor=W).place(x=9,y=40,width=100,height=20)
vtelefone=Entry(janela)
vtelefone.place(x=70,y=40)
Label(janela,text="Email:",background="#dde",foreground="#009",anchor=W).place(x=10,y=70,width=100,height=20)
vemail=Entry(janela)
vemail.place(x=70,y=70,width=300,height=20)
Label(janela,text="Informações Adicionais :",background="#dde",foreground="#009",anchor=W).place(x=10,y=150)
vinfoadicionais=Text(janela)
vinfoadicionais.place(x=10,y=190,width=300,height=270)
bt1=Button(janela,text="Armazenar dados",command=printdados)
bt1.place(x=10,y=480,width=100,height=20)
janela.mainloop()
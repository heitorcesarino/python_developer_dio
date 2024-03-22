import webbrowser
from tkinter import *

#root vai representar o tkinter que nao tera nome
root = Tk( )

#definindo titulo e tamanho da caixa
root.title('Abrir Browser')
root.geometry('300x200')

#definindo funcao que chamara a url do google
def google():
    webbrowser.open('www.google.com')

#criando botao que ao clicar abrira o google
mygoogle = Button(root, text='Abrir o Google', command=google).pack(pady=20)
root.mainloop()
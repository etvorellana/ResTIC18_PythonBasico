from tkinter import Label       # importa um objeto widget específico
widget = Label(None, text='Olá mundo GUI!') # cria um widget
widget.pack()                   # organiza o widget na janela
widget.mainloop()               # inicia o loop de eventos
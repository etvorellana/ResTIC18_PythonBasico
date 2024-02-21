import tkinter as tk       
root = tk.Tk()                             # cria uma janela
root.title('Exemplo 02')                # configura o título da janela
widget = tk.Label(root)                    # cria um widget dentro da janela
widget.config(text='Hello GUI world!')  # configura o texto do widget
#widget.pack(side=tk.TOP)  # organiza o widget na janela
#widget.pack(side=tk.TOP, expand=tk.YES)  # organiza o widget na janela
widget.pack(side=tk.TOP, expand=tk.YES, fill=tk.BOTH)  # organiza o widget na janela
root.mainloop()               # inicia o loop de eventos
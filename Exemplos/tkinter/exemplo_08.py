import sys
import tkinter as tk
root = tk.Tk()   
root.title('Exemplo 08')

def hello(event):
    print('Press twice to exit')    

def quit(event):
    print('Hello, I must be going...') 
    sys.exit()

widget = tk.Button(root, text='Hello event world')
widget.pack()
widget.bind('<Button-1>', hello)    # bind left mouse clicks 
widget.bind('<Double-1>', quit)     # bind double-left clicks 
widget.mainloop()
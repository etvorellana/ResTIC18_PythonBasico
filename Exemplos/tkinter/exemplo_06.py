import sys
import tkinter as tk
root = tk.Tk()   
root.title('Exemplo 06')
def quit():
    print('Hello, I must be going...') 
    sys.exit()
widget = tk.Button(root, text='Hello event world', command=quit) 
widget.pack()
root.mainloop()
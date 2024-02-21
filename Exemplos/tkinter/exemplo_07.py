import sys
import tkinter as tk
root = tk.Tk()   
root.title('Exemplo 07')
widget = tk.Button(root, text='Hello event world',
                   command=(lambda: print('Hello lambda world') or sys.exit()) )
widget.pack()
root.mainloop()
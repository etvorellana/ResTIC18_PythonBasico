import tkinter as tk
root = tk.Tk()   
root.title('Exemplo 05')
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT) 
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES) 
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)      
#tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES, fill=tk.X)      
tk.Button(root, text='press', command=root.quit).pack(side=tk.LEFT, expand=tk.YES, fill=tk.Y)      
root.mainloop()
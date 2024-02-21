import tkinter as tk


def main():
    root = tk.Tk()   
    root.title('Exemplo 09')
    tk.labelfont = ('times', 20, 'bold')
    widget = tk.Label(root, text='Hello config world') 
    widget.config(bg='black', fg='yellow') 
    widget.config(font=tk.labelfont) 
    widget.config(height=3, width=20) 
    widget.pack(expand=tk.YES, fill=tk.BOTH) 
    root.mainloop()

if __name__ == '__main__':
    main()



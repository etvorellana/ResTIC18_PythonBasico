import tkinter as tk


def main():
    root = tk.Tk()   
    root.title('Exemplo 09')
    tk.labelfont = ('times', 20, 'bold')
    widget = tk.Button(text='Spam', padx=10, pady=10)
    widget.pack(padx=20, pady=20) 
    widget.config(cursor='gumby')
    widget.config(bd=8, relief=tk.RAISED)
    widget.config(bg='dark green', fg='white') 
    widget.config(font=('helvetica', 20, 'underline italic'))
    root.mainloop()

if __name__ == '__main__':
    main()


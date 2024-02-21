import tkinter as tk

def greeting():
    print('Hello stdout world!...')

def main():
    root = tk.Tk()   
    root.title('Exemplo 09')
    win = tk. Frame(root)
    win.pack()
    tk.Button(win, text='Hello', command=greeting).pack(side=tk.LEFT, anchor=tk.N) 
    tk.Label(win, text='Hello container world').pack(side=tk.TOP)
    tk.Button(win, text='Quit', command=win.quit).pack(side=tk.RIGHT)
    root.mainloop()

if __name__ == '__main__':
    main()


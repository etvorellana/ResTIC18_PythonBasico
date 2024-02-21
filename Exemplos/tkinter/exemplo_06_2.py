import sys
import tkinter as tk

def quit():
    print('Hello, I must be going...') 
    sys.exit()
    #root.quit()

def main():
    root = tk.Tk()   
    root.title('Exemplo 06')
    widget = tk.Button(root, text='Hello event world', command=quit) 
    widget.pack()
    root.mainloop()

if __name__ == '__main__':
    main()

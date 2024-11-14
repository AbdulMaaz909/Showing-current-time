import tkinter as tk
from time import strftime

root =tk.Tk()
root.title('Digital Clock')

def time():
    srting = strftime('%H:%M:%S \n %D')
    tk.label.config(text=srting)
    tk.label.after(1000,time)


tk.label = tk.Label(root,font=('cakibri',50,'bold'),background='yellow',foreground='black')
tk.label.pack(anchor='center')

time()
root.mainloop()
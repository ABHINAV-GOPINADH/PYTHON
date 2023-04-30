from tkinter import *
from tkinter import filedialog


root=Tk()
root.geometry('600x600')
root.title('notepad')
root.config(bg='lightblue')
root.resizable(False,False)

def save_file():
    open_file=filedialog.asksaveasfile(mode='w',defaultextension='.txt')
    if open_file is None:
        return
    Text=str(Entry.get(1.0,END))
    open_file.write(Text)
    open_file.close()

def open_file():
    file=filedialog.askopenfile(mode='r',filetypes=[('text files','.txt')])
    if open_file is not None:
        content=file.read()
    Entry.insert(INSERT,content)


b1=Button(root,width='20',height='2',bg='#fff',text='save_file',command=save_file).place(x=100,y=20)
b2=Button(root,width='20',height='2',bg='#fff',text='open_file',command=open_file).place(x=300,y=20)

Entry=Text(root,height='72',width='70',wrap=WORD)
Entry.place(x=10,y=70)
root.mainloop()
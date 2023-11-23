from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Text Editor')
root.geometry('1000x600')
root.resizable(False, False)
root.configure(bg='#313031')

def conf():
    tart = confirm.get()
    text.config(state=NORMAL)
    text.insert(tart)

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(
    label='Fájl',
    menu=file_menu
)

file_menu.add_command(
    label='Megnyitás'
)

file_menu.add_command(
    label='Mentés'
)

file_menu.add_command(
    label='Kilépés',
    command=root.destroy
)


text = Text(root, wrap=WORD, height=20, width=83, font=('Arial', 16), state=DISABLED)
text.pack()

entry = Entry(root, font=('Arial', 16))
entry.pack(pady=20)

confirm = Button(root, text='Oké', font=('Arial', 16), command=conf)
confirm.pack()



root.mainloop()
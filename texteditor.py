from tkinter import *

root = Tk()
root.title('Text Editor')
root.geometry('1000x600')

root.configure(bg='#313031')

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


sbar = Scrollbar(root, orient='vertical')
sbar.pack(side=RIGHT, fill='y')

text = Text(root, wrap=WORD, height=100, width=110, yscrollcommand=sbar.set)
sbar.config(command=text.yview)
text.pack()





root.mainloop()
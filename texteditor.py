from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox
from tkinter import colorchooser

root = Tk()
root.title('Notepad++++')
root.geometry('1000x700')
root.resizable(False, False)
root.configure(bg='#313031')

def conf(event):
    text_content = entry.get()
    text.config(state=NORMAL)
    text.insert(END, f'{text_content} ')
    text.config(state=DISABLED)
    entry.delete(0, END)

def linebreak():
    text_content = entry.get()
    text.config(state=NORMAL)
    text.insert(END, f'\n{text_content}')
    text.config(state=DISABLED)
    entry.delete(0, END)

def select_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='File megynyitása',
        initialdir='/',
        filetypes=filetypes)

    messagebox.showinfo(
        title='Kiválasztott file',
        message=filename
    )

    with open(filename, "r") as f:
        file_content = f.read()
        text.config(state=NORMAL)
        text.delete('1.0', END)
        text.insert(END, file_content)
        text.config(state=DISABLED)

def save_file():
    filetypes = (
        ('text files', '*.txt'),
        ('All files', '*.*')
    )

    filename = fd.asksaveasfilename(
        title='File mentése',
        initialdir='/',
        filetypes=filetypes)

    messagebox.showinfo(
        title='Mentett file neve',
        message=filename
    )

    with open(filename, "w") as f:
        f.write(text.get("1.0", END))

def quit_app():
    response = messagebox.askyesno('Kilépés', 'Biztos ki akarsz lépni?')
    if response:
        root.destroy()

def bold_text():
    try:
        current_tags = text.tag_names("sel.first")
        if "bold" in current_tags:
            text.tag_remove("bold", "sel.first", "sel.last")
        else:
            text.tag_add("bold", "sel.first", "sel.last")
            text.tag_configure("bold", font=('Arial', 16, 'bold'))
    except TclError:
        messagebox.showwarning('Error', 'Nem jelöltél ki semmit!')

def italic_text():
    try:
        current_tags = text.tag_names("sel.first")
        if "italic" in current_tags:
            text.tag_remove("italic", "sel.first", "sel.last")
        else:
            text.tag_add("italic", "sel.first", "sel.last")
            text.tag_configure("italic", font=('Arial', 16, 'italic'))
    except TclError:
        messagebox.showwarning('Error', 'Nem jelöltél ki semmit!')

def underline_text():
    try:
        current_tags = text.tag_names("sel.first")
        if "underline" in current_tags:
            text.tag_remove("underline", "sel.first", "sel.last")
        else:
            text.tag_add("underline", "sel.first", "sel.last")
            text.tag_configure("underline", underline=True)
    except TclError:
        messagebox.showwarning('Error', 'Nem jelöltél ki semmit!')

def choose_color():
    try:
        color_code = colorchooser.askcolor()[1]
        text.tag_add("color", "sel.first", "sel.last")
        text.tag_configure("color", foreground=color_code)
    except TclError:
        messagebox.showwarning('Error', 'Nem jelöltél ki semmit!')

menubar = Menu(root)
root.config(menu=menubar)
file_menu = Menu(menubar, tearoff=False)
menubar.add_cascade(label='Fájl', menu=file_menu)

file_menu.add_command(label='Megnyitás', command=select_file)
file_menu.add_command(label='Mentés', command=save_file)
file_menu.add_command(label='Kilépés', command=quit_app)

title = Label(root, text='Notepad++++', font=('Arial', 24, 'bold'), bg='#313031', fg='#D3D3D3')
title.pack()

format_frame = Frame(root, bg='#313031')
format_frame.pack(pady=10)

boldimg = PhotoImage(file='./bold.png')
bold_button = Button(format_frame, image=boldimg, command=bold_text, font=('Arial', 12, 'bold'), bg='#D3D3D3')
bold_button.grid(row=0, column=0, padx=5)

italicimg = PhotoImage(file='./italic.png')
italic_button = Button(format_frame, image=italicimg, command=italic_text, font=('Arial', 12, 'italic'), bg='#D3D3D3')
italic_button.grid(row=0, column=1, padx=5)

underlineimg = PhotoImage(file='./underline.png')
underline_button = Button(format_frame, image=underlineimg, command=underline_text, font=('Arial', 12, 'underline'), bg='#D3D3D3')
underline_button.grid(row=0, column=2, padx=5)

colorimg = PhotoImage(file='./color-text.png')
color_button = Button(format_frame, image=colorimg, command=choose_color, font=('Arial', 12), bg='#D3D3D3')
color_button.grid(row=0, column=3, padx=5)

text = Text(root, wrap=WORD, height=20, width=83, font=('Arial', 16), state=DISABLED, bg='#D3D3D3')
text.pack()

entry = Entry(root, font=('Arial', 16), bg='#D3D3D3')
entry.bind('<Return>', conf)
entry.pack(pady=20)

confirm = Button(root, text='Enter', font=('Arial', 16), command=linebreak, bg='#D3D3D3')
confirm.pack()



root.mainloop()

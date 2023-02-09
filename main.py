from tkinter import *
from tkinter import messagebox
from tkinter import filedialog


def second():
    Sec = Toplevel()
    Sec.title('Another Me')
    Sec.geometry('250x100')


def radio():
    Radio_Buttons = Toplevel()
    Radio_Buttons.title('Radio Buttons')
    Radio_Buttons.geometry('110x250')
    r = IntVar()
    r.set(2)
    Value = Label(Radio_Buttons, text=r.get(), anchor=W)
    Value.grid(row=3, column=0)

    def clicked():
        Value.config(text=r.get())

    Radiobutton(Radio_Buttons, text='Cheese', variable=r, value=1, command=clicked).grid(row=0, column=0, sticky=W)
    Radiobutton(Radio_Buttons, text='Pasta', variable=r, value=2, command=clicked).grid(row=1, column=0, sticky=W)

    Val = [
        (1, 'Me', 'Don'),
        (2, 'You', 'Boo'),
        (3, 'Other You', 'what uuupppp!!!!'),
        (4, 'Onion', 'Onion')
    ]

    yourval = StringVar()
    yourval.set('Don')
    YourValue = Label(Radio_Buttons, text=yourval.get(), anchor=CENTER)
    YourValue.grid(row=8, column=0, padx=5)

    def clicked2():
        YourValue.config(text=yourval.get())

    for row, text, value in Val:
        Radiobutton(Radio_Buttons, text=text, variable=yourval, value=value, command=clicked2, anchor=E).grid(
            row=row + 3, column=0, sticky=W)


def Frames():
    frames = Toplevel()
    frames.title('Frames')
    frames.geometry('250x250')
    frame1 = LabelFrame(frames, text="frame1", padx=5, pady=5)
    frame1.grid(row=0, column=0, padx=6, pady=6)
    Hello = Label(frame1, text='Hello')
    Hello.pack()

    def set():
        frame2 = LabelFrame(frames, text="frame2", padx=3, pady=3)
        frame2.grid(row=0, column=2, padx=6, pady=6)
        Helloagain = Label(frame2)
        Helloagain.pack()
        Helloagain.config(text="Hello Again")

    B = Button(frame1, text='Hello', command=set)
    B.pack()


def Message():
    Messages = Toplevel()
    Messages.title('Messages')
    Messages.geometry('270x270')

    def popup():
        messagebox.showinfo('Popup', 'Hello World')

    popup = Button(Messages, text='Popup', command=popup).pack()
    showerror = Button(Messages, text='Show Error', command=lambda: messagebox.showerror('Error', 'You')).pack()
    WarningMessage = Button(Messages, text='Warning Message',
                            command=lambda: messagebox.showwarning('Warning', '11 Calls from Home')).pack()
    askokcancle = Button(Messages, text='AskOkCancel',
                         command=lambda: messagebox.askokcancel('askokcancel', "How you doin'")).pack()
    askquestion = Button(Messages, text='Ask Question',
                         command=lambda: messagebox.askquestion('Ask Question', "How you doin'")).pack()
    askretrycancel = Button(Messages, text='Ask Retry Cancel',
                            command=lambda: messagebox.askretrycancel('Ask Retry Cancel',
                                                                      "What's better than giving up?")).pack()
    askyesno = Button(Messages, text='Ask Yes No',
                      command=lambda: messagebox.askyesno('Ask Yes No', "Wanna break from the ads?")).pack()
    askyesnocancel = Button(Messages, text='Ask Yes No Cancel',
                            command=lambda: messagebox.askyesnocancel('Ask Yes No Cancel', "Want a cookie?")).pack()


def OpenFile():
    Open_File = Toplevel()

    def browse():
        filename = filedialog.askopenfilename(initialdir='/', title='Select File', filetypes=(
            ('All Files', '*.*'), ('PNG Files', '*.png'), ('JPG Files', '*.jpg')))
        path = Label(Open_File, text=filename)
        path.pack()

    Browse = Button(Open_File, text='Browse', command=browse).pack()


def Sliders():
    Sliders = Toplevel()
    Sliders.title('Sliders')
    Sliders.geometry('200x200')

    def slide(a):
        if a != 0:
            Sliders.geometry(str(Horizontal.get()) + 'x' + str(Verticle.get()))

    Verticle = Scale(Sliders, from_=200, to=400, command=slide)
    Verticle.grid(row=0, column=2)
    Horizontal = Scale(Sliders, from_=200, to=400, orient=HORIZONTAL, command=slide)
    Horizontal.grid(row=2, column=0)


def Check():
    Check = Toplevel()
    Check.title('Check Box')
    Check.geometry('200x200')
    var = StringVar()

    def translate():
        l.config(text=var.get())

    a = Checkbutton(Check, text='Thank You', variable=var, onvalue='Arigato', command=translate)
    a.deselect()
    a.pack()
    b = Checkbutton(Check, text='Welcome', variable=var, onvalue='Irasshaimase', command=translate)
    b.deselect()
    b.pack()
    l = Label(Check)
    l.pack()


def Dropdown():
    Drop_down = Toplevel()
    Drop_down.title('Drop Down')
    Drop_down.geometry('200x200')
    Options = [
        'Dragalge',
        'Drowzee',
        'Krookodile',
        'Dewgong',
        'Mankey',
        'Shellos'
    ]
    option = StringVar()
    option.set('Shellos')
    def show(n):
        if n != '':
            lb.config(text='You choose '+option.get()+'!!')
    d = OptionMenu(Drop_down, option, *Options, command=show)
    d.pack()
    lb = Label(Drop_down)
    lb.pack()


if __name__ == '__main__':
    root = Tk()
    root.title('Me')
    root.geometry('200x290')
    Open = Button(root, text='Aonther Me', command=second).pack()
    Radio = Button(root, text='Radio Buttons', command=radio).pack()
    Frame = Button(root, text='Frames', command=Frames).pack()
    Message = Button(root, text='Messages', command=Message).pack()
    Openfile = Button(root, text='Open File', command=OpenFile).pack()
    Sliders = Button(root, text='Sliders', command=Sliders).pack()
    CheckBox = Button(root, text='Check Box', command=Check).pack()
    Dropdown = Button(root, text='Drop Down', command=Dropdown).pack()
    Close = Button(root, text='Let me Sleep!!', command=root.destroy).pack()
    mainloop()

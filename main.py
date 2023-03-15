# "Тренажер Блок-схем алгоритмов"
from tkinter import *

root = Tk()
root.title("Тренажер блок-схем алгоритмов")
root.geometry("600x400")
root.config(bg="white")


def level1():

    def clic1():
        answer1 = e1.get()
        if answer1 == "10":
            e1.config(bg="lightgreen")
            e1.delete(0, END)
            e1.insert(0, 'Правильно!')
            btn1.config(text='Выполнено')
        else:
            e1.config(bg="orange red")
            e1.delete(0, END)
            e1.insert(0, 'Неправильно!')
    root.withdraw()
    l1 = Tk()
    l1.config(bg="white")
    l1.geometry("1980x1080")
    l1.image = PhotoImage(file='Уровень 1.png', master=l1)
    l1.title("Уровень 1")
    bg_logo1 = Label(l1, image=l1.image)
    lall1 = Button(l1, text="< Назад", command=lambda: open_level(l1))
    lall1.pack(padx=120, pady=30)
    e1 = Entry(l1)
    e1.pack()
    entry1 = Button(l1, text="Ответить", command=clic1, compound=BOTTOM)
    entry1.pack()
    bg_logo1.pack()
    l1.mainloop()


def level2():
    def clic2():
        answer2 = e2.get()
        if answer2 == "7":
            e2.config(bg="lightgreen")
            e2.delete(0, END)
            e2.insert(0, 'Правильно!')
            btn2.config(text='Выполнено')
        else:
            e2.config(bg="orange red")
            e2.delete(0, END)
            e2.insert(0, 'Неправильно!')
    root.withdraw()
    l2 = Tk()
    l2.config(bg="white")
    l2.title("Уровень 1")
    l2.geometry("1980x1080")
    l2.image = PhotoImage(file='Уровень 2.png', master=l2)
    lall2 = Button(l2, text="< Назад", command=lambda: open_level(l2))
    bg_logo2 = Label(l2, image=l2.image)
    lall2.pack(padx=120, pady=30)
    e2 = Entry(l2)
    e2.pack()
    entry2 = Button(l2, text="Ответить", command=clic2, compound=BOTTOM)
    entry2.pack()
    bg_logo2.pack()
    l2.mainloop()


def level3():
    def clic3():
        answer3 = e3.get()
        if answer3 == "8":
            e3.config(bg="lightgreen")
            e3.delete(0, END)
            e3.insert(0, 'Правильно!')
            btn3.config(text='Выполнено')
        else:
            e3.config(bg="orange red")
            e3.delete(0, END)
            e3.insert(0, 'Неправильно!')
    root.withdraw()
    l3 = Tk()
    l3.config(bg="white")
    l3.title("Уровень 2")
    l3.geometry("1980x1080")
    l3.image = PhotoImage(file='Уровень 3.png', master=l3)
    lall3 = Button(l3, command=lambda: open_level(l3))
    lall3.config(text="< Назад")
    bg_logo3 = Label(l3, image=l3.image)
    lall3.pack(padx=120, pady=30)
    e3 = Entry(l3)
    e3.pack()
    entry3 = Button(l3, text="Ответить", command=clic3, compound=BOTTOM)
    entry3.pack()
    bg_logo3.pack()
    l3.mainloop()


def level4():
    def clic4():
        answer4 = e4.get()
        if answer4 == "5":
            e4.config(bg="lightgreen")
            e4.delete(0, END)
            e4.insert(0, 'Правильно!')
            btn4.config(text='Выполнено')
        else:
            e4.config(bg="orange red")
            e4.delete(0, END)
            e4.insert(0, 'Неправильно!')
    root.withdraw()
    l4 = Tk()
    l4.config(bg="white")
    l4.title("Уровень 3")
    l4.geometry("1980x1080")
    l4.image = PhotoImage(file='Уровень 4.png', master=l4)
    lall4 = Button(l4, command=lambda: open_level(l4))
    lall4.config(text="< Назад")
    bg_logo4 = Label(l4, image=l4.image)
    lall4.pack(padx=120, pady=30)
    e4 = Entry(l4)
    e4.pack()
    entry4 = Button(l4, text="Ответить", command=clic4, compound=BOTTOM)
    entry4.pack()
    bg_logo4.pack()
    l4.mainloop()


def level5():
    def clic5():
        answer5 = e5.get()
        if answer5 == "30":
            e5.config(bg="lightgreen")
            e5.delete(0, END)
            e5.insert(0, 'Правильно!')
            btn5.config(text='Выполнено')
        else:
            e5.config(bg="orange red")
            e5.delete(0, END)
            e5.insert(0, 'Неправильно!')
    root.withdraw()
    l5 = Tk()
    l5.config(bg="white")
    l5.title("Уровень 1")
    l5.geometry("1980x1080")
    l5.image = PhotoImage(file='Уровень 5.png', master=l5)
    lall5 = Button(l5, command=lambda: open_level(l5))
    lall5.config(text="< Назад")
    bg_logo5 = Label(l5, image=l5.image)
    lall5.pack(padx=120, pady=30)
    e5 = Entry(l5)
    e5.pack()
    entry5 = Button(l5, text="Ответить", command=clic5, compound=BOTTOM)
    entry5.pack()
    bg_logo5.pack()
    l5.mainloop()


def level6():
    def clic6():
        answer6 = e6.get()
        if answer6 == "3":
            e6.config(bg="lightgreen")
            e6.delete(0, END)
            e6.insert(0, 'Правильно!')
            btn6.config(text='Выполнено')
        else:
            e6.config(bg="orange red")
            e6.delete(0, END)
            e6.insert(0, 'Неправильно!')
    root.withdraw()
    l6 = Tk()
    l6.title("Уровень 2")
    l6.geometry("1980x1080")
    l6.config(bg="white")
    l6.image = PhotoImage(file='Уровень 6.png', master=l6)
    lall6 = Button(l6, command=lambda: open_level(l6))
    lall6.config(text="< Назад")
    bg_logo6 = Label(l6, image=l6.image)
    lall6.pack(padx=120, pady=30)
    e6 = Entry(l6)
    e6.pack()
    entry6 = Button(l6, text="Ответить", command=clic6, compound=BOTTOM)
    entry6.pack()
    bg_logo6.pack()
    l6.mainloop()


def level7():
    def clic7():
        answer7 = e7.get()
        if answer7 == "6":
            e7.config(bg="lightgreen")
            e7.delete(0, END)
            e7.insert(0, 'Правильно!')
            btn7.config(text='Выполнено')
        else:
            e7.config(bg="orange red")
            e7.delete(0, END)
            e7.insert(0, 'Неправильно!')

    root.withdraw()
    l7 = Tk()
    l7.title("Уровень 4")
    l7.geometry("1980x1080")
    l7.config(bg="white")
    l7.image = PhotoImage(file='уровень 7.png', master=l7)
    lall7 = Button(l7, command=lambda: open_level(l7))
    lall7.config(text="< Назад")
    bg_logo7 = Label(l7, image=l7.image)
    lall7.pack(padx=120, pady=30)
    e7 = Entry(l7)
    e7.pack()
    entry7 = Button(l7, text="Ответить", command=clic7, compound=BOTTOM)
    entry7.pack()
    bg_logo7.pack()
    l7.mainloop()


def level8():
    def clic8():
        answer8 = e8.get()
        if answer8 == "7":
            e8.config(bg="lightgreen")
            e8.delete(0, END)
            e8.insert(0, 'Правильно!')
            btn9.config(text='Выполнено')
        else:
            e8.config(bg="orange red")
            e8.delete(0, END)
            e8.insert(0, 'Неправильно!')

    root.withdraw()
    l8 = Tk()
    l8.title("Уровень 3")
    l8.geometry("1980x1080")
    l8.config(bg="white")
    l8.image = PhotoImage(file='Уровень 8.png', master=l8)
    lall8 = Button(l8, command=lambda: open_level(l8))
    lall8.config(text="< Назад")
    bg_logo8 = Label(l8, image=l8.image)
    lall8.pack(padx=120, pady=30)
    e8 = Entry(l8)
    e8.pack()
    entry8 = Button(l8, text="Ответить", command=clic8, compound=RIGHT)
    entry8.pack()
    bg_logo8.pack()
    l8.mainloop()


def level9():
    def clic9():
        answer9 = e9.get()
        if answer9 == "-72":
            e9.config(bg="lightgreen")
            e9.delete(0, END)
            e9.insert(0, 'Правильно!')
            btn9.config(text='Выполнено')
        else:
            e9.config(bg="orange red")
            e9.delete(0, END)
            e9.insert(0, 'Неправильно!')

    root.withdraw()
    l9 = Tk()
    l9.title("Уровень 2")
    l9.geometry("1980x1080")
    l9.config(bg="white")
    l9.image = PhotoImage(file='Уровень 9.png', master=l9)
    lall9 = Button(l9, command=lambda: open_level(l9))
    lall9.config(text="< Назад")
    bg_logo9 = Label(l9, image=l9.image)
    lall9.pack(padx=120, pady=30)
    e9 = Entry(l9)
    e9.pack()
    entry9 = Button(l9, text="Ответить", command=clic9, compound=BOTTOM)
    entry9.pack()
    bg_logo9.pack()
    l9.mainloop()


def level10():
    def clic10():
        answer10 = e10.get()
        if answer10 == "30":
            e10.config(bg="lightgreen")
            e10.delete(0, END)
            e10.insert(0, 'Правильно!')
            btn10.config(text='Выполнено')
        else:
            e10.config(bg="orange red")
            e10.delete(0, END)
            e10.insert(0, 'Неправильно!')
    root.withdraw()
    l10 = Tk()
    l10.title("Уровень 3")
    l10.geometry("1980x1080")
    l10.config(bg="white")
    l10.image = PhotoImage(file='Уровень 10.png', master=l10)
    lall10 = Button(l10, command=lambda: open_level(l10))
    lall10.config(text="< Назад")
    bg_logo10 = Label(l10, image=l10.image)
    lall10.pack(padx=120, pady=30)
    e10 = Entry(l10)
    e10.pack()
    entry10 = Button(l10, text="Ответить", command=clic10, compound=BOTTOM)
    entry10.pack()
    bg_logo10.pack()
    l10.mainloop()


def level11():

    root.withdraw()
    l11 = Tk()
    l11.title("Обучение")
    l11.geometry("1980x1080")
    l11.config(bg="white")
    l11.image = PhotoImage(file='Обучение.png', master=l11)
    lall10 = Button(l11, command=lambda: open_level(l11))
    lall10.config(text="< Назад")
    bg_logo10 = Label(l11, image=l11.image)
    lall10.pack(padx=120, pady=30)
    bg_logo10.pack()
    l11.mainloop()


def open_level(level_window):
    level_window.withdraw()
    root.deiconify()


study = Button(root, font='Trebuchet', text="Обучение", borderwidth=0, bg="medium aquamarine")
study.config(command=level11, height=1, width=40)
study.place(x=112, y=50)


btn1 = Button(root, font='Trebuchet', text="Уровень 1", borderwidth=0, bg="yellow")
btn1.config(command=level1, height=1, width=9)
btn1.place(x=250, y=100)

btn2 = Button(root, font='Trebuchet', text="Уровень 1", borderwidth=0, bg="lightgreen")
btn2.config(command=level2, height=1, width=9)
btn2.place(x=100, y=100)

btn3 = Button(root, font='Trebuchet', text="Уровень 2", borderwidth=0, bg="lightgreen")
btn3.config(command=level3, height=1, width=9)
btn3.place(x=100, y=150)

btn4 = Button(root, font='Trebuchet', text="Уровень 3", borderwidth=0, bg="lightgreen")
btn4.config(command=level4, height=1, width=9)
btn4.place(x=100, y=200)

btn5 = Button(root, font='Trebuchet', text="Уровень 1", borderwidth=0, bg="lightblue")
btn5.config(command=level5, height=1, width=9)
btn5.place(x=400, y=100)

btn6 = Button(root, font='Trebuchet', text="Уровень 2", borderwidth=0, bg="yellow")
btn6.config(command=level6, height=1, width=9)
btn6.place(x=250, y=150)

btn7 = Button(root, font='Trebuchet', text="Дополнительное задание", borderwidth=0, bg="PeachPuff2")
btn7.config(command=level7, height=1, width=40)
btn7.place(x=112, y=250)

btn8 = Button(root, font='Trebuchet', text="Уровень 3", borderwidth=0, bg="yellow")
btn8.config(command=level8, height=1, width=9)
btn8.place(x=250, y=200)

btn9 = Button(root, font='Trebuchet', text="Уровень 2", borderwidth=0, bg="lightblue")
btn9.config(command=level9, height=1, width=9)
btn9.place(x=400, y=150)

btn10 = Button(root, font='Trebuchet', text="Уровень 3", borderwidth=0, bg="lightblue")
btn10.config(command=level10, height=1, width=9)
btn10.place(x=400, y=200)


root.mainloop()

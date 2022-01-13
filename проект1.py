from tkinter import *
from tkinter import messagebox, Label
from random import randint
import sys
import os
import subprocess
def restart():
    subprocess.Popen([sys.executable, 'проект1.py'])
    root.withdraw()
def is_digit(n):
    try:
        int(n)
        return True
    except ValueError:
        return False
n=0
def clickbtn():
    global a
    global b
    global w1
    global n
    global c
    x = w1.get()
    c = b - a
    if is_digit(x):
        x = float(w1.get())
        if c==x and n==0:
            message = "Правильный ответ"
            messagebox.showinfo("Результат", message)
            root.destroy()
            import проект2
        if c==x and n!=0:
            message = "Правильный ответ, попробуйте еще отработать это задание"
            messagebox.showinfo("Результат", message)
            f = open("counter.txt", "a")
            for i in range(n):
                f.write("1")
            f.close()
            restart()
        if c!=x:
            message = "Неправильный ответ,попробуйте еще раз"
            messagebox.showinfo("Результат", message)
            n = n + 1
            print(n)
    else:
        messagebox.showinfo('Ошибка', 'Введите числовые значения')


root = Tk()
root.title("Задание 1")
root.geometry('1600x800')
root.resizable(width= False, height=False)

frame = Frame(root, bg='white')
frame.place(relwidth=1,relheight=1)

b = randint(1,100)
a = randint(1,b)

x1 = Label(frame, text = "x", bg='white',font="Arial 150")
x1.place(x=350,y=80,width=120, height=150)

plus = Label(frame, text = '+', bg='white',font="Arial 150")
plus.place(x=500,y=100, width=120, height=150)

a1 = Label(frame, text = a, bg='white',font="Arial 120")
a1.place(x=625,y=90, width=170, height=150)

eq = Label(frame, text = '=', bg='white',font="Arial 150")
eq.place(x=825,y=100, width=120, height=150)

b1 = Label(frame, text = b, bg='white',font="Arial 120")
b1.place(x=1000,y=100, width=170, height=150)

x1 = Label(frame, text = "x", bg='white',font="Arial 150")
x1.place(x=520,y=330,width=120, height=150)

eq = Label(frame, text = '=', bg='white',font="Arial 150")
eq.place(x=700,y=350, width=120, height=150)

w1 = Entry(frame, bg = 'grey',font="Arial 80")
w1.place(x=900,y=330, width=120, height=120)

btn= Button(frame, text = 'Проверить',font="Arial 80", bg='green', command = clickbtn)
btn.place(x=450,y=600,width=600, height=120)


print(b-a)
print(n)
root.mainloop()

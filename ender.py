from tkinter import *
from tkinter import messagebox, Label
def clickbtn():
    message = "Спасибо, что прошел тест. Проходи его еще, чтобы совершенствоваться."
    messagebox.showinfo("Спасибо", message)
    root.destroy()

root = Tk()
root.title("Результаты")
root.geometry('1600x800')
root.resizable(width= False, height=False)
frame = Frame(root, bg='white')
frame.place(relwidth=1,relheight=1)

f = open("name.txt")
name = f.read()
f.close()

g = open("counter.txt", "r")
m = len(g.read())
g.close()

t1 = Label(frame, text = "Ваш результат", bg='white',font="Arial 110")
t1.place(x=60,y=0,width=1600, height=150)

t2 = Label(frame, text = name, bg='white',font="Arial 90")
t2.place(x=50,y=200,width=1600, height=150)

t3 = Label(frame, text = "Количество ошибок :", bg='white',font="Arial 80")
t3.place(x=50,y=400,width=1600, height=150)

t4 = Label(frame, text = m, bg='white',font="Arial 80")
t4.place(x=1400,y=400,width=50, height=150)

btn= Button(frame, text = 'Закончить',font="Arial 80", bg='green', command = clickbtn)
btn.place(x=550,y=600,width=600, height=120)

root.mainloop()
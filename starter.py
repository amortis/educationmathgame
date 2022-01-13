from tkinter import *
def clickbtn():
    a = w1.get()
    file = open("name.txt", "w")
    file.write(a)
    file.close()
    root.destroy()
    import проект1
root = Tk()
root.title("Обучающие приложение")
root.geometry('1600x800')
root.resizable(width= False, height=False)
frame = Frame(root, bg='white')
frame.place(relwidth=1,relheight=1)

text = Label(frame, text = "Введите ваше имя", bg='white',font="Arial 130")
text.place(x=10,y=80,width=1600, height=500)

w1 = Entry(frame, bg = 'grey',font="Arial 80")
w1.place(x=300,y=455, width=900, height=120)

btn= Button(frame, text = 'Начать',font="Arial 80", bg='green', command = clickbtn)
btn.place(x=450,y=600,width=600, height=120)
root.mainloop()

counter = open('counter.txt','w')
counter.close()
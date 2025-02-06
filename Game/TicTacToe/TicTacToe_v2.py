from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("500x500")

Grid.rowconfigure(window, 0, weight=1)
Grid.rowconfigure(window, 1, weight=1)
Grid.rowconfigure(window, 2, weight=1)
Grid.columnconfigure(window, 0, weight=1)
Grid.columnconfigure(window, 1, weight=1)
Grid.columnconfigure(window, 2, weight=1)

gracz1 = True

def stop():
    btn1.config(state=DISABLED)
    btn2.config(state=DISABLED)
    btn3.config(state=DISABLED)
    btn4.config(state=DISABLED)
    btn5.config(state=DISABLED)
    btn6.config(state=DISABLED)
    btn7.config(state=DISABLED)
    btn8.config(state=DISABLED)
    btn9.config(state=DISABLED)

def wygrana():
    global gracz1
# wiersze
    if btn1["text"] != " " and  btn1["text"] == btn2["text"] and btn1["text"] == btn3["text"]:
        btn1.config(bg="green")
        btn2.config(bg="green")
        btn3.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
    if btn4["text"] != " " and  btn4["text"] == btn5["text"] and btn4["text"] == btn6["text"]:
        btn4.config(bg="green")
        btn5.config(bg="green")
        btn6.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
    if btn7["text"] != " " and  btn7["text"] == btn8["text"] and btn7["text"] == btn9["text"]:
        btn7.config(bg="green")
        btn8.config(bg="green")
        btn9.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
# kolumny
    if btn1["text"] != " " and  btn1["text"] == btn4["text"] and btn1["text"] == btn7["text"]:
        btn1.config(bg="green")
        btn4.config(bg="green")
        btn7.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
    if btn2["text"] != " " and  btn2["text"] == btn5["text"] and btn2["text"] == btn8["text"]:
        btn2.config(bg="green")
        btn5.config(bg="green")
        btn8.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
    if btn3["text"] != " " and  btn3["text"] == btn6["text"] and btn3["text"] == btn9["text"]:
        btn3.config(bg="green")
        btn6.config(bg="green")
        btn9.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
# skos
    if btn1["text"] != " " and  btn1["text"] == btn5["text"] and btn1["text"] == btn9["text"]:
        btn1.config(bg="green")
        btn5.config(bg="green")
        btn9.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")
    if btn3["text"] != " " and  btn3["text"] == btn5["text"] and btn3["text"] == btn7["text"]:
        btn3.config(bg="green")
        btn5.config(bg="green")
        btn7.config(bg="green")
        stop()
        if gracz1 == True:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz O")
        else:
            messagebox.showinfo("Zwycięzcą jest ... ", " Gracz X")


def tick(btn):
    global gracz1
    if btn["text"] == " " and gracz1 == True:
        btn["text"] = "X"
        gracz1 = False
        wygrana()

    elif btn["text"] == " " and gracz1 == False:
        btn["text"] = "O"
        gracz1 = True
        wygrana()

btn1 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn1))
btn1.grid(row=0, column=0, sticky="news")
btn2 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn2))
btn2.grid(row=0, column=1, sticky="news")
btn3 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn3))
btn3.grid(row=0, column=2, sticky="news")

btn4 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn4))
btn4.grid(row=1, column=0, sticky="news")
btn5 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn5))
btn5.grid(row=1, column=1, sticky="news")
btn6 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn6))
btn6.grid(row=1, column=2, sticky="news")

btn7 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn7))
btn7.grid(row=2, column=0, sticky="news")
btn8 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn8))
btn8.grid(row=2, column=1, sticky="news")
btn9 = Button(window, text=" ", bg="light blue", font="Arial 30 bold", command=lambda: tick(btn9))
btn9.grid(row=2, column=2, sticky="news")

window.mainloop()

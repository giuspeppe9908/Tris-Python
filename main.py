import tkinter as tk
from tkinter import messagebox
list_btn = []
window = tk.Tk()
window.title("Tris Game")
#window.geometry("800x800")
clicked = True
count = 0
def checkWinner():
    global winner
    winner = False
    #in the row
    if btn1["text"] == "X" and btn2["text"] == "X" and btn3["text"] == "X":
        btn1["bg"] = "green"
        btn2["bg"] = "green"
        btn3["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")
    elif btn4["text"] == "X" and btn5["text"] == "X" and btn6["text"] == "X":
        btn4["bg"] = "green"
        btn5["bg"] = "green"
        btn6["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")
    elif btn7["text"] == "X" and btn8["text"] == "X" and btn9["text"] == "X":
        btn7["bg"] = "green"
        btn8["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!","X won!")
    elif btn1["text"] == "X" and btn4["text"] == "X" and btn7["text"] == "X":
        btn1["bg"] = "green"
        btn4["bg"] = "green"
        btn7["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")
    elif btn2["text"] == "X" and btn5["text"] == "X" and btn8["text"] == "X":
        btn2["bg"] = "green"
        btn5["bg"] = "green"
        btn8["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")
    elif btn3["text"] == "X" and btn6["text"] == "X" and btn9["text"] == "X":
        btn3["bg"] = "green"
        btn6["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")
    elif btn1["text"] == "X" and btn5["text"] == "X" and btn9["text"] == "X":
        btn1["bg"] = "green"
        btn5["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")
    elif btn3["text"] == "X" and btn5["text"] == "X" and btn7["text"] == "X":
        btn3["bg"] = "green"
        btn5["bg"] = "green"
        btn7["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "X won!")

    #Checking O's wins
    elif btn1["text"] == "O" and btn2["text"] == "O" and btn3["text"] == "O":
        btn1["bg"] = "green"
        btn2["bg"] = "green"
        btn3["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    elif btn4["text"] == "O" and btn5["text"] == "O" and btn6["text"] == "O":
        btn4["bg"] = "green"
        btn5["bg"] = "green"
        btn6["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    elif btn7["text"] == "O" and btn8["text"] == "O" and btn9["text"] == "O":
        btn7["bg"] = "green"
        btn8["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    #diagonals
    elif btn1["text"] == "O" and btn5["text"] == "O" and btn9["text"] == "O":
        btn1["bg"] = "green"
        btn5["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    elif btn3["text"] == "O" and btn5["text"] == "O" and btn7["text"] == "O":
        btn3["bg"] = "green"
        btn5["bg"] = "green"
        btn7["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    #coloumns
    elif btn1["text"] == "O" and btn4["text"] == "O" and btn7["text"] == "O":
        btn1["bg"] = "green"
        btn4["bg"] = "green"
        btn7["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    elif btn2["text"] == "O" and btn5["text"] == "O" and btn8["text"] == "O":
        btn2["bg"] = "green"
        btn5["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    elif btn3["text"] == "O" and btn6["text"] == "O" and btn9["text"] == "O":
        btn3["bg"] = "green"
        btn6["bg"] = "green"
        btn9["bg"] = "green"
        winner = True
        messagebox.showinfo("We have a Winner!", "O won!")
    if count == 9 and winner == False:
        messagebox.showinfo("Tris Game","Pair Game!")

def XorY(btn):
    global clicked, count
    if btn["text"] == "" and clicked == True:
        btn["text"] = "X"
        clicked = False
        count += 1
        checkWinner()
    elif btn["text"] == "" and clicked == False:
            btn["text"] = "O"
            clicked = True
            count += 1
            checkWinner()
    else : messagebox.showerror("Tris Game","Yet clicked! Choose another box!")


def reset():
    global btn1, btn2, btn3, btn4, btn5, btn6, btn7, btn8, btn9
    global clicked, count
    clicked = True
    count = 0
    btn1 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn1))
    btn2 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn2))
    btn3 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn3))
    btn4 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn4))
    btn5 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn5))
    btn6 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn6))
    btn7 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn7))
    btn8 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn8))
    btn9 = tk.Button(window, height=4, width=4, text="", command=lambda : XorY(btn9))
    btn1.grid(column=0, row=0)
    btn2.grid(column=0, row=1)
    btn3.grid(column=0, row=2)
    btn4.grid(column=1, row=0)
    btn5.grid(column=1, row=1)
    btn6.grid(column=1, row=2)
    btn7.grid(column=2, row=0)
    btn8.grid(column=2, row=1)
    btn9.grid(column=2, row=2)

#menu
myMenu = tk.Menu(window)
window.config(menu=myMenu)
options_menu = tk.Menu(myMenu, tearoff=False)
myMenu.add_cascade(label="Options", menu=options_menu)
options_menu.add_command(label="Reset Game", command=reset)
reset()
window.mainloop()
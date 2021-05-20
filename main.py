from tkinter import*
import math
import parser
import tkinter.messagebox

//testmodifygit

root = Tk()
root.title("Karaskiv Pycalc")
root.configure(background = "MediumPurple2")
root.resizable(width = False, height = False)
root.geometry("388x505+0+0")

calc = Frame(root)
calc.grid()

# Color palette
hex1 = "#355C7D"
hex2 = "#725A7A"
hex3 = "#fBA31A"
hex4 = "#C56C86"

txtDisplay = Entry(calc, font = ('arial', 24, 'bold'), bg = "snow2", bd = 20, width = 19, justify = RIGHT)
txtDisplay.grid(row = 0, column = 0, columnspan = 4, pady = 1)
txtDisplay.insert(0, "0")

numberpad = "789456123"
i = 0
btn = []
for j in range (2, 5):
	for k in range (3):
		btn.append(Button(calc, width = 4, height = 2, font = ('arial', 20, 'bold'),fg = "snow", bg = hex1, bd = 4, text = numberpad[i]))
		btn[i].grid(row = j, column = k, pady = 1)

		i += 1

#==========================================================
btnClear = Button(calc, text = "C", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "gray18", bg = "snow3").grid(row = 1, column = 0, pady = 1)

btnAllClear = Button(calc, text = "AC", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "gray18", bg = "snow3").grid(row = 1, column = 1, pady = 1)

btnSq = Button(calc, text = "√", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex2).grid(row = 1, column = 2, pady = 1)

btnAdd = Button(calc, text = "+", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex3).grid(row = 1, column = 3, pady = 1)

btnSub = Button(calc, text = "-", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex3).grid(row = 2, column = 3, pady = 1)

btnMult = Button(calc, text = "×", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex3).grid(row = 3, column = 3, pady = 1)

btnDiv = Button(calc, text = "÷", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex3).grid(row = 4, column = 3, pady = 1)

btnZero = Button(calc, text = "0", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex1).grid(row = 5, column = 0, pady = 1)

btnDot = Button(calc, text = ".", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex2).grid(row = 5, column = 1, pady = 1)

btnPM = Button(calc, text = chr(177), width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = hex2).grid(row = 5, column = 2, pady = 1)

btnEquals = Button(calc, text = "=", width = 4, height = 2, font = ('arial', 20, 'bold'), bd = 4, fg = "snow", bg = "firebrick1").grid(row = 5, column = 3, pady = 1)
#=====================Menu and function====================

def iExit():
	iExit = tkinter.messagebox.askyesno("Karaskiv Pycalc","Confirm if you want to exit")
	if iExit > 0:
		root.destroy()
		return

def Scientific():
	root.resizable(width = False, height = False)
	root.geometry("944x568+0+0")

def Standard():
	root.resizable(width = False, height = False)
	root.geometry("480x568+0+0")

menubar = Menu(calc)

filemenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "File", menu = filemenu)
menubar.configure(background = "lavender blush")
filemenu.add_command(label = "Standard", command = Standard)
filemenu.add_command(label = "Scientific", command = Scientific)
filemenu.add_separator()
filemenu.add_command(label = "Exit", command = iExit)

editmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Edit", menu = editmenu)
editmenu.add_command(label = "Cut")
editmenu.add_command(label = "Copy")
editmenu.add_separator()
editmenu.add_command(label = "Paste")

helpmenu = Menu(menubar, tearoff = 0)
menubar.add_cascade(label = "Help", menu = helpmenu)
helpmenu.add_command(label = "View Help")
helpmenu.add_command(label = "About")

root.configure(menu = menubar)
root.mainloop()

#git commit test, editing from another pc

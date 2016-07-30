import tkinter
from tkinter import messagebox
from tkinter import *
import os

root = tkinter.Tk()

code = ""
inputs = ""
content = ""

def helloCallBack():
	with open("output.txt") as f:
		content = f.readlines()
	messagebox.showinfo( "Hello Python", content)

def createFile():
	code = text.get("1.0",END)
	inputs = inputfield.get("1.0",END)
	with open("out.cpp", "w") as text_file:
		print(code, file=text_file)
	with open("input.txt", "w") as text_file:
		print(inputs, file=text_file)
	open('output.txt', 'w').close()
	
def readFile():
	with open("output.txt") as f:
		content = f.readlines()
	outputfield.delete('1.0', END)
	outputfield.insert(INSERT, content)

def compileRun():
	path = os.getcwd()
	os.chdir(path)
	os.system('g++ out.cpp')
	os.system("a.exe < input.txt > output.txt")

def submitClick():
	createFile();
	compileRun();
	readFile();

inputfield = Text(root,height="15");
inputfield.grid(row=0, column=2,sticky=N+E)

outputfield = Text(root,height="15");
outputfield.grid(row=1,column=2,sticky=S+E)

    
xscrollbar = Scrollbar(root, orient=HORIZONTAL)
xscrollbar.grid(row=4, column=0, sticky=N+S+E+W)

yscrollbar = Scrollbar(root)
yscrollbar.grid(row=0, column=1,rowspan=2, sticky=N+W+S)

text = tkinter.Text(root,
			height = "30",
			bg = "#00FF00",
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)

text.grid(row=0, column=0,rowspan=4,sticky=W+N)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

B = tkinter.Button(root, text ="Hello", command = submitClick)

B.grid(row=5, column=0)

root.mainloop()


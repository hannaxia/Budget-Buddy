from tkinter import *
from time import *
from PIL import Image, ImageTk
from random import *

root = Tk()
root.geometry("270x480")
root.title('BudgetBuddy')
s = Canvas(root, width = 270, height = 480, bg='#ffffff')
s.pack(fill = BOTH, expand=False)

n=0
goal = 0
date = []
reason = []
expenses = []
income = 0

bg = ImageTk.PhotoImage(file = 'bg.png')

def home():
	global startBtn
	s.create_image(0, -40, image = (bg), anchor = NW)
	startBtn = Button(root, text = "Start", command = goalset, bg="#80C915", font="Arial 10", anchor = CENTER)
	startBtn.pack()
	startBtn.place(x=135, y=300,height=21,width=150,anchor=CENTER)
	
	s.update()

def goalset():
	global startBtn, enterBtn, answer, incomeEntry, incomeEntryWindow, enterIncome
	startBtn.destroy()
	s.delete('all')
	s.create_text(135, 130, text = ('Set your Bi-weekly income:'), anchor=CENTER, fill = "black", font = "arial 13")
	incomeEntry = Entry(root, font=("Helvetica", 7), width=30, fg="#000000", borderwidth=0)
	incomeEntryWindow = s.create_window(43, 160, anchor="nw", window=incomeEntry)

	s.create_text(135, 210, text = ('Enter your saving goal:'), anchor=CENTER, fill = "black", font = "arial 13")
	answer = Entry(root, font=("Helvetica", 7), width=30, fg="#000000", borderwidth=0)
	answerWindow = s.create_window(43, 240, anchor="nw", window=answer)
	enterBtn=Button(root,text="                   SUBMIT", command = setgoal, bg="#80C915", font="Helvetica 7", anchor = NW)
	enterBtn.pack()
	enterBtn.place(x=135, y=300, height = 21, width = 180, anchor = CENTER)

def setgoal():
	global startBtn, enterBtn, answer, goal, income
	
	income = int(incomeEntry.get())
	
	goal = int(answer.get())
	enterBtn.destroy()
	s.delete('all')
	page2()

def page2():
	global expenses, startBtn, date, reason, expenses
	totalexpenses = 0
	if n == 1:
		global closeBtn
		closeBtn.destroy()
		s.delete('all')
	for i in expenses:
		totalexpenses += int(i)
	
	s.create_text(135, 50, text = ('Goal: $' + str(goal)), anchor=CENTER, fill = "black", font = "arial 20")

	#progress bar
	s.create_rectangle(35,85,35+2*100,110, fill='#fff')
	if (35+2*(100 - (totalexpenses/income*100))) <=0:
		gameover()

	else:
		s.create_rectangle(35,85,(35+2*(100 - (totalexpenses/income*100))),110, fill='#80C915')
		s.create_text(235, 125, text = ('Bi-weekly Income: $'+str(income)), anchor=NE, fill = "black", font = "arial 13")
		s.create_text(235, 155, text = ('Expenses: $'+str(totalexpenses)), anchor=NE, fill = "black", font = "arial 13")
		s.create_rectangle (35+2*(goal/income*100), 85, 35+2*(goal/income*100), 110, fill = 'red')
	
		startBtn = Button(root, text = "Add", command = popup, bg="lightgrey", font="Arial 10", anchor = CENTER)
		startBtn.pack()
		startBtn.place(x=135, y=210, height=21,width=200,anchor=CENTER)
		
		for i in range(len(date)):
			s.create_text(35, 240 + i*50, text = date[i], font = 'arial 14', fill = 'black', anchor = NW)
			s.create_text(35, 260 + i*50, text = reason[i], font = 'arial 14', fill = 'black', anchor = NW)
			s.create_text(245, 240 + i*50, text = expenses[i], font = 'arial 28', anchor = NE, fill = 'black')
			s.create_rectangle(35, 290 + i*50,235, 290 + i*50, fill = 'black')
			doneBtn.destroy()
	
	    
		s.update()
	
	
def popup():
	global startBtn, closeBtn, doneBtn, n, dateEntry, reasonEntry, incomeEntry
	n = 1
	startBtn.destroy()
	s.create_rectangle(20,185,250,185, fill='black')
	s.create_rectangle(20,167,250,372,fill = '#CDED9D')

	s.create_text(40,200, fill = 'black', text = 'Date', font = 'arial 14', anchor = NW)
	dateEntry = Entry(root, font = ("Helvetica", 7), width=20, fg="#000000", borderwidth=0)
	dateEntry_inside = StringVar()
	dateEntry_inside.set("MM/DD/YYYY")
	dateEntryWindow = s.create_window(120,205,anchor=NW, window = dateEntry)
	
	
	s.create_text(40,235, fill = 'black', text = 'Reason', font = 'arial 14', anchor = NW)
	reasonEntry = Entry(root, font = ("Helvetica", 7), width=20, fg="#000000", borderwidth=0)
	reasonEntryWindow = s.create_window(120,240,anchor=NW, window = reasonEntry)

	s.create_text(40, 270, text = ('Amount'), anchor=NW, fill = "black", font = "arial 14")
	incomeEntry = Entry(root, font=("Helvetica", 7), width=20, fg="#000000", borderwidth=0)
	expenseEntryWindow = s.create_window(120, 275, anchor="nw", window=incomeEntry)
	
	
	closeBtn = Button(root, bg = '#CDED9D', text = 'X', command = page2)
	closeBtn.pack()
	closeBtn.place(x=230, y=165, height = 20, width = 20, anchor = NW)

	doneBtn = Button(root, bg = '#fff', text = 'Done', command = expenseAdd)
	doneBtn.pack()
	doneBtn.place(x=135, y=350, height = 20, width = 80, anchor = CENTER)

	
def expenseAdd():
	global closeBtn, doneBtn, dateEntry, reasonEntry, incomeEntry, date, reason, expenses
	closeBtn.destroy()
	doneBtn.destroy()

	date.append(dateEntry.get())
	reason.append(reasonEntry.get())
	expenses.append(incomeEntry.get())
	
	s.delete('all')
	page2()

def gameover():
	global startBtn
	startBtn.destroy()
	s.delete('all')
	s.create_rectangle(0,0,270,480,fill='white')
	s.create_text(135,240,text='You used up all your money...\nStop spending money!',font='arial 12',fill='red')

home()
s.update()
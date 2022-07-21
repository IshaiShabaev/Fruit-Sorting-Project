import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random, time, threading, sys
from threading import Timer 

root = Tk()

global x

global stop_threads
stop_threads = False

global weightValue
weightValue = 'asdfa'

def GetWeight():
	w = random.randrange(0, 1000, 50)
	return w

def IsSensor1(Sensor):
	return not Sensor

def OpenGate(gate):
	if gate == 1:
		print("open gate 1")
	if gate == 2:
		print("open gate 2")
	if gate == 3:
		print("open gate 3")
	if gate == 4:
		print("open gate 4")
	if gate == 5:
		print("open gate 5")
	if gate == 6:
		print("open gate 6")
	if gate == 7:
		print("open gate 7")
	if gate == 8:
		print("open gate 8")
	
	time.sleep(5)


def getIntSafely(val):
	if val != '' and val.isnumeric():
		return int(val)
	else:
		return 0



def initParams():
	################# RESET / START #############################
	gate1= [getIntSafely(getMinGateOne()),getIntSafely(getMaxGateOne())]
	gate2= [getIntSafely(getMinGateTwo()),getIntSafely(getMaxGateTwo())]
	gate3= [getIntSafely(getMinGateTree()),getIntSafely(getMaxGateTree())]
	gate4= [getIntSafely(getMinGateFour()),getIntSafely(getMaxGateFour())]
	gate5= [getIntSafely(getMinGateFive()),getIntSafely(getMaxGateFive())]
	gate6= [getIntSafely(getMinGateSix()),getIntSafely(getMaxGateSix())]
	gate7= [getIntSafely(getMinGateSeven()),getIntSafely(getMaxGateSeven())]
	gate8= [getIntSafely(getMinGateEight()),getIntSafely(getMaxGateEight())]

	gate1Active= getCbVariable1()
	gate2Active= getCbVariable2()
	gate3Active= getCbVariable3()
	gate4Active= getCbVariable4()
	gate5Active= getCbVariable5()
	gate6Active= getCbVariable6()
	gate7Active= getCbVariable7()
	gate8Active= getCbVariable8()

	gate1Delay= getIntSafely(getDelayGateOne())
	gate2Delay= getIntSafely(getDelayGateTwo())
	gate3Delay= getIntSafely(getDelayGateThree())
	gate4Delay= getIntSafely(getDelayGateFour())
	gate5Delay= getIntSafely(getDelayGateFive())
	gate6Delay= getIntSafely(getDelayGateSix())
	gate7Delay= getIntSafely(getDelayGateSeven())
	gate8Delay= getIntSafely(getDelayGateEight())

	gates = [gate1, gate2,gate3,gate4, gate5, gate6, gate7, gate8]
	delays = [[],[],[],[],[],[],[],[]]
	delaysValue = [gate1Delay, gate2Delay,gate3Delay,gate4Delay,gate5Delay, gate6Delay, gate7Delay,gate8Delay ]
	gatesActive = [gate1Active,gate2Active,gate3Active,gate4Active,gate5Active,gate6Active,gate7Active,gate8Active]
	itemsCount = [0,0,0,0,0,0,0,0]
	isStop = False

	return gates, delays, delaysValue, gatesActive, itemsCount, isStop

def thread_function(name):
	# This is the section of code which creates the a label
	

	Sensor1 = True
	Weight = random.randrange(0, 1000, 50)
	Count = 0
	gates = []
	isStop = False
	delays = [[],[],[],[],[],[],[],[]]
	delaysValue =[] 
	gatesActive = []
	itemsCount = [0,0,0,0,0,0,0,0]
	
	gates, delays, delaysValue, gatesActive, itemsCount, isStop = initParams()
	print(gates, delays,delaysValue,gatesActive, len(gates))
	
	##################### MAIN LOOP ######################

	textWeight = tk.StringVar()
	textWeight.set("")

	lblWeight =  tk.Label(root, textvariable=textWeight).place(x=360, y=41)

	textC1 = tk.StringVar()
	textC1.set("0")
	textC2 = tk.StringVar()
	textC2.set("0")
	textC3 = tk.StringVar()
	textC3.set("0")
	textC4 = tk.StringVar()
	textC4.set("0")
	textC5 = tk.StringVar()
	textC5.set("0")
	textC6 = tk.StringVar()
	textC6.set("0")
	textC7 = tk.StringVar()
	textC7.set("0")
	textC8 = tk.StringVar()
	textC8.set("0")

	countersLabelArrays = [textC1,textC2,textC3,textC4,textC5,textC6,textC7,textC8]

	lblCg1 = tk.Label(root, textvariable=countersLabelArrays[0]).place(x=580, y=131)
	lblCg2 = tk.Label(root, textvariable=countersLabelArrays[1]).place(x=580, y=171)
	lblCg3 = tk.Label(root, textvariable=countersLabelArrays[2]).place(x=580, y=211)
	lblCg4 = tk.Label(root, textvariable=countersLabelArrays[3]).place(x=580, y=251)
	lblCg5 = tk.Label(root, textvariable=countersLabelArrays[4]).place(x=580, y=291)
	lblCg6 = tk.Label(root, textvariable=countersLabelArrays[5]).place(x=580, y=331)
	lblCg7 = tk.Label(root, textvariable=countersLabelArrays[6]).place(x=580, y=371)
	lblCg8 = tk.Label(root, textvariable=countersLabelArrays[7]).place(x=580, y=411)

	strClosed = 'closed'
		
	text1 = tk.StringVar()
	text1.set("closed")
	text2 = tk.StringVar()
	text2.set("closed")
	text3 = tk.StringVar()
	text3.set("closed")
	text4 = tk.StringVar()
	text4.set("closed")
	text5 = tk.StringVar()
	text5.set("closed")
	text6 = tk.StringVar()
	text6.set("closed")
	text7 = tk.StringVar()
	text7.set("closed")
	text8 = tk.StringVar()
	text8.set("closed")


	lblsArray = [text1,text2,text3,text4,text5,text6,text7,text8]

	lblS1 = tk.Label(root, textvariable=lblsArray[0]).place(x=720, y=131)
	lblS2 = tk.Label(root, textvariable=lblsArray[1]).place(x=720, y=171)
	lblS3 = tk.Label(root, textvariable=lblsArray[2]).place(x=720, y=211)
	lblS4 = tk.Label(root, textvariable=lblsArray[3]).place(x=720, y=251)
	lblS5 = tk.Label(root, textvariable=lblsArray[4]).place(x=720, y=291)
	lblS6 = tk.Label(root, textvariable=lblsArray[5]).place(x=720, y=331)
	lblS7 = tk.Label(root, textvariable=lblsArray[6]).place(x=720, y=371)
	lblS8 = tk.Label(root, textvariable=lblsArray[7]).place(x=720, y=411)


	while True:

		global stop_threads
		if stop_threads:
			break

		time.sleep(1)
		lblsArray[0].set("closed")
		lblsArray[1].set("closed")
		lblsArray[2].set("closed")
		lblsArray[3].set("closed")
		lblsArray[4].set("closed")
		lblsArray[5].set("closed")
		lblsArray[6].set("closed")
		lblsArray[7].set("closed")
		
		Sensor1 = IsSensor1(Sensor1)
		Weight = GetWeight()

		weightValue = str(Weight)
		textWeight.set(weightValue)

		if Sensor1:

			Count = Count + 1

			# ### DELAY ########################################
			for i in range(0, len(gates)):
				if gatesActive[i]:
					if delays[i].__contains__(Count):
						openGateThread = threading.Thread(target=OpenGate, args=(i+1,))
						openGateThread.start()
						lblsArray[i].set('open')
						delays[i].remove(min(delays[i]))

						itemsCount[i] += 1

			### WEIGHTS ########################################
			for i in range(0, len(gates)):
				if gatesActive[i]:
					if gates[i][0] <= Weight <= gates[i][1]:
						delays[i].append(delaysValue[i] + Count)


		if Sensor1:
			print(Count, Sensor1, Weight)
			print(delays)
			print(itemsCount)
			countersLabelArrays[0].set(itemsCount[0])
			countersLabelArrays[1].set(itemsCount[1])
			countersLabelArrays[2].set(itemsCount[2])
			countersLabelArrays[3].set(itemsCount[3])
			countersLabelArrays[4].set(itemsCount[4])
			countersLabelArrays[5].set(itemsCount[5])
			countersLabelArrays[6].set(itemsCount[6])
			countersLabelArrays[7].set(itemsCount[7])
	###################################################

# this is the function called when the button is clicked
def btnClickFunctionStart():
	print('Start')
	global x
	x = threading.Thread(target=thread_function, args=(1,))
	x.start()
	global stop_threads
	stop_threads = False
	

# this is the function called when the button is clicked
def btnClickFunctionStop():
	global stop_threads
	stop_threads = True
	print('Stop')


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable1():
	checkedOrNot = cbVariable1.get()
	return checkedOrNot
	

# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable2():
	checkedOrNot = cbVariable2.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable3():
	checkedOrNot = cbVariable3.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable4():
	checkedOrNot = cbVariable4.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable5():
	checkedOrNot = cbVariable5.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable6():
	checkedOrNot = cbVariable6.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable7():
	checkedOrNot = cbVariable7.get()
	return checkedOrNot


# this is a function to check the status of the checkbox (1 means checked, and 0 means unchecked)
def getCbVariable8():
	checkedOrNot = cbVariable8.get()
	return checkedOrNot

# this is a function to get the user input from the text input box
def getMinGateOne():
	userInput = MinGateOne.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateOne():
	userInput = MaxGateOne.get()
	return userInput

# this is a function to get the user input from the text input box
def getMinGateTwo():
	userInput = MinGateTwo.get()
	return userInput


# this is a function to get the user input from the text input box
def getMinGateTree():
	userInput = MinGateTree.get()
	return userInput


# this is a function to get the user input from the text input box
def getMinGateFour():
	userInput = MinGateFour.get()
	return userInput


# this is a function to get the user input from the text input box
def getMinGateFive():
	userInput = MinGateFive.get()
	return userInput


# this is a function to get the user input from the text input box
def getMinGateSix():
	userInput = MinGateSix.get()
	return userInput


# this is a function to get the user input from the text input box
def getMinGateSeven():
	userInput = MinGateSeven.get()
	return userInput


# this is a function to get the user input from the text input box
def getMinGateEight():
	userInput = MinGateEight.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateEight():
	userInput = MaxGateEight.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateSeven():
	userInput = MaxGateSeven.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateSix():
	userInput = MaxGateSix.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateFive():
	userInput = MaxGateFive.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateFour():
	userInput = MaxGateFour.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateTree():
	userInput = MaxGateTree.get()
	return userInput


# this is a function to get the user input from the text input box
def getMaxGateTwo():
	userInput = MaxGateTwo.get()
	return userInput

# this is a function to get the user input from the text input box
def getDelayGateOne():
	userInput = DelayGateOne.get()
	return userInput


# this is a function to get the user input from the text input box
def getDelayGateTwo():
	userInput = DelayGateTwo.get()
	return userInput

# this is a function to get the user input from the text input box
def getDelayGateThree():
	userInput = DelayGateThree.get()
	return userInput


# this is a function to get the user input from the text input box
def getDelayGateFour():
	userInput = DelayGateFour.get()
	return userInput


# this is a function to get the user input from the text input box
def getDelayGateSix():
	userInput = DelayGateSix.get()
	return userInput

# this is a function to get the user input from the text input box
def getDelayGateFive():
	userInput = DelayGateFive.get()
	return userInput


# this is a function to get the user input from the text input box
def getDelayGateSeven():
	userInput = DelayGateSeven.get()
	return userInput

# this is a function to get the user input from the text input box
def getDelayGateEight():
	userInput = DelayGateEight.get()
	return userInput




#this is the declaration of the variable associated with the checkbox
cbVariable1 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable2 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable3 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable4 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable5 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable6 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable7 = tk.IntVar()


#this is the declaration of the variable associated with the checkbox
cbVariable8 = tk.IntVar()


# This is the section of code which creates the main window
root.geometry('1024x600')
root.configure(background='#BEBEBE')
root.title('Fruit Sort App')

# this is the function called when the button is clicked
def btnClickFunctionRest():
	cbVariable1.set(False)
	cbVariable2.set(False)
	cbVariable3.set(False)
	cbVariable4.set(False)
	cbVariable5.set(False)
	cbVariable6.set(False)
	cbVariable7.set(False)
	cbVariable8.set(False)

	MinGateOne.delete(0, "end")
	MinGateTwo.delete(0, "end")
	MinGateTree.delete(0, "end")
	MinGateFour.delete(0, "end")
	MinGateFive.delete(0, "end")
	MinGateSix.delete(0, "end")
	MinGateSeven.delete(0, "end")
	MinGateEight.delete(0, "end")

	MaxGateOne.delete(0, "end")
	MaxGateTwo.delete(0, "end")
	MaxGateTree.delete(0, "end")
	MaxGateFour.delete(0, "end")
	MaxGateFive.delete(0, "end")
	MaxGateSix.delete(0, "end")
	MaxGateSeven.delete(0, "end")
	MaxGateEight.delete(0, "end")

	DelayGateOne.delete(0, "end")
	DelayGateTwo.delete(0, "end")
	DelayGateThree.delete(0, "end")
	DelayGateFour.delete(0, "end")
	DelayGateFive.delete(0, "end")
	DelayGateSix.delete(0, "end")
	DelayGateSeven.delete(0, "end")
	DelayGateEight.delete(0, "end")

	print('Rest')


# This is the section of code which creates a button
Button(root, text='Start', bg='#FAEBD7', font=('arial', 12, 'normal'), command=btnClickFunctionStart).place(x=40, y=31)


# This is the section of code which creates a button
Button(root, text='Stop', bg='#FAEBD7', font=('arial', 12, 'normal'), command=btnClickFunctionStop).place(x=110, y=31)


# This is the section of code which creates a button
Button(root, text='Reset', bg='#FAEBD7', font=('arial', 12, 'normal'), command=btnClickFunctionRest).place(x=180, y=31)

# This is the section of code which creates a checkbox
CheckGateOne=Checkbutton(root, text='Gate1', variable=cbVariable1, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateOne.place(x=40, y=131)


# This is the section of code which creates a checkbox
CheckGateTwo=Checkbutton(root, text='Gate2', variable=cbVariable2, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateTwo.place(x=40, y=171)


# This is the section of code which creates a checkbox
CheckGateThree=Checkbutton(root, text='Gate3', variable=cbVariable3, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateThree.place(x=40, y=211)


# This is the section of code which creates a checkbox
CheckGateFour=Checkbutton(root, text='Gate4', variable=cbVariable4, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateFour.place(x=40, y=251)


# This is the section of code which creates a checkbox
CheckGateFive=Checkbutton(root, text='Gate5', variable=cbVariable5, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateFive.place(x=40, y=291)


# This is the section of code which creates a checkbox
CheckGateSix=Checkbutton(root, text='Gate6', variable=cbVariable6, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateSix.place(x=40, y=331)


# This is the section of code which creates a checkbox
CheckGateSeven=Checkbutton(root, text='Gate7', variable=cbVariable7, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateSeven.place(x=40, y=371)


# This is the section of code which creates a checkbox
CheckGateEight=Checkbutton(root, text='Gate8', variable=cbVariable8, bg='#FAEBD7', font=('arial', 12, 'normal'))
CheckGateEight.place(x=40, y=411)


# This is the section of code which creates a text input box
MinGateOne=Entry(root)
MinGateOne.place(x=130, y=131)

# This is the section of code which creates a text input box
MaxGateOne=Entry(root)
MaxGateOne.place(x=280, y=131)

# This is the section of code which creates a text input box
DelayGateOne=Entry(root)
DelayGateOne.place(x=430, y=131)

# This is the section of code which creates the a label


# This is the section of code which creates a text input box
MinGateTwo=Entry(root)
MinGateTwo.place(x=130, y=171)

# This is the section of code which creates a text input box
MaxGateTwo=Entry(root)
MaxGateTwo.place(x=280, y=171)

# This is the section of code which creates a text input box
DelayGateTwo=Entry(root)
DelayGateTwo.place(x=430, y=171)



# This is the section of code which creates a text input box
MinGateTree=Entry(root)
MinGateTree.place(x=130, y=211)

# This is the section of code which creates a text input box
MaxGateTree=Entry(root)
MaxGateTree.place(x=280, y=211)

# This is the section of code which creates a text input box
DelayGateThree=Entry(root)
DelayGateThree.place(x=430, y=211)



# This is the section of code which creates a text input box
MinGateFour=Entry(root)
MinGateFour.place(x=130, y=251)

# This is the section of code which creates a text input box
MaxGateFour=Entry(root)
MaxGateFour.place(x=280, y=251)

# This is the section of code which creates a text input box
DelayGateFour=Entry(root)
DelayGateFour.place(x=430, y=251)

# This is the section of code which creates a text input box
MinGateFive=Entry(root)
MinGateFive.place(x=130, y=291)

# This is the section of code which creates a text input box
MaxGateFive=Entry(root)
MaxGateFive.place(x=280, y=291)

# This is the section of code which creates a text input box
DelayGateFive=Entry(root)
DelayGateFive.place(x=430, y=291)



# This is the section of code which creates a text input box
MinGateSix=Entry(root)
MinGateSix.place(x=130, y=331)

# This is the section of code which creates a text input box
MaxGateSix=Entry(root)
MaxGateSix.place(x=280, y=331)

# This is the section of code which creates a text input box
DelayGateSix=Entry(root)
DelayGateSix.place(x=430, y=331)



# This is the section of code which creates a text input box
MinGateSeven=Entry(root)
MinGateSeven.place(x=130, y=371)

# This is the section of code which creates a text input box
MaxGateSeven=Entry(root)
MaxGateSeven.place(x=280, y=371)

# This is the section of code which creates a text input box
DelayGateSeven=Entry(root)
DelayGateSeven.place(x=430, y=371)



# This is the section of code which creates a text input box
MinGateEight=Entry(root)
MinGateEight.place(x=130, y=411)

# This is the section of code which creates a text input box
MaxGateEight=Entry(root)
MaxGateEight.place(x=280, y=411)

# This is the section of code which creates a text input box
DelayGateEight=Entry(root)
DelayGateEight.place(x=430, y=411)





# This is the section of code which creates the a label
Label(root, text='Weight: ', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=290, y=41)


# This is the section of code which creates the a label
Label(root, text='Min.', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=130, y=91)


# This is the section of code which creates the a label
Label(root, text='Max.', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=280, y=91)


# This is the section of code which creates the a label
Label(root, text='Delay', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=430, y=91)


# This is the section of code which creates the a label
Label(root, text='Count', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=580, y=91)


# This is the section of code which creates the a label
Label(root, text='Gate State', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=720, y=91)



root.mainloop()

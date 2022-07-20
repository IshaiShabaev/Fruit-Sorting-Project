import tkinter as tk
from tkinter import ttk
from tkinter import * 
import random, time, threading, sys
from threading import Timer

from gpiozero import LED, Button
from time import sleep
from signal import pause

global my_full_screen
my_full_screen = True

#mishkal
import RPi.GPIO as GPIO
from hx711 import HX711

root = Tk()

global x

global stop_threads
stop_threads = False

global weightValue
weightValue = 'asdfa'


#mishkal init
def cleanAndExit():
    print("Cleaning...")
    GPIO.cleanup()
    print("Bye!")
    sys.exit()

hx = HX711(5, 6)

hx.set_reading_format("MSB", "MSB")

hx.set_reference_unit(1)
#hx.set_reference_unit(referenceUnit)

hx.reset()

hx.tare()

print("Tare done! Add weight now...")

# to use both channels, you'll need to tare them both
hx.tare_A()
hx.tare_B()

#end mishkal init

#key#

def create_keypad(root):
    keypad = tk.Frame(root)

    for y in range(3):
        for x in range(3):
            val = y*3 + x
            text = str(val) 
            b = tk.Button(keypad, text=text, command=lambda txt=text:insert_text(txt))
            b.grid(row=y, column=x, sticky='news')

    x = tk.Button(keypad, text='Hide', command=hide_keypad)
    x.grid(row=10, column=0, columnspan=3, sticky='news')

    return keypad

def insert_text(text):
    target.insert('end', text)

def show_keypad(widget):
    global target
    target = widget

    keypad.place(relx=0.5, rely=0.5, anchor='c')

def hide_keypad():
    global taget
    target = None

    keypad.place_forget()

#end key#

def GetWeight():
	#w = random.randrange(0, 1000, 50)
	try:
		val = hx.get_weight(5)
		print(val)
		hx.power_down()
		hx.power_up()
		time.sleep(0.1)

	except (KeyboardInterrupt, SystemExit):
		cleanAndExit()
    
	return val

def IsSensor1 (Sensor):
    button = Button(26)
    while True:
        button.wait_for_press()
        #print("The button was pressed!")
        button.wait_for_release()
        #print("The button was release!")
        return not Sensor

def OpenGate(gate):
	if gate == 1:
            gate = LED(16)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 1")
	if gate == 2:
            gate = LED(12)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 2")
	if gate == 3:
            gate = LED(7)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 3")
	if gate == 4:
            gate = LED(8)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 4")
	if gate == 5:
            gate = LED(25)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 5")
	if gate == 6:
            gate = LED(24)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 6")
	if gate == 7:
            gate = LED(23)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 7")
	if gate == 8:
            gate = LED(18)
            gate.off()
            sleep(0.5)
            gate.on()
            sleep(0.01)
		#print("open gate 8")



def getIntSafely(val):
	if val != '' and val.isnumeric():
		return int(val)
	else:
		return 0



def initParams():
	################# RESET / START ############################
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
	

	Sensor1 = False
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

	lblWeight =  tk.Label(root, textvariable=textWeight).place(x=835, y=550)

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

	lblCg1 = tk.Label(root, textvariable=countersLabelArrays[0]).place(x=810, y=150)
	lblCg2 = tk.Label(root, textvariable=countersLabelArrays[1]).place(x=810, y=200)
	lblCg3 = tk.Label(root, textvariable=countersLabelArrays[2]).place(x=810, y=250)
	lblCg4 = tk.Label(root, textvariable=countersLabelArrays[3]).place(x=810, y=300)
	lblCg5 = tk.Label(root, textvariable=countersLabelArrays[4]).place(x=810, y=350)
	lblCg6 = tk.Label(root, textvariable=countersLabelArrays[5]).place(x=810, y=400)
	lblCg7 = tk.Label(root, textvariable=countersLabelArrays[6]).place(x=810, y=450)
	lblCg8 = tk.Label(root, textvariable=countersLabelArrays[7]).place(x=810, y=500)

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

	lblS1 = tk.Label(root, textvariable=lblsArray[0]).place(x=910, y=150)
	lblS2 = tk.Label(root, textvariable=lblsArray[1]).place(x=910, y=200)
	lblS3 = tk.Label(root, textvariable=lblsArray[2]).place(x=910, y=250)
	lblS4 = tk.Label(root, textvariable=lblsArray[3]).place(x=910, y=300)
	lblS5 = tk.Label(root, textvariable=lblsArray[4]).place(x=910, y=350)
	lblS6 = tk.Label(root, textvariable=lblsArray[5]).place(x=910, y=400)
	lblS7 = tk.Label(root, textvariable=lblsArray[6]).place(x=910, y=450)
	lblS8 = tk.Label(root, textvariable=lblsArray[7]).place(x=910, y=500)


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
			
		Sensor1 = not Sensor1 # add for sensor reset 

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
if (my_full_screen == True):
	root.attributes('-fullscreen', True)
root.configure(background='#BEBEBE')
root.title('Fruit Sort App')

keypad = create_keypad(root)
target = None

f = tk.Frame(root)
f.pack()

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
tk.Button(root, text='START', bg='#6E8B3D', font=('arial', 34, 'bold'), command=btnClickFunctionStart).place(x=50, y=30)


# This is the section of code which creates a button
tk.Button(root, text='STOP', bg='#CD3333', font=('arial', 34, 'bold'), command=btnClickFunctionStop).place(x=250, y=30)


# This is the section of code which creates a button
tk.Button(root, text='RESET', bg='#00CED1', font=('arial', 34, 'bold'), command=btnClickFunctionRest).place(x=820, y=30)

# This is the section of code which creates a checkbox
CheckGateOne=Checkbutton(root, text='Gate1', variable=cbVariable1, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateOne.place(x=35, y=150)


# This is the section of code which creates a checkbox
CheckGateTwo=Checkbutton(root, text='Gate2', variable=cbVariable2, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateTwo.place(x=35, y=200)


# This is the section of code which creates a checkbox
CheckGateThree=Checkbutton(root, text='Gate3', variable=cbVariable3, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateThree.place(x=35, y=250)


# This is the section of code which creates a checkbox
CheckGateFour=Checkbutton(root, text='Gate4', variable=cbVariable4, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateFour.place(x=35, y=300)


# This is the section of code which creates a checkbox
CheckGateFive=Checkbutton(root, text='Gate5', variable=cbVariable5, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateFive.place(x=35, y=350)


# This is the section of code which creates a checkbox
CheckGateSix=Checkbutton(root, text='Gate6', variable=cbVariable6, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateSix.place(x=35, y=400)


# This is the section of code which creates a checkbox
CheckGateSeven=Checkbutton(root, text='Gate7', variable=cbVariable7, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateSeven.place(x=35, y=450)


# This is the section of code which creates a checkbox
CheckGateEight=Checkbutton(root, text='Gate8', variable=cbVariable8, bg='#E0EEEE', font=('arial', 18, 'normal'))
CheckGateEight.place(x=35, y=500)


# This is the section of code which creates a text input box
MinGateOne=Entry(root, font=('arial', 14, 'normal'))
MinGateOne.place(x=150, y=150)

# This is the section of code which creates a text input box
MaxGateOne=Entry(root, font=('arial', 14, 'normal'))
MaxGateOne.place(x=360, y=150)

# This is the section of code which creates a text input box
DelayGateOne=Entry(root, font=('arial', 14, 'normal'))
DelayGateOne.place(x=570, y=150)

# This is the section of code which creates the a label


# This is the section of code which creates a text input box
MinGateTwo=Entry(root, font=('arial', 14, 'normal'))
MinGateTwo.place(x=150, y=200)

# This is the section of code which creates a text input box
MaxGateTwo=Entry(root, font=('arial', 14, 'normal'))
MaxGateTwo.place(x=360, y=200)

# This is the section of code which creates a text input box
DelayGateTwo=Entry(root, font=('arial', 14, 'normal'))
DelayGateTwo.place(x=570, y=200)



# This is the section of code which creates a text input box
MinGateTree=Entry(root, font=('arial', 14, 'normal'))
MinGateTree.place(x=150, y=250)

# This is the section of code which creates a text input box
MaxGateTree=Entry(root, font=('arial', 14, 'normal'))
MaxGateTree.place(x=360, y=250)

# This is the section of code which creates a text input box
DelayGateThree=Entry(root, font=('arial', 14, 'normal'))
DelayGateThree.place(x=570, y=250)



# This is the section of code which creates a text input box
MinGateFour=Entry(root, font=('arial', 14, 'normal'))
MinGateFour.place(x=150, y=300)

# This is the section of code which creates a text input box
MaxGateFour=Entry(root, font=('arial', 14, 'normal'))
MaxGateFour.place(x=360, y=300)

# This is the section of code which creates a text input box
DelayGateFour=Entry(root, font=('arial', 14, 'normal'))
DelayGateFour.place(x=570, y=300)

# This is the section of code which creates a text input box
MinGateFive=Entry(root, font=('arial', 14, 'normal'))
MinGateFive.place(x=150, y=350)

# This is the section of code which creates a text input box
MaxGateFive=Entry(root, font=('arial', 14, 'normal'))
MaxGateFive.place(x=360, y=350)

# This is the section of code which creates a text input box
DelayGateFive=Entry(root, font=('arial', 14, 'normal'))
DelayGateFive.place(x=570, y=350)



# This is the section of code which creates a text input box
MinGateSix=Entry(root, font=('arial', 14, 'normal'))
MinGateSix.place(x=150, y=400)

# This is the section of code which creates a text input box
MaxGateSix=Entry(root, font=('arial', 14, 'normal'))
MaxGateSix.place(x=360, y=400)

# This is the section of code which creates a text input box
DelayGateSix=Entry(root, font=('arial', 14, 'normal'))
DelayGateSix.place(x=570, y=400)



# This is the section of code which creates a text input box
MinGateSeven=Entry(root, font=('arial', 14, 'normal'))
MinGateSeven.place(x=150, y=450)

# This is the section of code which creates a text input box
MaxGateSeven=Entry(root, font=('arial', 14, 'normal'))
MaxGateSeven.place(x=360, y=450)

# This is the section of code which creates a text input box
DelayGateSeven=Entry(root, font=('arial', 14, 'normal'))
DelayGateSeven.place(x=570, y=450)



# This is the section of code which creates a text input box
MinGateEight=Entry(root, font=('arial', 14, 'normal'))
MinGateEight.place(x=150, y=500)

# This is the section of code which creates a text input box
MaxGateEight=Entry(root, font=('arial', 14, 'normal'))
MaxGateEight.place(x=360, y=500)

# This is the section of code which creates a text input box
DelayGateEight=Entry(root, font=('arial', 14, 'normal'))
DelayGateEight.place(x=570, y=500)





# This is the section of code which creates the a label
Label(root, text='Weight: ', bg='#BEBEBE', font=('arial', 12, 'normal')).place(x=745, y=550)


# This is the section of code which creates the a label
Label(root, text='Min.', bg='#BEBEBE', font=('arial', 12, 'bold')).place(x=220, y=120)


# This is the section of code which creates the a label
Label(root, text='Max.', bg='#BEBEBE', font=('arial', 12, 'bold')).place(x=430, y=120)


# This is the section of code which creates the a label
Label(root, text='Delay', bg='#BEBEBE', font=('arial', 12, 'bold')).place(x=630, y=120)


# This is the section of code which creates the a label
Label(root, text='Count', bg='#BEBEBE', font=('arial', 12, 'bold')).place(x=795, y=120)


# This is the section of code which creates the a label
Label(root, text='Gate State', bg='#BEBEBE', font=('arial', 12, 'bold')).place(x=895, y=120)



root.mainloop()

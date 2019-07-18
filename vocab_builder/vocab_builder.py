from tkinter import *
import Read_PDF
from tkinter import messagebox
from random import randint, randrange

wrong_words=[]
wrong_ans_int=0
correct_ans_int=0
practiced_q=0
random_no = 0

def gen_random():
    global random_no
    global randon_no_list
    random_no = randrange(0, 1054)
    return random_no

def quit():
    top.destroy()

def yesFunction():
    global practiced_q
    global correct_ans_int
    correct_ans_int = correct_ans_int + 1
    correct_ans.set("correct ones: " + str(correct_ans_int))
    random_no = gen_random()
    var.set(Read_PDF.word[random_no])
    practiced_q = practiced_q + 1
    UpdatePractice()

def noFunction():
    global practiced_q
    global wrong_ans_int
    wrong_ans_int = wrong_ans_int + 1
    wrong_ans.set("Wrong ones: "+str(wrong_ans_int))
    random_no = gen_random()
    var.set(Read_PDF.word[random_no])
    wrong_words.append(Read_PDF.word[random_no])
    practiced_q = practiced_q + 1
    UpdatePractice()

def meaningFunction():
    msg = messagebox.showinfo("Meaning",Read_PDF.meaning[random_no])

def PracticeScrewedOnes():
    #print (len(wrong_words))
    random_nos = randrange(0, len(wrong_words))
    var.set(wrong_words[random_nos])

def UpdatePractice():
    practiced.set("practiced ones: " + str(practiced_q))

top = Tk()

top.geometry("300x250")

var = StringVar()
label = Label( top, textvariable = var, relief = FLAT ,pady = 20)
var.set(Read_PDF.word[gen_random()])
label.pack()

B = Button(top, text = "yes", command = yesFunction)
B.place(x = 50,y = 150)

n = Button(top, text = "No", command = noFunction)
n.place(x = 100,y = 150)

m = Button(top, text = "Meaning", command = meaningFunction)
m.place(x = 150,y = 150)


correct_ans = StringVar()
correct_label = Label(top, textvariable = str(correct_ans), relief = FLAT )
correct_ans.set("correct ones: ")
correct_label.pack()


wrong_ans = StringVar()
wrong_label = Label(top, textvariable = str(wrong_ans), relief = FLAT )
wrong_ans.set("Wrong ones: ")
wrong_label.pack()

practiced = StringVar()
practiced_label = Label(top, textvariable = str(practiced), relief = FLAT )
practiced.set("practiced ones: ")
practiced_label.pack()

ww = Button(top, text = "Practice screwed ones", command = PracticeScrewedOnes)
ww.place(x = 50,y = 190)


top.mainloop()

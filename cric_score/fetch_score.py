import data
from tkinter import *

update=data.data

update.refresh('self')

top = Tk()

top.geometry("300x250")



ww = Button(top, text = "Refresh", command = update.refresh('self'))
ww.place(x = 100,y=180)


var_s = StringVar()
print(update.score)
label_s = Label( top, textvariable =var_s, relief = FLAT ,pady = 20)
var_s.set("SCORE :"+update.score)
label_s.pack()

var_o = StringVar()
label_o = Label( top, textvariable = var_o)
var_o.set("OVERS :"+update.overs)
label_o.pack()

var_b1 = StringVar()
label_b1 = Label( top, textvariable = var_b1)
var_b1.set(""+update.batsman1)
label_b1.pack()

var_b2 = StringVar()
label_b2 = Label( top, textvariable = var_b2)
var_b2.set(""+update.batsman2)
label_b2.pack()

var_bo = StringVar()
label_bo = Label( top, textvariable = var_bo )
var_bo.set(""+update.Bowler)
label_bo.pack()



top.mainloop()

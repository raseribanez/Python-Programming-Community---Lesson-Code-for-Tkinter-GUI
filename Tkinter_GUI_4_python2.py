from Tkinter import *

top = Tk()
top.title('Tkinter GUI - Example 4')
top.minsize(400, 400)
top.configure(bg="orange")

lbl = Label(top, text="Assigning Functions To Buttons", bg='yellow', fg='blue', font='14') 
lbl.pack() 

def hello_callback(): print ("Button Clicked")

def callback():
  print(ent.get())

btn = Button(top, text="Click Here", font='freesansbold, 14', command=hello_callback)
btn.pack() 

exit_button=Button(top, text="Exit", fg='red', bg='black', font='freesansbold, 14', command=quit) 
exit_button.pack(side=BOTTOM)

ent = Entry(top)
ent.pack()

btn2 = Button(top, text = "Print Text", fg='blue', font='bold, 14', width=15, command=callback)
btn2.pack()

top.mainloop()

from tkinter import *

top = Tk()
top.title('Tkinter GUI - Example 3')
top.minsize(800, 800)
top.configure(bg='orange')

lbl = Label(top, text='A Basic Window With 2 Buttons') 
lbl.pack() 

def hello_callback(): print ('Button Clicked')

btn = Button(top, text='Click Here', font='freesansbold, 14', command=hello_callback)
btn.pack() 

exit_button = Button(top, text='Exit', fg='red', bg='black', font='freesansbold, 14', command=quit) 
exit_button.pack(side=BOTTOM) 

top.mainloop()


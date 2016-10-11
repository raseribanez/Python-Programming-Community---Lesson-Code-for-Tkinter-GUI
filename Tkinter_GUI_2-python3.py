from tkinter import *

top = Tk()
top.minsize(400,400)
top.title("Tkinter Basic GUI's")

exit_button = Button(top, text='Exit', fg='red', bg='black', font='freesansbold, 12', command=quit)
exit_button.pack(side=BOTTOM)

top.mainloop                                                                                     

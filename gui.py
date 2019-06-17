from tkinter import *
import t_to_s as t2s
import s_to_t as s2t
def click():
    t=text.get("1.0","end")
    t2s.text2speech(t)
def click1():
    output.delete("1.0","end")
    out= s2t.recognize()
    output.insert(END, out)
    
window = Tk()
window.title("text2speech & speech2text")
window.configure(background="grey")
window.geometry("1200x400") #You want the size of the app to be 500x500
window.resizable(0, 0) #Don't allow resizing in the x or y direction
# for text to speech------------------------------------------------------------------------------------
Label (window, text="         TEXT TO SPEECH      ",bg="black",fg="red",font="none 35 bold") .grid(row=2, column=0, sticky=W)
Label (window, text="                  ENTER THE TEXT",bg="grey",fg="blue",font="none 20 bold") .grid(row=4, column=0, sticky=W)
text= Text(window, width=50,height=10,bg="white")
text.grid(row=5,column=0)
Button(window,text="CONVERT",width=10,command=click) .grid(row=6)
# for speech to text------------------------------------------------------------------------------------
Label (window, text="      SPEECH TO TEXT          ",bg="red",fg="black",font="none 35 bold") .grid(row=2, column=1, sticky=W)
Button(window,text="START LISTNING",width=14,command=click1) .grid(row=4,column=1)
output = Text(window, width=50,height=10,wrap=WORD,bg="white")
output.grid(row=5,column=1)

#mainloop
window.mainloop()

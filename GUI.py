from tkinter import *
import nltk
from search import search
import webbrowser




#making window
win=Tk()
win.title("Search Engine")
win.geometry("1200x700")

#making frame
frame = Frame(win, bg="white")
frame.pack(expand=True, fill=BOTH)

#making JITZ title
label1=Label(frame,fg="dark blue", bg="white", text="JITZ",font=("Times New Roman", 40, "bold"))
label1.pack(padx=10, pady=30, side=TOP)

#making the text box
e1 = Entry(frame,font=(29),width=95)
e1.place(x=200, y=100)
e1.focus_set()

#making the enter number label
label2=Label(frame, fg="dark blue", bg="white", text="Enter number of search results ", font=("Times New Roman", 12))
label2.place(x=500, y=150)

#making the spinbox option
spin = Spinbox(frame, from_ = 0, to = 10) 
spin.place(x=700, y=150)
spin.focus_set()

#frame at the bottom for search results
global list_frame
list_frame = Frame(win, bg="white")
list_frame.pack(side=BOTTOM)


def callback(event,href):
    webbrowser.open_new(href)


#this should return the results
def results():
        
        x=e1.get()
        x=x.lower()
        h=int(spin.get())#gets the data from spin box
        y=search(nltk.word_tokenize(x),h)
        
        return y
    
#this calls the result function   
def printtimes():

    try:
        for widget in list_frame.winfo_children():
            widget.destroy()
    except:1
    
    
    data=results()
    i=0
    labels=[]
    for href in data:
        labels.append(Label(list_frame,text=href))
        labels[i].pack()
        labels[i].bind("<Button-1>",webbrowser.open_new(href))

        i+=1

    
        
##        listbox.insert(END,href)
##        listbox.bind("<Button-1>",webbrowser.open_new(href))
##        
##    while h>0: #calls the result funstion h times
##        listbox.insert(END, results())
##        h-=1

          
#search button        
Button=Button(frame, text="GO", fg="dark blue", command=printtimes)
Button.place(x=1080, y=100)

mainloop()







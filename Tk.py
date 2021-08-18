from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
import csv
import time

root = Tk()
root.title("Frisco File Processing")
root.geometry('700x400')
root.resizable(0,0)
#window settings


DirectoryName = Entry(root, font = 40, width = 45)
DirectoryName.place(x = 140,y = 70)

#path directory bar

outputwindow = Text(root, bd=0, height="10", width="60", font="Arial",)
outputwindow.pack(side=BOTTOM)
outputwindow.config(state=DISABLED)




filename = None


def SearchFunc():
    
    global filename
    filename = filedialog.askopenfilename(filetypes = (("CSV files","*CSV"),("All files","*.*")))
    
    DirectoryName.delete(0, END)
    DirectoryName.insert(0, filename) #updates text in path directory bar
   
    if not filename:
        
        outputwindow.config(state=NORMAL)
        outputwindow.update
        outputwindow.delete('1.0', END)
        outputwindow.tag_configure('left', foreground='red', font = "arial 9 bold")
        outputwindow.insert("1.0", "Error: Did not select any file, try again.\n")
        outputwindow.tag_add("left", "1.0", "end")
        outputwindow.tag_remove("the_tag", "1.0", "end")
        
        
        
        outputwindow.pack()
        outputwindow.config(state=DISABLED)
    
    elif not ".csv" in filename and not ".CSV" in filename:
        outputwindow.config(state=NORMAL)
        outputwindow.update
        outputwindow.delete('1.0', END)
        outputwindow.tag_configure('left', foreground='red', font = "arial 9 bold")
        outputwindow.insert("1.0", "Error: Did not select a .csv file.\n", "left")
        outputwindow.tag_add("left", "1.0", "end")
        outputwindow.tag_remove("the_tag", "1.0", "end")
        
        
        
        outputwindow.pack()
        outputwindow.config(state=DISABLED)
    
    else:
        outputwindow.config(state=NORMAL)
        outputwindow.delete('1.0', END)
        outputwindow.update()
        
        outputwindow.tag_configure("center", justify='center', foreground='black', font = "arial 13 bold")
        outputwindow.insert("1.0", "File Loaded\n", "center")
        outputwindow.tag_add("center", "1.0", "end")

        outputwindow.tag_remove("the_tag", "1.0", "end")
        outputwindow.pack()
        
        outputwindow.config(state=DISABLED)
   
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        data = list(reader)
        
        del data[0]
    data = list(filter(None, data))
    print(data, flush=True)
    
    max_currentlist = max(data, key=lambda x: x[1]) 
    max_timelist = max(data, key=lambda x: x[0])
    current = max_currentlist[1]
    time = max_timelist[0]
    print(time)
    print(current)


    CurrentConversion_90 = float(max_currentlist[1]) * .9
    CurrentConversion_10 = float(max_currentlist[1]) * .1
    TitleAt_90 = min(data,key=lambda x: abs(float(x[1]) - CurrentConversion_90))
    TitleAt_10 = min(data,key=lambda x: abs(float(x[1]) - CurrentConversion_10))
    print(TitleAt_90)
    print(TitleAt_10)
    


    outputwindow.config(state=NORMAL)
    outputwindow.tag_configure('black', foreground='black', font = "arial 9")
    outputwindow.insert(END, "The maximum value of the current is: " + current, "black")
    outputwindow.insert(END, "\nThe time the current reaches 90% value is:" + TitleAt_90[0], "black")
    outputwindow.insert(END, "\nThe time the current reaches 10% value is:" + TitleAt_10[0], "black")
    outputwindow.config(state=DISABLED)
        
    
        
    
#search button logic



    


TitleLabel = Label(root, text="Frisco File Processing", fg = "black", font = "Arial 20 bold")
TitleLabel.pack(side = TOP)

PathLabel = Label(root, text="Path", fg = "black", font = "Arial 15").place(x = 40,y= 70)

SearchButton = Button(root, text = "Search", command = SearchFunc).place(x = 600,y = 70)
SearchButton = Entry(root, width = 15)

#labels, buttons, etc.



root.mainloop() #runs program




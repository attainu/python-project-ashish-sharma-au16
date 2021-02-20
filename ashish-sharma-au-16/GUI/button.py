from tkinter import * 
from tkinter.ttk import *
  
# creates a Tk() object 
master = Tk() 
  
# sets the geometry of main  
# root window 
master.geometry("500x500") 
  

def openEntry():
    
    openEntry = Toplevel(master)
    openEntry.title("PARK STASH PVT. LTD.")
    openEntry.geometry("500 * 500")
    openEntry.config(background="lightgreen")
    label2= Label(openEntry, text= "enter").grid(row=0)
    e1 = Entry(openEntry)
    e1.grid(row=0, column=1)
    #label2.pack(pady = 10)
#command class package commands ui entities folders for file
def openNewWindow(): 
      
    newWindow = Toplevel(master) 
  
    newWindow.title("PARK STASH PVT. LTD.") 
  
  
    newWindow.geometry("500x500") 
  
    newWindow.config(background="lightblue")
    label1 = Label(newWindow,  
              text ="ON ROUTE TO YOUR PARKING LOT")

    label1.config(background="lightgreen")
    label1.pack(pady = 10) 
    btn2 = Button(newWindow,  
             text ="Provide",command= openEntry)
    
    btn2.pack(pady=10)
    Label(newWindow,  
          text ="Provide No of Slots Required").pack() 


master.title("PARK STASH PVT. LTD.") 

master.config(background='lightblue')  
label = Label(master,  
              text ="CREATE A PARKING LOT") 
label.config(background='lightgreen') 

  
label.pack(pady = 10) 
  
btn = Button(master,  
             text ="Create Parking Lot",  
             command = openNewWindow) 
btn.pack(pady = 10) 
  

mainloop() 
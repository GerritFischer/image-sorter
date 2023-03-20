import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import filedialog
import shutil
import os
img_list = []
path_list = []


 


root = tk.Tk()
root.title("Image Sorter")
root.geometry("1280x720")




path = ""
movePath = ""

imageLabel = ttk.Label(root, width=100)
imageLabel.pack(side="left")

counter = 0
def updateImage():
    global counter
    counter += 1
    try:
        imageLabel.configure(image=img_list[counter])
    except:
        resetProgram()

        
        

def keep():

    updateImage()

def move():
     global counter
     global movePath
     mPath = movePath + str(counter) + "." + path_list[counter].split(".")[-1]
     while os.path.isfile(mPath):
           mPath = mPath.split(".")
           print(mPath)
           mPath.insert(-1, "1")
           print(mPath)
           mPath = ".".join(mPath)

     print(mPath)  
     shutil.move(path_list[counter], mPath)
     updateImage()

def loadDirectory():
    for f in os.listdir(path):
        if f.endswith(".jpg") or f.endswith(".png") or f.endswith(".webp") or f.endswith(".jpeg"):
            img_list.append(ImageTk.PhotoImage(Image.open(os.path.join(path, f)).resize((640,720))))
            path_list.append(os.path.join(path, f))
        
    if len(img_list) < 1:
        open_popup("Keine Bilder", "Es gibt keine Bilder in diesem Ordner")
    else:
        imageLabel.configure(image=img_list[0])
        moveButton.configure(state="normal")
        keepButton.configure(state="normal")

    

def enableLoadButton():
    global path
    global movePath
    if path != "" and movePath != "" and path != "/" and movePath != "/" :
        loadDictButton.configure(state="normal")


def selectPath():
     global path
     path = filedialog.askdirectory() + "/"
     pathLabel.configure(text="Path: " + path)
     enableLoadButton()
     
def selectMove():
     global movePath 
     movePath = filedialog.askdirectory()  + "/"
     moveLabel.configure(text="MovePath: " + movePath)
     enableLoadButton()
def open_popup(title, text):
   top= tk.Toplevel(root)
   top.geometry("200x200")
   top.title(title)
   ttk.Label(top, text=text, font=('Mistral 18 bold')).place(x=10,y=10)

def resetProgram():
    global img_list
    global path_list
    open_popup("Done", "Done")
    imageLabel.configure(image="")
    global counter
    counter = 0
    img_list = list()
    path_list = list()
    moveButton.configure(state="disabled")
    keepButton.configure(state="disabled")

def onKeyPress(event):
    if event.char == "q":
        keep()
    elif event.char == "e":
        move()

#testdir = filedialog.askdirectory()
#print(testdir)
moveLabel = ttk.Label(text="MovePath:  ", font=('Mistral 18 bold'))
moveLabel.pack(side="bottom",expand=True, fill="x")
pathLabel = ttk.Label(text="Path: ", font=('Mistral 18 bold'))
pathLabel.pack(side="bottom", expand=True, fill="x")

loadDictButton = ttk.Button(text="Load Directory", command=loadDirectory, state="disabled")
loadDictButton.pack(expand=True, fill="both")
selectPathButton = ttk.Button(text="Select Path", command=selectPath)
selectPathButton.pack(expand=True, fill="both")
selectMoveButton = ttk.Button(text="Select Move Path", command=selectMove)
selectMoveButton.pack(expand=True, fill="both")
keepButton = ttk.Button(root, text="Keep", command=keep, state="disabled")
keepButton.pack(expand=True, fill="both")
moveButton = ttk.Button(root, text="Move", command=move, state="disabled")
moveButton.pack(expand=True, fill="both")

root.bind('<KeyPress>', onKeyPress)
root.mainloop()



from tkinter import *
from PIL import ImageTk, Image
import os
import shutil
from tkinter import ttk #keyboard link
import tkinter.messagebox
import tkinter.filedialog
from tkinter import filedialog
import numpy as np
import scipy.misc
import pathlib
import copy


ned, Saving now...
Total  NB02  files: 100
Aligned, Saving now...
Total  NB03  files: 142
Aligned, Saving now...
Total  NB04  files: 100
Aligned, Saving now...
Total  NB05  files: 100
Aligned, Saving now...
Total  NB06  files: 100
Aligned, Saving now...
Total  NB07  files: 100
Aligned, Saving now...
Total  NB08  files: 100
Aligned, Saving now...
Run Time:  5.262819021949993 Mins
(base) adithya@Savitr:~/Desktop/Sun/SUIT_work/SUIT_Flares/Jun1$ /bin/python3 /home/adithya/Desktop/Sun/SUIT_work/SUIT_Flares/Jun1/ROI_Align_Movies.py
Total  NB01  files: 100
Aligned, Saving now...
Total  NB02  files: 100
Aligned, Saving now...
Total  NB03  files: 142
Aligned, Saving now...
Total  NB04  files: 100
Aligned, Saving now...
Total  NB05  files: 100
Aligned, Saving now...
Total  NB06  files: 100
Aligned, Saving now...
Total  NB07  files: 100
Aligned, Saving now...
Total  NB08  files: 100
Aligned, Saving now...
Run Time:  7.522663443966667 Mi
    global currImageIndex



    global imgLabel
    currImageIndex += 1
    filename.delete("1.0","end")
    filecount.delete("1.0","end")

    imgLabel.grid_forget()
    img = ImageTk.PhotoImage(Image.open(picturesList[currImageIndex]).resize((500, 500)))
    filecount.insert(END,currImageIndex)
    filecount.insert(END,'/')
    filecount.insert(END,len(picturesList))
    filename.insert(END,picturesList[currImageIndex])
    
    current_img = img
    imgLabel = Label(root,image=img)
    imgLabel.grid(row=8,column=1)



dummyInp=1   #Nothing to with mouse click need an extra argument
def moveBackward(event):
    global current_img
    global currImageIndex
    global imgLabel
    currImageIndex -= 1
    filename.delete("1.0","end")
    filecount.delete("1.0","end")

    imgLabel.grid_forget()
    

    img = ImageTk.PhotoImage(Image.open(picturesList[currImageIndex]).resize((500, 500)))
    filecount.insert(END,currImageIndex)
    filecount.insert(END,'/')
    filecount.insert(END,len(picturesList))
    filename.insert(END,picturesList[currImageIndex])
    current_img = img
    imgLabel = Label(root,image=img)
    imgLabel.grid(row=8,column=1)    
    

   

def moveImg(event):
    global current_img
    global currImageIndex
    print(picturesList[currImageIndex])
    destination='Moved_imgs'
    shutil.move(picturesList[currImageIndex], destination)
    
def moveBackImg(event):
    global current_img
    global currImageIndex
    #print(Pic_list[currImageIndex])
    imgPath=Pic_list[currImageIndex]
    pathSplits=imgPath.split(os.sep)
    #print(pathSplits)
    #print(pathSplits[-1])
    pathSplits.insert(-1,'Moved_imgs')
    mv_img_loc_=os.sep.join(pathSplits)
    print(mv_img_loc_)
    #destination='/home/adithyahn/Desktop/'
    shutil.move(mv_img_loc_ ,picturesList[currImageIndex])   
    print('Moved back')
    
#print(os. getcwd())
pathlib.Path("Moved_imgs").mkdir(parents=True, exist_ok=True)
picturesList = []

#Here is the variable where the reference will be stored
current_img = None
for pictures in os.listdir(os. getcwd()):
    if pictures.endswith('jpg'):
        picturesList.append(os. getcwd()+'/'+pictures)

picturesList.sort()
Pic_list=copy.deepcopy(picturesList)
currImageIndex = 0

root = Tk()
root.title('XRT Image filter')
#root['bg']='black'


menu1=Menu(root)
root.config(menu=menu1)
subMenu=Menu(menu1)
menu1.add_cascade(label='File',menu=subMenu)
subMenu.add_command(label='New Project',command=myCommand)
subMenu.add_command(label='Open',command=file_open)
subMenu.add_separator()
subMenu.add_command(label='Exit',command=exitButton)


menu2=Menu(menu1)
menu1.add_cascade(label='Edit',menu=menu2)
menu2.add_command(label='Costamize Run code',command=myCommand)

menu3=Menu(menu1)
menu1.add_cascade(label='Help',menu=menu3)
menu3.add_command(label='Guide doc',command=test)
menu3.add_command(label='Contact Author',command=test)

toolFrame=Frame(root,bg='Ivory2')


toolButton4=Button(toolFrame,text='Move Image',command=moveImg)
toolButton4.grid(row=0,column=0)
toolButton4=Button(toolFrame,text='Mv Back',command=moveBackImg)
toolButton4.grid(row=0,column=1)
toolButton4=Button(toolFrame,text='Analyse',command=test)
toolButton4.grid(row=0,column=2)
toolButton3=Button(toolFrame,text='Quit',command=toolFrame.quit,fg='red')
toolButton3.grid(row=0,column=3)
toolFrame.grid(row=0,column=1)


#WorkFlow=Frame(root,width=800, height=10,bg='Ivory').grid(row=1,column=1)#place(x=5,y=40)#.pack(side=TOP)

filename = Text(root, height = 2, width = 65, bg = "light yellow")
filename.grid(row=2,column=1)

filecount = Text(root, height = 1, width = 10, bg = "light cyan")
filecount.grid(row=2,column=0)

statusBar=Label(root,text='Version N0.1.0',bg='Ivory2',fg='thistle3',bd=1,relief=SUNKEN,anchor=W).grid(row=10,column=0)

img = ImageTk.PhotoImage(Image.open(picturesList[0]).resize((500, 500)))
imgLabel = Label(image=img)
imgLabel.grid(row=8,column=1)

#backwardImg = ImageTk.PhotoImage(Image.open("/home/adithyahn/Desktop/XRT/GUI/left.ico").resize((40, 40), Image.ANTIALIAS))
#backButton = Button(image=backwardImg,width=80,height=80,relief=FLAT,command=moveBackward)
backButton=Button(text='<<',command=moveBackward,fg='Blue')
backButton.bind("<Button-1>", moveBackward)
backButton.grid(row=8,column=0)


#forwardImg = ImageTk.PhotoImage(Image.open("/home/adithyahn/Desktop/XRT/GUI/right.ico").resize((40, 40), Image.ANTIALIAS))
#forwardButton = Button(image=forwardImg, width=80, height=80, relief=FLAT, command=moveForward)
forwardButton=Button(text='>>',command=moveForward,fg='Blue')
#forwardButton.bind("<Button-1>", moveForward)
forwardButton.grid(row=8,column=2)

#toolButton4.bind("<Shift-Z>",moveImg)
root.bind("<Left>",moveBackward)

root.bind("<Right>",moveForward)
root.bind("<Button-1>",moveForward)
root.bind("<q>",moveImg)
root.bind("<w>",moveBackImg)
root.bind("<i>",inpu_val_button)

#photo=PhotoImage(file='Untitled 2.png')
#frame1=Frame(root,bg='Ivory2',width=500, height=500)
#frame2=Frame(root).grid(row=0,column=0)
#frame1.grid(row=3, column=1)#pack(side=TOP,side=LEFT)


root.mainloop()







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

def myCommand():
    print("I can just print")


def test():
    print("I can just print")


def printit():
    printLabel = Label(WorkFlow, text='calcium').place(x=0, y=40)


def printit1():
    printLabel = Label(WorkFlow, text='Single image').place(x=60, y=40)


def printit2():
    printLabel = Label(WorkFlow, text='Result image').place(x=560, y=40)


def run():
    #import singleImageProcessor
    image = Image.open('Ca.jpg')  # to
    img = image.resize((400, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)  # jpg file from PIL library
    Pholabel1 = Label(frame2, image=photo)
    Pholabel1.image = photo  # refferece needed by packeage PIL
    Pholabel1.pack(side=LEFT)  # .place(x=200,y=40)
    g = printit2()


def exitButton():
    m = tkinter.messagebox.askyesno(title='Exit', message='Do you want to exit..?')
    if m == 1:
        root.destroy()


def file_open():
    global filename
    pt = browse_button()  # to get folder path
    file1 = tkinter.filedialog.askopenfilename(initialdir=folder_path, title="Select file", filetypes=(
    (".fits", ".fits.gz"), (".fits", ".fits"), ("all files", "*.*")))
    filename = file1
    FitsFile = fits.open(file1)
    ImgM = FitsFile[0].data
    imC = ((ImgM / 255)).astype(np.uint8)
    scipy.misc.imsave('fitsImg.jpg', imC[::-1])
    image = Image.open('fitsImg.jpg')  # to
    img = image.resize((400, 400), Image.ANTIALIAS)
    photo = ImageTk.PhotoImage(img)  # jpg file from PIL library
    Pholabel1 = Label(frame2, image=photo)
    Pholabel1.image = photo  # refferece needed by packeage PIL
    Pholabel1.pack(side=LEFT)  # .place(x=200,y=40)
    a = printit1()
    f = open('temp.txt', 'w+')
    f.write(filename)
    f.close()


def browse_button():
    global folder_path
    filename = tkinter.filedialog.askdirectory()
    folder_path = (filename)
    # print(filename)


def exitWindow():
    root.destroy()


def mode_button():
    modeWindow = Tk()
    modeWindow.title('Mode of Operation')
    modeButton1 = Button(modeWindow, text='White Light Images', command=exitWindow).pack()
    modeButton2 = Button(modeWindow, text='Calicium Light Images', command=printit).pack()
    modeButton3 = Button(modeWindow, text='Coronal  Images').pack()
    # modeWindow.mainloop()
def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename


def moveForward():
    global current_img
    global currImageIndex
    global imgLabel
    currImageIndex += 1
    filename.delete("1.0","end")
    filecount.delete("1.0","end")

    imgLabel.grid_forget()
    #print(picturesList)
    img = ImageTk.PhotoImage(Image.open(picturesList[currImageIndex]).resize((500, 500), Image.ANTIALIAS))
    filecount.insert(END,currImageIndex)
    filecount.insert(END,'/')
    filecount.insert(END,len(picturesList))
    filename.insert(END,picturesList[currImageIndex])
    
    current_img = img
    imgLabel = Label(frame1,image=img)
    imgLabel.grid(row=3,column=1)
    
    
def moveBackward():
    global current_img
    global currImageIndex
    global imgLabel
    currImageIndex -= 1
    filename.delete("1.0","end")
    filecount.delete("1.0","end")

    imgLabel.grid_forget()
    picturesList.sort()
    img = ImageTk.PhotoImage(Image.open(picturesList[currImageIndex]).resize((500, 500), Image.ANTIALIAS))
    filecount.insert(END,currImageIndex)
    filecount.insert(END,'/')
    filecount.insert(END,len(picturesList))
    filename.insert(END,picturesList[currImageIndex])
    current_img = img
    imgLabel = Label(frame1,image=img)
    imgLabel.grid(row=3,column=1)    
    
    

def moveImg():
    global current_img
    global currImageIndex
    print(picturesList[currImageIndex])
    destination='/home/adithyahn/Desktop/XRT/XBP/5_XBP/Al_rm_imgs'
    dest = shutil.move(picturesList[currImageIndex], destination)
    
def moveBackImg():
    global current_img
    global currImageIndex
    print(picturesList[currImageIndex])
    imgPath=picturesList[currImageIndex]
    pathSplits=imgPath.split(os.sep)
    print(pathSplits)
    print(pathSplits[-1])
    #destination='/home/adithyahn/Desktop/'
    #dest = shutil.move(picturesList[currImageIndex], destination)   

def openfn():
    filename = filedialog.askopenfilename(title='open')
    return filename

def open_img():
    x = openfn()
    pthLen=len(x.split(os.sep))-1
    firstImgPth=(x.split(os.sep))[0:pthLen]
    rootPth="/"
    endPth=""
    #print(os.path.join(endPth,rootPth))
    imgDir=os.path.join(rootPth,*firstImgPth,endPth)
    #print(imgDir.extend('/'))
    img = Image.open(x)
    img = img.resize((450, 450), Image.ANTIALIAS)
    img = ImageTk.PhotoImage(img)
    imgLabel = Label(frame1, image=img)
    imgLabel.image = img
    imgLabel.grid(row=3,column=1)#pack(side=LEFT,fill=X)
    global picturesList
    picturesList = []
    current_img = None
    print(imgDir)
    for pictures in os.listdir(imgDir):
        if pictures.endswith('jpg'):
            picturesList.append(imgDir+pictures)
    




currImageIndex = 0

root = Tk()
root.title('XRT Database')
root.geometry("1245x556")


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

toolButton4=Button(toolFrame,text='Load Data',command=open_img)
toolButton4.grid(row=0,column=0)
toolButton4=Button(toolFrame,text='Move Image',command=moveImg)
toolButton4.grid(row=0,column=1)
toolButton4=Button(toolFrame,text='Mv Back',command=moveBackImg)
toolButton4.grid(row=0,column=2)
toolButton4=Button(toolFrame,text='Analyse',command=test)
toolButton4.grid(row=0,column=3)
toolButton3=Button(toolFrame,text='Quit',command=toolFrame.quit,fg='red')
toolButton3.grid(row=0,column=4)
toolFrame.grid(row=0,column=1)


#WorkFlow=Frame(root,width=800, height=10,bg='Ivory').grid(row=1,column=1)#place(x=5,y=40)#.pack(side=TOP)

filename = Text(root, height = 2, width = 65, bg = "light yellow")
filename.grid(row=2,column=1)

filecount = Text(root, height = 1, width = 10, bg = "light cyan")
filecount.grid(row=2,column=0)



'''
dataD2 = Text(root, height = 1, width = 8, bg = "light cyan")
dataD2.grid(row=3,column=5)
dataD3 = Text(root, height = 1, width = 8, bg = "light cyan")
dataD3.grid(row=3,column=6)
dataD4 = Text(root, height = 1, width = 8, bg = "light cyan")
dataD4.grid(row=3,column=7)
dataD5 = Text(root, height = 1, width = 8, bg = "light cyan")
dataD5.grid(row=3,column=8)
dataD1 = Text(root, height = 1, width = 8, bg = "light cyan")
dataD1.grid(row=4,column=4)
'''


#img = ImageTk.PhotoImage(open_img().resize((500, 500), Image.ANTIALIAS))
#imgLabel = Label(image=img)
#imgLabel.grid(row=3,column=1)



backwardImg = ImageTk.PhotoImage(Image.open("/home/adithyahn/Desktop/XRT/GUI/left.ico").resize((40, 40)))
backButton = Button(image=backwardImg,width=80,height=80,relief=FLAT,command=moveBackward)
backButton.grid(row=3,column=0)


forwardImg = ImageTk.PhotoImage(Image.open("/home/adithyahn/Desktop/XRT/GUI/right.ico").resize((40, 40)))
forwardButton = Button(image=forwardImg, width=80, height=80, relief=FLAT, command=moveForward)
forwardButton.grid(row=3,column=2)

#toolButton4.bind("<Shift-Z>",moveImg)
root.bind("<Left>",moveBackward)
root.bind("<Right>",moveForward)
#root.bind("<Button-1>",moveForward)
root.bind("<q>",moveImg)
#root.bind("<w>",moveBackImg)

#photo=PhotoImage(file='Untitled 2.png')
frame1=Frame(root,bg='Ivory2',width=500, height=450)
frame1.grid(row=3, column=1)#pack(side=TOP,side=LEFT)
imgLabel = Label(frame1)

frame2=Frame(root,bg='Ivory2',width=500, height=300)
frame2.grid(row=3, column=4)#pack(side=TOP,side=LEFT)
imgLabel = Label(frame2)



frame3=Frame(frame2,bg='Ivory1',width=500, height=100)
frame3.grid(row=8, column=4,padx=4,pady=4)#pack(side=TOP,side=LEFT)
imgLabel = Label(frame3)
#frame3.Text(300, 50, text="HELLO WORLD", fill="black", font=('Helvetica 15 bold'))
#frame3.pack()

Dataprint = Text(frame3, height = 20, width = 65, bg = "light yellow")
Dataprint.grid(row=1,column=1)

frame4=Frame(frame2,bg="Ivory4",width=500, height=70)
frame4.grid(row=9, column=4,padx=4,pady=4)#pack(side=TOP,side=LEFT)
imgLabel = Label(frame4)

#dataD1 = Text(frame3, height = 1, width = 8, bg = "light cyan")
#dataD1.grid(row=1,column=4)

statusBar=Label(root,text='Version No.1.1',bg='Ivory2',fg='thistle3',bd=1,relief=SUNKEN,anchor=W).grid(row=12,column=0)
root.mainloop()





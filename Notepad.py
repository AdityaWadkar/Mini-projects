from tkinter import *
import os
import tkinter.messagebox as t
from tkinter.filedialog import askopenfilename,asksaveasfilename
import webbrowser
def newfile():
    global file
    root.title("Untitled-Notepad")
    file=None
    textarea.delete(1.0,END)
def openfile():
    file=askopenfilename(defaultextension=".text",filetypes=[("All Files","*.*"),("Text Documents","*.text")])
    if file=="":
        file=None
    else:
        root.title(os.path.basename(file)+"- Notepad")
        textarea.delete(1.0,END)
        f=open(file,"r")
        textarea.insert(1.0,f.read())

def savefile():
    global file
    if file ==None:
        file=asksaveasfilename(initialfile="Untitled.txt",
                               defaultextension=".text",
                               filetypes=[("All Files","*.*"),("Text Documents","*.text")])
    if file=="":
        file=None
    else:
        #save as new file
        f=open(file,"w")
        f.write(textarea.get(1.0,END))
        f.close()
        root.title(os.path.basename(file)+" - Notepad")
def quitfile():
    root.destroy()
def copy():
    textarea.event_generate("<<Copy>>")
def cut():
    textarea.event_generate("<<Cut>>")
def paste():
    textarea.event_generate("<<Paste>>")
def delete():
    textarea.event_generate("<<Delete>>")
def select_all():
    textarea.event_generate("<<SelectAll>>")
def undo():
    textarea.event_generate("<<Undo>>")
def help1():
    webbrowser.open("https://www.bing.com/search?q=get+help+with+notepad+in+windows+10&filters=guid:%224466414-en-dia%22%20lang:%22en%22&form=T00032&ocid=HelpPane-BingIA")
def about():
    t.showinfo("Notepad","Created By Aditya")
def white():
    textarea.config(background="white")
def grey():
    textarea.config(background="darkgrey")
def brown():
    textarea.config(background="Chocolate")
def red():
    textarea.config(background="orangered")
def yellow():
    textarea.config(background="gold")
def green():
    textarea.config(background="palegreen")
def whitetext():
    textarea.config(fg="white")
def greytext():
    textarea.config(fg="darkgrey")
def browntext():
    textarea.config(fg="Chocolate")
def yellowtext():
    textarea.config(fg="gold")
def redtext():
    textarea.config(fg="orangered")
def greentext():
    textarea.config(fg="palegreen")
def bluetext():
    textarea.config(fg="dodgerblue")
def zoomin():
    global a
    textarea.config(font=f"lucida {a+5}")
    a=a+5
def zoomout():
    global a
    textarea.config(font=f"lucida {a - 5}")
    a = a-5
if __name__ == '__main__':
    root =Tk()
    root.title("Notepad")
    root.geometry("600x400")
    a=13
    textarea=Text(root,font=f'lucida {a}')
    textarea.config(background="white",foreground="black")
    textarea.pack(expand=True,fill=BOTH)
    file =None

    #Menubar
    menubar=Menu(root,tearoff=0)
    menubar.config(bg = "GREEN",fg='white',activebackground='red',activeforeground='pink',relief=SUNKEN,selectcolor="yellow")
    # To add new filemenu
    filemenu=Menu(menubar,tearoff=0)
    #List in file menu
    filemenu.add_command(label="New            ",command=newfile)
    filemenu.add_command(label="Open",command=openfile)
    filemenu.add_command(label="Save",command=savefile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit",command=quitfile)
    menubar.add_cascade(label='File',menu=filemenu)

    #New Edit menu
    editmenu=Menu(menubar,tearoff=0,selectcolor="yellow")
    #list in edit menu
    editmenu.add_command(label="Copy           Ctrl+C",command=copy)
    editmenu.add_command(label="Cut              Ctrl+X",command=cut)
    editmenu.add_command(label="Paste           Ctrl+V",command=paste)
    editmenu.add_separator()
    editmenu.add_command(label="Delete",command=delete)
    editmenu.add_command(label="select All    Ctrl+A",command=select_all)
    editmenu.add_command(label="Undo",command=undo)
    menubar.add_cascade(label="Edit",menu=editmenu)

    # New Theme menu
    # editmenu = Menu(menubar, tearoff=0)
    # list in edit menu
    # menubar.add_cascade(label="Theme", menu=editmenu)
    # Submenu 1
    submenu1=Menu(menubar,tearoff=0)
    submenu1.add_command(label="White", command=white)
    submenu1.add_command(label="grey", command=grey)
    submenu1.add_command(label="Brown", command=brown)
    submenu1.add_command(label="Yellow", command=yellow)
    submenu1.add_command(label="Red", command=red)
    submenu1.add_command(label="Green", command=green)
    menubar.add_cascade(label="Theme",menu=submenu1)

    # Submenu2
    submenu2 = Menu(menubar, tearoff=0)
    submenu2.add_command(label="White ", command=whitetext)
    submenu2.add_command(label="grey", command=greytext)
    submenu2.add_command(label="Brown", command=browntext)
    submenu2.add_command(label="Yellow", command=yellowtext)
    submenu2.add_command(label="Red", command=redtext)
    submenu2.add_command(label="Green", command=greentext)
    submenu2.add_command(label="Blue", command=bluetext)
    menubar.add_cascade(label="Text Colour", menu=submenu2)

    # submenu 3

    submenu3 = Menu(menubar, tearoff=0)
    submenu3.add_command(label="Zoom In", command=zoomin)
    submenu3.add_command(label="Zoom Out", command=zoomout)
    menubar.add_cascade(label="View", menu=submenu3)
    # editmenu.add_separator()
    # editmenu.add_command(label="Delete", command=delete)
    # editmenu.add_command(label="select All", command=select_all)
    # editmenu.add_command(label="Undo", command=undo)


    #New Help menu
    helpmenu=Menu(menubar,tearoff=0)
    helpmenu.add_command(label="View Help",command=help1)
    helpmenu.add_separator()
    helpmenu.add_command(label="About Noptepad",command=about)
    menubar.add_cascade(label="Help",menu=helpmenu)

    root.config(menu=menubar,relief=SUNKEN, bg="linen")

    # Adding Scrollabr
    scrollbar=Scrollbar(textarea)
    scrollbar.pack(side=RIGHT,fill=Y)
    scrollbar.config(command=textarea.yview)
    textarea.config(yscrollcommand=scrollbar.set)

    scrollbar = Scrollbar(textarea,orient=HORIZONTAL)
    scrollbar.pack(side=BOTTOM, fill=X)
    scrollbar.config(command=textarea.yview)
    textarea.config(xscrollcommand=scrollbar.set)

    # status bar
    sbar = Label(root, relief=SUNKEN, anchor="w")
    sbar.config(relief=SUNKEN, bg="linen")
    sbar.pack(side=BOTTOM, fill=X)

    root.mainloop()
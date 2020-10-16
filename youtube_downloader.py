'''
from pip._internal import main as pipmain
pipmain(['install', 'pytube3'])
'''
from tkinter import *
from pytube import YouTube
from tkinter import messagebox
root=Tk()
root.title("Video Downloader")
root.geometry("400x400")

linklabel = Label(root,text="Link")
linklabel.grid(row=0,column=0)
linkentry = Entry(root)
linkentry.grid(row=0,column=1)
#link=str(linkentry.get())

pathlabel = Label(root,text="Path")
pathlabel.grid(row=1,column=0)
pathentry = Entry(root)
pathentry.grid(row=1,column=1)
#path = str(pathentry.get())

def click():
    link = linkentry.get()
    path = pathentry.get()
    try:
        yt = YouTube(link)
        stream = yt.streams.first()
    except: 
        messagebox.showerror("Error","Invalid link entered")
        response=messagebox.askyesno("Choose an option","Retry?")
        if response == 1:
            linkentry.delete(0,END)
            pathentry.delete(0,END)
        else:
            quit()

    try:
        stream.download(path)
        messagebox.showinfo("Confirmation","Your video was downloaded in "+path)
    except:
        path ="D:/"
        stream.download(path)
        messagebox.showinfo("Confirmation","Invalid path, Video was downloaded in "+path)
    quit()
button = Button(root,text="Download",command=click)
button.grid(row=2,column=0)
#root.mainloop()

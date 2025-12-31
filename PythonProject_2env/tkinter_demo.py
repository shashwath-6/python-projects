import tkinter

print(tkinter.TkVersion)
print(tkinter.TclVersion)

mainWindow = tkinter.Tk()
mainWindow.title("Hello World")
mainWindow.geometry("900x1080")

a=tkinter.Label(mainWindow,text="Hello World")
a.pack()

b = tkinter.Canvas(mainWindow, relief="raised", borderwidth=2)
b.pack(side="top")

mainWindow.mainloop()
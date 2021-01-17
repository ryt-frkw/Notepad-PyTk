import tkinter as tk

def function():
    global num
    num += 1
    var.set(str(num))

root = tk.Tk()
root.geometry("70x70")
root.title("Tk")

cv = tk.Canvas(root, width=400, height=400)
cv.pack()

num = 0
var = tk.StringVar()
var.set(str(num))

lab = tk.Label(cv, textvariable=var)
lab.pack()

but = tk.Button(cv, text="Button", command=function)
but.pack()


root.mainloop()

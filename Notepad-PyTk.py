import os
import sys
import json
import platform
import tkinter as tk
import tkinter.font as font
from tkinter import filedialog
import tkinter.ttk as ttk
from tkinter.scrolledtext import ScrolledText
import datetime
import webbrowser

root = tk.Tk()
now = datetime.datetime.now()
root.title("Untitled - Notepad-PyTk")
root.geometry("1250x750")


json_open = open('./files/config.json', 'r')
json_load = json.load(json_open)

fore = json_load['Color']['foreground-color']
back = json_load['Color']['background-color']
cursor = json_load['Color']['cursor-color']

font_family = json_load['Font']['font-family']
font_size = json_load['Font']['font-size']

dialogop = json_load['Open_Filedialog']['dialog']
dialogsa = json_load['Save_Filedialog']['dialog']

temp1 = json_load['Template']['template1-menu']
temp2 = json_load['Template']['template2-menu']
temp3 = json_load['Template']['template3-menu']
temp4 = json_load['Template']['template4-menu']
temp5 = json_load['Template']['template5-menu']
temp_load1 = json_load['Template']['template1-filename']
temp_load2 = json_load['Template']['template2-filename']
temp_load3 = json_load['Template']['template3-filename']
temp_load4 = json_load['Template']['template4-filename']
temp_load5 = json_load['Template']['template5-filename']

lang = json_load['Language']['Language']
if lang == "Japanese":
    WIN_TITLE = "Notepad-PyTk"
    M_FILE = "ファイル(F)"
    M_EDIT = "編集(E)"
    M_TEMP = "テンプレート(T)"
    M_HELP = "ヘルプ(H)"

    M_NEW = "新規作成"
    M_OPEN = "開く(O)..."
    M_SAVEAS = "名前をつけて保存(A)..."
    M_EXIT = "アプリケーションの終了"
    M_CUT = "カット"
    M_COPY = "コピー"
    M_PASTE = "ペースト"
    M_COPYRIGHT = "著作権表記"
    M_TIMEDATE = "日付と時間"
    M_APPSETTINGS = "アプリ設定(A)"
    M_SENDFEED = "フィードバックを送信"
    M_GOGITHUB = "GitHubページを表示"
    M_ABOUT = "このアプリケーションについて"
else:
    WIN_TITLE = "Notepad-PyTk"
    M_FILE = "File"
    M_EDIT = "Edit"
    M_TEMP = "Template"
    M_SETTINGS = "Settings"
    M_HELP = "Help"

    M_NEW = "New"
    M_OPEN = "Open..."
    M_SAVEAS = "Save As..."
    M_EXIT = "Exit"
    M_CUT = "Cut"
    M_COPY = "Copy"
    M_PASTE = "Paste"
    M_COPYRIGHT = "Copyright"
    M_TIMEDATE = "Time/Date"
    M_SENDFEED = "Send feedback"
    M_GOGITHUB = "View GitHub page"
    M_ABOUT = "About - Notepad-PyTk"


main_font = font.Font(root, family=font_family, size=font_size)
__version__ = (1, 0, "b")
root.tk.call('wm', 'iconphoto', root._w, tk.PhotoImage(file='./files/Notepad-PyTk.gif'))


def sendfeed():
    url = "https://forms.gle/8wQ6wcHb2eKDNhzu5"
    webbrowser.open(url)

def gogithub():
    url = "https://github.com/ryt-frkw/Notepad-PyTk/"
    webbrowser.open(url)

def about():
    about.win = tk.Toplevel()
    about.win.geometry("400x300")
    about.win.title(M_ABOUT)
    about.win.tk.call('wm', 'iconphoto', about.win._w, tk.PhotoImage(file='./files/Notepad-PyTk.gif'))
    about.win.wait_visibility()
    about.win.grab_set()
    lab1 = tk.Label(about.win, text="Notepad-PyTk", font='Century')
    lab1.place(x=40, y=15)
    lab2 = tk.Label(about.win, text="License")
    lab2.place(x=40, y=45)
    txtbox = ScrolledText(about.win, width=45, height=10)
    txtbox.insert(tk.END, "MIT License\n\nCopyright (c) 2021 Ryota Furukawa.\n\nPermission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files(the \"Software\"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and / or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED \"AS IS\", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.")
    txtbox.configure(state='disabled')
    txtbox.place(x=40, y=70)
    py_version = '.'.join(platform.python_version_tuple())
    np_version = '.'.join([str(v) for v in __version__])
    os_version = platform.system() + str(platform.release())
    lab9 = tk.Label(about.win, text=f"Notepad-PyTk Version : {np_version}")
    lab9.place(x=40, y=210)
    lab10 = tk.Label(about.win, text=f"Python Version : {py_version}")
    lab10.place(x=40, y=230)
    lab11 = tk.Label(about.win, text=f"OS Version : {os_version}")
    lab11.place(x=40, y=250)
    about.win.resizable(0, 0)
    about.win.mainloop()

def new():
    root.title("Untitled - Notepad-PyTk")
    EDIT_TEXTBOX.delete(1.0, tk.END)

def savefile():
    textfile = filedialog.asksaveasfilename(initialfile='Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*")])
    text = EDIT_TEXTBOX.get('1.0', 'end -1c')
    root.title(os.path.basename(textfile) + " - Notepad-PyTk")
    asf = open(textfile, 'w', encoding='utf-8')
    asf.write(text)
    asf.close()

def openfile():
    typ = [('', '*')]
    dir = dialogop
    textfile = filedialog.askopenfilename(filetypes=typ, initialdir=dir)
    root.title(os.path.basename(textfile) + " - Notepad-PyTk")
    text_data = open(textfile, "r", encoding='utf-8')
    reads = text_data.read()
    EDIT_TEXTBOX.insert(tk.END, reads)
    text_data.close()

def tempopen1():
    opfile = json_load['Template']['template1-filename']
    text_data = open(opfile, "r", encoding='utf-8')
    reads = text_data.read()
    EDIT_TEXTBOX.insert(tk.END, reads)
    text_data.close()

def tempopen2():
    opfile = json_load['Template']['template2-filename']
    text_data = open(opfile, "r", encoding='utf-8')
    reads = text_data.read()
    EDIT_TEXTBOX.insert(tk.END, reads)
    text_data.close()

def tempopen3():
    opfile = json_load['Template']['template3-filename']
    text_data = open(opfile, "r", encoding='utf-8')
    reads = text_data.read()
    EDIT_TEXTBOX.insert(tk.END, reads)
    text_data.close()

def tempopen4():
    opfile = json_load['Template']['template4-filename']
    text_data = open(opfile, "r", encoding='utf-8')
    reads = text_data.read()
    EDIT_TEXTBOX.insert(tk.END, reads)
    text_data.close()

def tempopen5():
    opfile = json_load['Template']['template5-filename']
    text_data = open(opfile, "r", encoding='utf-8')
    reads = text_data.read()
    EDIT_TEXTBOX.insert(tk.END, reads)
    text_data.close()

def entercr():
    now = datetime.datetime.now()
    reads = 'Copyright (c) {0:%Y}'.format(now)
    EDIT_TEXTBOX.insert(tk.END, reads)

def timedate():
    now = datetime.datetime.now()
    reads = '{0:%I}:{0:%M} {0:%p} {0:%d}/{0:%m}/{0:%Y}'.format(now)
    EDIT_TEXTBOX.insert(tk.END, reads)


EDIT_TEXTBOX = tk.Text(root, wrap=tk.NONE, font=main_font, foreground=fore, background=back, insertbackground=cursor)
EDIT_TEXTBOX.grid(column=0, row=0, sticky=(tk.N, tk.S, tk.E, tk.W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)


scr_y = tk.Scrollbar(EDIT_TEXTBOX, command=EDIT_TEXTBOX.yview)
scr_x = tk.Scrollbar(EDIT_TEXTBOX, command=EDIT_TEXTBOX.xview, orient=tk.HORIZONTAL)
scr_y.pack(side=tk.RIGHT, fill="y")
scr_x.pack(side=tk.BOTTOM, fill="x")
EDIT_TEXTBOX['yscrollcommand'] = scr_y.set
EDIT_TEXTBOX['xscrollcommand'] = scr_x.set


menubar = tk.Menu(root)

filemenu = tk.Menu(menubar, tearoff=0)
filemenu.add_command(label=M_NEW, command=new)
filemenu.add_command(label=M_OPEN, command=openfile)
filemenu.add_command(label=M_SAVEAS, command=savefile)
filemenu.add_separator()
filemenu.add_command(label=M_EXIT, command=root.quit)
menubar.add_cascade(label=M_FILE, menu=filemenu)

editmenu = tk.Menu(menubar, tearoff=0)
editmenu.add_command(label=M_CUT, command=lambda: EDIT_TEXTBOX.event_generate("<<Cut>>"))
editmenu.add_command(label=M_COPY, command=lambda: EDIT_TEXTBOX.event_generate("<<Copy>>"))
editmenu.add_command(label=M_PASTE, command=lambda: EDIT_TEXTBOX.event_generate("<<Paste>>"))
editmenu.add_separator()
editmenu.add_command(label=M_COPYRIGHT, command=entercr)
editmenu.add_command(label=M_TIMEDATE, command=timedate)
menubar.add_cascade(label=M_EDIT, menu=editmenu)

templatemenu = tk.Menu(menubar, tearoff=0)
templatemenu.add_command(label=temp1, command=tempopen1)
templatemenu.add_command(label=temp2, command=tempopen2)
templatemenu.add_command(label=temp3, command=tempopen3)
templatemenu.add_command(label=temp4, command=tempopen4)
templatemenu.add_command(label=temp5, command=tempopen5)
menubar.add_cascade(label=M_TEMP, menu=templatemenu)

helpmenu = tk.Menu(menubar, tearoff=0)
helpmenu.add_command(label=M_SENDFEED, command=sendfeed)
helpmenu.add_command(label=M_GOGITHUB, command=gogithub)
helpmenu.add_separator()
helpmenu.add_command(label=M_ABOUT, command=about)
menubar.add_cascade(label=M_HELP, menu=helpmenu)


root.config(menu=menubar)
root.mainloop()

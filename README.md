# Notepad-PyTk
[Web(日本語)を参照する場合はクリックしてください。](https://ryt-frkw.github.io/Notepad-PyTk/)
## Overview
Notepad-PyTk is a simple text editor using Python Tkinter.

Notepad-PyTk has the ability to pre-save and load templates. You can save up to 5 templates for this feature.

You can also set the Notepad-PyTk font and font size, background and characters and cursors color, templates, and language in `./files/config.json`.

For more information on config.json, see Setting method.

## Licence
MIT Licence

## Operating environment

Files in Python format work on Windows, Linux, and macOS environments.

Python3 is required to execute Python format files.

Also, exe format files can only be executed on Windows.

## Language
This software is available in English and Japanese.

## Execution method
Start a terminal or command prompt and enter the following command.

Windows environment

`python Notepad-PyTk.py`

Linux environment

`python3 Notepad-PyTk.py`

macOS environment

`python3 Notepad-PyTk.py`

Also, if you want to execute an exe format file for Windows, execute `Notepad-PyTk.exe`.

## Setting method
In order to set Notepad-PyTk, you need to edit `./files/config.json` directly.
### Language
To change the language to Japanese, use `./files/config.json`

`"Language": {`

`"Language": "English or Japanese"`

`},`

You need to change "English" to "Japanese".

### Color
Change the color in `./files/config.json`

`"Color": {`

`"foreground-color": "color-code to set",`

`"background-color": "color-code to set",`

`"cursor-color": "color-code to set"`

`},`

Can be set using the color code in the order of characters, background, and cursor.

### Font
To set the font family and font size, go to `./files/config.json`

`"Font": {`


`"font-family": "font family to set",`

`"font-size": font size to set`

`},`

It can be set with. Enter the font family in "font-family" and the font size in "font-size".

### Template
To set the template, use `./files/congif.json` to set the name to be displayed in the menu bar and the path under` ./template/`. In the initial state, 3 samples are set.

Save the template under `./template/`. Then edit `config.json` as per the example.

`"Template": {`

`"template1-menu": "String to display in the menu bar",`

`"template1-filename": "./template/filename to be template ",`

`...`

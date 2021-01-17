# Notepad-PyTk

## Overview
Notepad-PyTk is a simple text editor using Python Tkinter.

Notepad-PyTk has the ability to pre-save and load templates. You can save up to 5 templates for this feature.

You can also set the Notepad-PyTk font and font size, background color, characters and cursors, templates, and language in `./files/config.json.`

For more information on config.json, see Setting method.

## Licence
MIT Licence

## Operating environment
Works on Windows, Linux and macOS environments.

Python 3 is required to run.
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

____

# Notepad-PyTk(日本語版)

## 概要
Notepad-PyTk はPythonの標準GUIモジュールであるTkinterを使用したシンプルなテキストエディターです。

Notepad-PyTk には、テンプレートを事前に保存して読み込む機能があります。この機能用に最大5つのテンプレートを保存できます。

`./files/config.json` で、メモ帳-PyTkフォントとフォントサイズ、背景色、文字とカーソル、テンプレート、および言語を設定することもできます。

config.jsonの詳細については、「設定方法」を参照してください。

## ライセンス
MIT ライセンス

## 動作環境
Windows、Linux、macOS環境で動作します。

実行するにはPython3が必要です。

## 言語
このソフトウェアは英語と日本語が利用できます。

## 実行方法
ターミナルまたはコマンドプロンプトを起動し、次のコマンドを入力します。

Windows環境

`python Notepad-PyTk.py`

Linux環境

`python3 Notepad-PyTk.py`

macOS環境

`python3 Notepad-PyTk.py`

## 設定方法
Notepad-PyTk を設定するには、 `./files/config.json` を直接編集する必要があります。
### 言語
言語を日本語にするためには `./files/config.json` の

`"Language": {`

`"Language": "English または Japanese"`

`},`

の"English"を"Japanese"に変更する必要があります。

### カラー
色の変更は `./files/config.json` の

`"Color": {`

`"foreground-color": "設定するカラーコード",`

`"background-color": "設定するカラーコード",`

`"cursor-color": "設定するカラーコード"`

`},`

を、文字・バックグラウンド・カーソルの順でカラーコードを用いて設定できます。

### フォント
フォントファミリーやフォントサイズを設定するには `./files/config.json` の

`"Font": {`


`"font-family": "設定するフォントファミリー",`

`"font-size": 設定するフォントサイズ`

`},`

で設定できます。"font-family"にフォントファミリーを、"font-size"にフォントサイズを入力します。

### テンプレート
テンプレートを設定するには  `./files/congif.json` で メニューバーに表示する名称と `./template/` 以下のパスを設定します。初期状態では3つのサンプルが設定されています。

テンプレートは `./template/`以下に保存してください。そして例にそって `config.json` を編集してください。

`"Template": {`

`"template1-menu": "メニューバーに表示する文字列",`

`"template1-filename": "./template/テンプレートにするファイル名",`

`...`
____
### 2021 Ryota Furukawa.

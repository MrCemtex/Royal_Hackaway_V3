# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 07:51:09 2020

@author: marks
"""


from pynput import keyboard


COMBINATIONS = [
        {keyboard.KeyCode(char="a")},
        {keyboard.KeyCode(char="A")},
        {keyboard.KeyCode(char="b")},
        {keyboard.KeyCode(char="B")},
        {keyboard.KeyCode(char="c")},
        {keyboard.KeyCode(char="C")},
        {keyboard.KeyCode(char="d")},
        {keyboard.KeyCode(char="D")},
        {keyboard.KeyCode(char="e")},
        {keyboard.KeyCode(char="E")},
        {keyboard.KeyCode(char="f")},
        {keyboard.KeyCode(char="F")},
        {keyboard.KeyCode(char="g")},
        {keyboard.KeyCode(char="G")},
        {keyboard.KeyCode(char="h")},
        {keyboard.KeyCode(char="H")},
        {keyboard.KeyCode(char="i")},
        {keyboard.KeyCode(char="I")},
        {keyboard.KeyCode(char="j")},
        {keyboard.KeyCode(char="J")},
        {keyboard.KeyCode(char="k")},
        {keyboard.KeyCode(char="K")},
        {keyboard.KeyCode(char="l")},
        {keyboard.KeyCode(char="L")},
        {keyboard.KeyCode(char="m")},
        {keyboard.KeyCode(char="M")},
        {keyboard.KeyCode(char="o")},
        {keyboard.KeyCode(char="O")},
        {keyboard.KeyCode(char="p")},
        {keyboard.KeyCode(char="P")},
        {keyboard.KeyCode(char="q")},
        {keyboard.KeyCode(char="Q")},
        {keyboard.KeyCode(char="r")},
        {keyboard.KeyCode(char="R")},
        {keyboard.KeyCode(char="s")},
        {keyboard.KeyCode(char="S")},
        {keyboard.KeyCode(char="t")},
        {keyboard.KeyCode(char="T")},
        {keyboard.KeyCode(char="u")},
        {keyboard.KeyCode(char="U")},
        {keyboard.KeyCode(char="v")},
        {keyboard.KeyCode(char="V")},
        {keyboard.KeyCode(char="w")},
        {keyboard.KeyCode(char="W")},
        {keyboard.KeyCode(char="x")},
        {keyboard.KeyCode(char="X")},
        {keyboard.KeyCode(char="y")},
        {keyboard.KeyCode(char="Y")},
        {keyboard.KeyCode(char="z")},
        {keyboard.KeyCode(char="Z")},
        {keyboard.KeyCode(char="1")},
        {keyboard.KeyCode(char="2")},
        {keyboard.KeyCode(char="3")},
        {keyboard.KeyCode(char="4")},
        {keyboard.KeyCode(char="5")},
        {keyboard.KeyCode(char="6")},
        {keyboard.KeyCode(char="7")},
        {keyboard.KeyCode(char="8")},
        {keyboard.KeyCode(char="9")},
        {keyboard.KeyCode(char="0")},
        {keyboard.KeyCode(char="`")},
        {keyboard.KeyCode(char="¬")},
        {keyboard.KeyCode(char=",")},
        {keyboard.KeyCode(char="<")},
        {keyboard.KeyCode(char=".")},
        {keyboard.KeyCode(char=">")},
        {keyboard.KeyCode(char="/")},
        {keyboard.KeyCode(char="?")},
        {keyboard.KeyCode(char=";")},
        {keyboard.KeyCode(char=":")},
        {keyboard.KeyCode(char="'")},
        {keyboard.KeyCode(char="@")},
        {keyboard.KeyCode(char="[")},
        {keyboard.KeyCode(char="{")},
        {keyboard.KeyCode(char="]")},
        {keyboard.KeyCode(char="}")},
        {keyboard.KeyCode(char="!")},
        {keyboard.KeyCode(char='"')},
        {keyboard.KeyCode(char="£")},
        {keyboard.KeyCode(char="$")},
        {keyboard.KeyCode(char="%")},
        {keyboard.KeyCode(char="^")},
        {keyboard.KeyCode(char="&")},
        {keyboard.KeyCode(char="&")},
        {keyboard.KeyCode(char="*")},
        {keyboard.KeyCode(char="(")},
        {keyboard.KeyCode(char=")")},
        {keyboard.KeyCode(char="-")},
        {keyboard.KeyCode(char="_")},
        {keyboard.KeyCode(char="=")},
        {keyboard.KeyCode(char="+")},
        {keyboard.Key.enter},
        {keyboard.KeyCode(char="")},
        {keyboard.KeyCode(char="|")},
        {keyboard.KeyCode(char="#")},
        {keyboard.KeyCode(char="~")}
        ]

current = set()

code_text = ''
for i in range(1,7):
    fname = 'egcode' + str(i) + '.txt'
    with open(fname) as f:
        code_text += f.read() + '\n\n'
indx = 0

def execute():
    global indx
    if (indx+3) <= (len(code_text)):
        print(code_text[indx:indx+3], end='')
        indx += 3
    else:
        print(code_text[indx:len(code_text)])
        indx = 0
    
def on_press(key):
    if any([key in COMBO for COMBO in COMBINATIONS]):
        if key == keyboard.Key.enter:
            print("works enter")
        else:
            current.add(key)
            if any(all(k in current for k in COMBO)for COMBO in COMBINATIONS):
                execute()
        
def on_release(key):
    if key != keyboard.Key.enter:
        if any([key in COMBO for COMBO in COMBINATIONS]):
            current.remove(key)



with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
    
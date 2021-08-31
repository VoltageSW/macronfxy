#
# Programmed in 2021 by bariscodefx
#
# Copyright 2021 Voltage Software
#

import tkinter as tk
import pyautogui
from pynput import keyboard

class Program(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.macro_speed = 1
        self.macro_open = False
        self.master = master
        self.pack()
        self.create_widgets()
        self.keyboard_listener = keyboard.Listener(on_press=self.on_press_key)
        self.keyboard_listener.start()
        self.master.after(self.macro_speed, self.macro)

    def create_widgets(self):
        self.info_label = tk.Label(self.master, text="To run left click macro press the P key.")
        self.info_label.pack()
        
    def on_press_key(self, key):
        try:
            if(key.char == "p"):
                if(self.macro_open == True):
                    print("pressed p")
                    self.macro_open = False
                elif(self.macro_open == False):
                    self.macro_open = True
        except AttributeError:
            print("AttributeError")
            
    def macro(self):
        if(self.macro_open == True):
            pyautogui.click()
        self.master.after(self.macro_speed, self.macro)
#
# Programmed in 2021 by bariscodefx
#
# Copyright 2021 Voltage Software
#

import tkinter as tk
from Program import Program

root = tk.Tk()
app = Program(master=root)
app.master.title("macronfxy v1.0")
app.master.minsize(300,500)
app.master.maxsize(300,500)
app.mainloop()
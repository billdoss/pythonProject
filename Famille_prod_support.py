#! /usr/bin/env python
#
# Support module generated by PAGE version 4.9
# In conjunction with Tcl version 8.6
#    Aug 02, 2017 11:45:32 AM


import sys

try:
    from Tkinter import *
except ImportError:
    from tkinter import *

try:
    import ttk
    py3 = 0
except ImportError:
    import tkinter.ttk as ttk
    py3 = 1

def set_Tk_var():
    global heure
    heure = StringVar()
    global date
    date = StringVar()
    global code
    code = StringVar()
    global lib
    lib = StringVar()

def Valider(p1):
    print('Famille_prod_support.Valider')
    sys.stdout.flush()

def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import Famille_prod
    Famille_prod.vp_start_gui()



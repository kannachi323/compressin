import tkinter as tk
from tkinter import messagebox, Menu
from sys import platform
from osx_config import *
from program import *



def main(window):
    window.title("Compressin!")
    window.geometry("680x550")
    bkg = tk.PhotoImage(file="images/background.png")
    bkg_label = tk.Label(window, image=bkg)
    bkg_label.pack()

    if platform == "darwin":
        mac_placement(window)

    elif platform == "win32":
        win_placement(window)


    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    #create main window
    window = tk.Tk()

    #call main function
    main(window)







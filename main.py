import tkinter as tk
from sys import platform
from config import *
from program import *


def main():
    root = tk.Tk()
    root.title("Compressin!")
    root.geometry("680x550")
    bkg = tk.PhotoImage(file="ipv6-compress-aggregation/images/background.png")
    bkg_label = tk.Label(root, image=bkg)
    bkg_label.pack()
    root.resizable(False, False)


    if platform == "darwin":
        osx_placement(root)

    elif platform == "win32":
        win_placement(root)

    
    
    root.mainloop()


if __name__ == '__main__':
    main()





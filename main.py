import tkinter as tk
from tkinter import messagebox

#MENU options:
def ipv6_compression_window():
    window = tk.Toplevel()
    window.title("IPv6 Compression")
    return window

def route_aggregation_window():
    window = tk.Toplevel()
    window.title("Route Aggregation")
    return window

def exit_program():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit the program?"):
        window.destroy()

def main(window, w1, w2):
    menu_options = tk.Menu(w1)

    exit_b = tk.Button(window, text="Exit", command=exit_program)
    exit_b.pack()

    main_window.mainloop()

if __name__ == '__main__':
    window = tk.Tk()
    w1 = ipv6_compression_window()
    w2 = route_aggregation_window()
    main(window, w1, w2)




    


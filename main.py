import tkinter as tk
from tkinter import ttk, messagebox, Menu
from PIL import ImageTk, Image

import ipv6

#MENU options:
def ipv6_compression_window():
    ipv6_compress = tk.Toplevel()
    ipv6_compress.geometry("800x600")
    ipv6_compress.title("IPv6 Compression")
    return ipv6_compress

def ipv6_decompression_window():
    ipv6_decompress = tk.Toplevel()
    ipv6_decompress.geometry("800x600")
    ipv6_decompress.title("IPv6 Decompression")
    return ipv6_decompress

def route_aggregation_window():
    route = tk.Toplevel()
    route.geometry("800x600")
    route.title("Route Aggregation")
    return route

def exit_program():
    if messagebox.askokcancel("Exit", "Are you sure you want to exit the program?"):
        window.destroy()

def main(window):
    window.title("Compressin!")
    window.geometry("680x550")
    bkg = tk.PhotoImage(file="images/background.png")
    bkg_label = tk.Label(window, image=bkg)
    bkg_label.pack()
    
    #Menu Options
    menu_options = tk.Menu(window)
    filemenu = Menu(menu_options, tearoff=0)
    filemenu.add_command(label="IPv6 Compression", command=ipv6_compression_window)
    filemenu.add_separator()
    filemenu.add_command(label="Route Aggregation", command=route_aggregation_window)
    menu_options.add_cascade(label="File", menu=filemenu)
    

    #open ipv6 compression/route aggregation windows
    ipv6_compress = tk.Button(window, text="IPv6 Compression", width=16, height=8, borderwidth=1, command=ipv6_compression_window)
    ipv6_compress.place(x=65, y=45)
    ipv6_decompress = tk.Button(window, text="IPv6 Decompression", width=16, height=8, borderwidth=1, command=ipv6_decompression_window)
    ipv6_decompress.place(x=429, y=45)
    route = tk.Button(window, text="Route Aggregation", width=16, height=8, borderwidth=1, command=route_aggregation_window)
    route.place(x=242, y=366) 

    #Exit button
    exit_b = tk.Button(window, text="Exit", width=16, height=3, borderwidth=1, command=exit_program)
    


    window.config(menu=menu_options)
    window.resizable(False, False)
    window.mainloop()


if __name__ == '__main__':
    #create main window
    window = tk.Tk()

    #call main function
    main(window)







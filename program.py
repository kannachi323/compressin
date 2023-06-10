import tkinter as tk
from sys import platform
from config import *

current_window = None

def check_input_length(entry):
    pass

def remove_extra_colon(temp):
    pass
def compress(entry):
    pass

def compress_entry(window):
    # Create an entry box to get ipv6 addresses
    entry = tk.Text(window, height=5, width=40, highlightthickness=2)
    entry.place(x=200, y=300)
    compress_btn = tk.Button(window, text="Compress", command=lambda: compress(entry))
    compress_btn.place(x=200, y=400)

def decompress(window, entry, output):
    lines = entry.get("1.0", "end").strip().split("\n")
    if len(lines) > 50:
        print("Too many inputs! Maximum of 50 inputs exceeded!")
        pass
    else:
        for a, address in enumerate(lines):
            temp = address.replace(" ", '').split(":")
            
            #zero or discontinuous zero decompression
            if '' in temp:
                temp[temp.index('')] = "0"
                while len(temp) < 8:
                    temp.insert(temp.index("0"), "0")
            

            #leading zero decompression
            for b, bits in enumerate(temp):
                if len(bits) >= 1 and len(bits) < 4 and bits[0] != '0':
                    zeros = '0' * (4 - len(bits))
                    temp[b] = zeros + temp[b]
                if bits == "0":
                    temp[b] = temp[b].replace("0", "0000")

            lines[a] = ':'.join(temp)
        
        for line in lines:
            output.insert("1.0", f"{line}\n")
    
        
def decompress_entry(window):
    # Create an entry box to get ipv6 addresses
    entry = tk.Text(window, height=31, width=40, highlightthickness=1, highlightbackground="black")
    entry.place(x=5, y=0)
    compress_btn = tk.Button(window, text="Decompress", width=10, height=2, command=lambda: decompress(window, entry, output))
    compress_btn.place(x=120, y=506)
    output = tk.Text(window, height=31, width=40, highlightthickness=1, highlightbackground="black")
    output.place(x=348, y=0)
    main_menu_btn = tk.Button(window, text="Save/Exit", width=10, height=2, command=lambda: save_window())
    main_menu_btn.place(x=500, y=506)
    

#MENU options:
def ipv6_compression_window(window):
    ipv6_compress = tk.Toplevel(window)
    ipv6_compress.geometry("680x550")
    ipv6_compress.title("IPv6 Compression")
    ipv6_compress.resizable(False, False)
    compress_entry(ipv6_compress)
    
def ipv6_decompression_window(window):
    global current_window
    if current_window != None:
        reopen(current_window)
    else:
        ipv6_decompress = tk.Toplevel(window)
        ipv6_decompress.geometry("680x550")
        ipv6_decompress.title("IPv6 Decompression")
        ipv6_decompress.resizable(False, False)
        current_window = ipv6_decompress
        decompress_entry(ipv6_decompress)
    
def route_aggregation_window(window):
    route = tk.Toplevel(window)
    route.geometry("800x600")
    route.title("Route Aggregation")
    route.resizable(False, False)

def save_window():
    global current_window
    current_window.withdraw()
    return current_window

def reopen(window):
    window.deiconify()
    

    
    


    


    

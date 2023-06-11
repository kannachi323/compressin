import tkinter as tk
import ipaddress
from config import *
from tkVideoPlayer import TkinterVideo

window_for_compress = None
window_for_decompress = None
paused = False

def prevent_exit():
    pass

def validIPv6Address(address):
    try:
        ipaddress.IPv6Address(address.replace(" ", ''))
        return True
    except ipaddress.AddressValueError:
        return False
    
def clear_text(text):
    text.delete("1.0", "end")

def clear_all(entry, output):
    clear_text(entry)
    clear_text(output)

def save_compress_window():
    global window_for_compress
    window_for_compress.withdraw()
    return window_for_compress

def save_decompress_window():
    global window_for_decompress
    window_for_decompress.withdraw()
    return window_for_decompress

def reopen(window):
    window.deiconify()

#MENU options:
def ipv6_compression_window(window):
    global window_for_compress
    if window_for_compress != None:
        reopen(window_for_compress)
    else:
        ipv6_compress = tk.Toplevel(window)
        ipv6_compress.geometry("680x550")
        ipv6_compress.title("IPv6 Compression")
        ipv6_compress.resizable(False, False)
        window_for_compress = ipv6_compress
        compress_entry(ipv6_compress)
        
def ipv6_decompression_window(window):
    global window_for_decompress
    if window_for_decompress != None:
        reopen(window_for_decompress)
    else:
        ipv6_decompress = tk.Toplevel(window)
        ipv6_decompress.geometry("680x550")
        ipv6_decompress.title("IPv6 Decompression")
        ipv6_decompress.resizable(False, False)
        window_for_decompress = ipv6_decompress
        decompress_entry(ipv6_decompress)

def route_aggregation_window(window):
    route = tk.Toplevel(window)
    route.geometry("1024x768")
    route.title("Route Aggregation")
    route.resizable(False, False)
    videoplayer = TkinterVideo(master=route, scaled=True)
    videoplayer.load(r"ipv6-compress-aggregation/route_aggregation.mp4")
    videoplayer.pack(expand=True, fill="both")
    videoplayer.play()
    
    route.mainloop()

def compress(window, entry, output):
    clear_text(output)
    lines = entry.get("1.0", "end").strip().split("\n")
    for a, address in enumerate(lines):
        if validIPv6Address(address) and len(lines) <= 50:
            temp = address.replace(" ", '').split(":")
            temp = [c.lstrip('0') or '0' for c in temp if len(c) > 1]
            index = temp.index("0")
            while (temp[index] == "0"):
                temp[temp.index("0")] = ''
                index += 1
            lines[a] = ':'.join(temp)
            lines[a] = lines[a].replace(":::", "::")
            lines[a] = lines[a].replace("::::", "::")
            while (":::" in lines[a] or "::::" in lines[a] or ":::::" in lines[a] 
                   or ":::::::" in lines[a] or "::::::::" in lines[a]):
                lines[a] = lines[a].replace(":::", "::")
                lines[a] = lines[a].replace("::::", "::")
                lines[a] = lines[a].replace(":::::", "::")
                lines[a] = lines[a].replace("::::::", "::")
                lines[a] = lines[a].replace(":::::::", "::")
                lines[a] = lines[a].replace("::::::::", "::")

        
            output.insert("end", f"{lines[a]}\n")
        
        elif len(lines) > 50:
            output.insert("end", "Too many inputs!\n")
        else:
            output.insert("end", "Invalid Entry!\n")

def compress_entry(window):
    # Create an entry box to get ipv6 addresses
    entry = tk.Text(window, height=31, width=40, highlightthickness=1, highlightbackground="black")
    entry.place(x=5, y=0)
    compress_btn = tk.Button(window, text="Compress", width=10, height=2, command=lambda: compress(window, entry, output))
    compress_btn.place(x=120, y=506)
    output = tk.Text(window, height=31, width=40, highlightthickness=1, highlightbackground="black")
    output.place(x=348, y=0)
    save_exit_btn = tk.Button(window, text="Save/Exit", width=10, height=2, command=lambda: save_compress_window())
    save_exit_btn.place(x=300, y=506)
    clear_btn = tk.Button(window,  text="Clear All", width=10, height=2, command=lambda: clear_all(entry, output))
    clear_btn.place(x=480, y=506)
    window.protocol("WM_DELETE_WINDOW", prevent_exit)

def decompress(window, entry, output):
    lines = entry.get("1.0", "end").strip().split("\n")
    clear_text(output)
    
    for a, address in enumerate(lines):
        if validIPv6Address(address) and len(lines) <= 50:
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
            output.insert("end", f"{lines[a]}\n")
        
        elif len(lines) > 50:
            output.insert("end", "Too many inputs!\n")
        else:
            output.insert("end", "Invalid Entry!\n")
    
def decompress_entry(window):
    # Create an entry box to get ipv6 addresses
    entry = tk.Text(window, height=31, width=40, highlightthickness=1, highlightbackground="black")
    entry.place(x=5, y=0)
    compress_btn = tk.Button(window, text="Decompress", width=10, height=2, command=lambda: decompress(window, entry, output))
    compress_btn.place(x=120, y=506)
    output = tk.Text(window, height=31, width=40, highlightthickness=1, highlightbackground="black")
    output.place(x=348, y=0)
    save_exit_btn = tk.Button(window, text="Save/Exit", width=10, height=2, command=lambda: save_decompress_window())
    save_exit_btn.place(x=300, y=506)
    clear_btn = tk.Button(window,  text="Clear All", width=10, height=2, command=lambda: clear_all(entry, output))
    clear_btn.place(x=480, y=506)
    window.protocol("WM_DELETE_WINDOW", prevent_exit)

    
    


    
    


    


    

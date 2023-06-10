import tkinter as tk

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
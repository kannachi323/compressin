import tkinter as tk
from program import *

def mac_placement(window):
    #open ipv6 compression/route aggregation windows
    ipv6_compress = tk.Button(window, text="IPv6 Compression", width=16, height=8, borderwidth=1, command=ipv6_compression_window)
    ipv6_compress.place(x=65, y=45)
    ipv6_decompress = tk.Button(window, text="IPv6 Decompression", width=16, height=8, borderwidth=1, command=ipv6_decompression_window)
    ipv6_decompress.place(x=429, y=45)
    route = tk.Button(window, text="Route Aggregation", width=16, height=8, borderwidth=1, command=route_aggregation_window)
    route.place(x=242, y=366) 

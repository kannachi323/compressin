import tkinter as tk
from program import *

def win_placement(window):
    #open ipv6 compression/route aggregation windows
    ipv6_compress = tk.Button(window, text="IPv6 Compression", width=25, height=9, borderwidth=1, command=lambda: ipv6_compression_window(window))
    ipv6_compress.place(x=63, y=43)
    ipv6_decompress = tk.Button(window, text="IPv6 Decompression", width=25, height=9, borderwidth=1, command=lambda: ipv6_decompression_window(window))
    ipv6_decompress.place(x=427, y=43)
    route = tk.Button(window, text="Route Aggregation", width=25, height=9, borderwidth=1, command=lambda: route_aggregation_window(window))
    route.place(x=240, y=364) 



    

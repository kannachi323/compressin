import tkinter as tk
import pygame
from pygame import mixer
from sys import platform
from config import *
from program import *

volume_state = None

def toggle_volume(volume_button):
    global volume_state
    if volume_state > 0:
        pygame.mixer.music.set_volume(0)
        volume_state = 0
        volume_button.config(text="Unmute")
    else:
        pygame.mixer.music.set_volume(0.2)
        volume_state = 1
        volume_button.config(text="Mute")

def main():
    bkg_path = os.path.join(get_os_path(), 'background.png')
    menu_music_path = os.path.join(get_os_path(), 'menu.mp3')

    root = tk.Tk()
    root.title("Compressin!")
    root.geometry("680x550")
    bkg = tk.PhotoImage(file=bkg_path)
    bkg_label = tk.Label(root, image=bkg)
    bkg_label.pack()
    root.resizable(False, False)
    
    global volume_state
    pygame.init()
    mixer.init()
    mixer.music.load(menu_music_path)
    pygame.mixer.music.set_volume(0.2)
    volume_state = 1
    pygame.mixer.music.play(loops=-1)
    volume_button = tk.Button(root, text="Mute", command=lambda: toggle_volume(volume_button))
    volume_button.place(x=600, y=500)

    if platform == "darwin":
        osx_placement(root)

    elif platform == "win32":
        win_placement(root)

    root.mainloop()


if __name__ == '__main__':
    main()





import tkinter as tk
from tkinter import filedialog
from pygame import mixer

def load_file():
    filename = filedialog.askopenfilename(filetypes=[("MP3 Files", "*.mp3")])
    if filename:
        mixer.music.load(filename)
        mixer.music.play()

def pause_music():
    mixer.music.pause()

def stop_music():
    mixer.music.stop()

root = tk.Tk()
root.title("Simple Music Player")

mixer.init()

play_button = tk.Button(root, text="Play Music", font=("Arial", 14), command=load_file)
play_button.pack(pady=10)

pause_button = tk.Button(root, text="Pause Music", font=("Arial", 14), command=pause_music)
pause_button.pack(pady=10)

stop_button = tk.Button(root, text="Stop Music", font=("Arial", 14), command=stop_music)
stop_button.pack(pady=10)

root.mainloop()

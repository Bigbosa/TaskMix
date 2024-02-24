import os
import pygame
import customtkinter as ctk
from customtkinter import CTkButton
import tkinter as tk
from tkinter import filedialog
from tkinter import ttk

class MusicPlayerApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Music Player")
        self.configure(bg="black")
        self.geometry("500x500")
        self.playlist = []
        self.loop_song = tk.BooleanVar()
        self.loop_song.set(False)
        self.resizable(False, False)
        self.iconbitmap("icon2.ico")

        self.create_widgets()

    def create_widgets(self):
        style = ttk.Style()
        style.configure('TButton', background='black', foreground='black')

        frame1 = ctk.CTkFrame(master=self, fg_color="black")
        frame1.pack(side=ctk.LEFT, fill=ctk.BOTH)
        frame1.configure(width=100, height=500)

        self.playlist_listbox = tk.Listbox(self, selectmode=tk.SINGLE, bg="black", fg="white", bd=0,
                                           selectborderwidth=0,
                                           highlightthickness=0)
        self.playlist_listbox.pack(side=tk.TOP, fill=tk.BOTH, padx=10)

        add_button = CTkButton(frame1, text="Add to Playlist", command=self.add_to_playlist, hover_color="white",
                               fg_color="transparent", text_color="white", border_color="white",
                               border_width=3)
        add_button.pack(side=tk.TOP, pady=5, padx=(0, 5))

        remove_button = CTkButton(frame1, text="Remove from Playlist", command=self.remove_from_playlist, hover_color="white",
                                  fg_color="transparent", text_color="white", border_color="white",
                                  border_width=3)
        remove_button.pack(side=tk.TOP, pady=5, padx=5)

        play_button = CTkButton(frame1, text="Play", command=self.play_music, hover_color="white",
                                fg_color="transparent", text_color="white", border_color="white",
                                border_width=3)
        play_button.pack(side=tk.TOP, pady=5, padx=5)

        stop_button = CTkButton(frame1, text="Stop", command=self.stop_music, hover_color="white",
                                fg_color="transparent", text_color="white", border_color="white",
                                border_width=3)
        stop_button.pack(side=tk.TOP, pady=5, padx=5)

        skip_button = CTkButton(frame1, text="Skip 10 Seconds", command=lambda: self.skip_time(10), hover_color="white",
                                fg_color="transparent", text_color="white", border_color="white",
                                border_width=3)
        skip_button.pack(side=tk.TOP, pady=5, padx=(5, 0))

        self.update_playlist_display()

    def add_to_playlist(self):
        file_path = filedialog.askopenfilename(
            title="Select MP3 file",
            filetypes=[("MP3 files", "*.mp3")]
        )
        if file_path:
            self.playlist.append(file_path)
            self.update_playlist_display()

    def remove_from_playlist(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            del self.playlist[selected_index]
            self.update_playlist_display()

    def play_music(self):
        selected_index = self.playlist_listbox.curselection()
        if selected_index:
            selected_index = int(selected_index[0])
            file_path = self.playlist[selected_index]

            pygame.mixer.init()
            pygame.mixer.music.load(file_path)
            pygame.mixer.music.play(loops=-1 if self.loop_song.get() else 0)

    def stop_music(self):
        pygame.mixer.music.stop()

    def skip_time(self, seconds):
        if pygame.mixer.music.get_busy():
            current_time = pygame.mixer.music.get_pos() / 1000
            new_time = max(0, min(current_time + seconds, pygame.mixer.Sound(self.playlist[0]).get_length()))
            pygame.mixer.music.set_pos(new_time)

    def update_playlist_display(self):
        self.playlist_listbox.delete(0, tk.END)
        for file_path in self.playlist:
            self.playlist_listbox.insert(tk.END, os.path.basename(file_path))

if __name__ == "__main__":
    app = MusicPlayerApp()
    app.mainloop()

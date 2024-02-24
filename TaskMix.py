import customtkinter
from customtkinter import *
import customtkinter as ctk
from PIL import Image, ImageTk
from player import MusicPlayerApp
from task_manager import TaskManager
import tkinter as tk

class TaskMix(ctk.CTk):
    def __init__(self, *args, **kwargs):
        ctk.CTk.__init__(self, *args, **kwargs)
        self.title("TaskMix")
        self.geometry("600x500")
        self.iconbitmap("icon2.ico")
        self.resizable(False, False)

        frame1 = customtkinter.CTkFrame(master=self, fg_color="black")
        frame1.pack(side=ctk.LEFT, fill=ctk.BOTH)
        frame1.configure(width=100, height=500)

        image_path_excel_app = r"E:\ExcelAssist\src\1.png"
        original_image_excel_app = Image.open(image_path_excel_app)
        resized_image_excel_app = original_image_excel_app.resize((50, 50))
        photo_excel_app = ImageTk.PhotoImage(resized_image_excel_app)

        image_path_task_mix = r"E:\ExcelAssist\src\2.png"
        original_image_task_mix = Image.open(image_path_task_mix)
        resized_image_task_mix = original_image_task_mix.resize((50, 50))
        photo_task_mix = ImageTk.PhotoImage(resized_image_task_mix)

        self.button_excel_app = CTkButton(frame1, text="MP3 Player", hover_color="black",
                                          fg_color="transparent", text_color="white", image=photo_excel_app,
                                          command=self.open_music_player)
        self.button_excel_app.pack(side=TOP)

        self.button_task_mix = CTkButton(frame1, text="Task Manager", hover_color="black",
                                         fg_color="transparent", text_color="white", image=photo_task_mix, command=self.open_task_manager)
        self.button_task_mix.pack(side=TOP)

        welcome_label = CTkLabel(self, text="Welcome to TaskMix!", font=("Helvetica", 16), fg_color="black")
        welcome_label.pack(pady=20)

        # Add app logo image
        image_path_app_logo1 = r"E:\ExcelAssist\src\icon.png"
        original_image_app_logo1 = Image.open(image_path_app_logo1)
        resized_image_app_logo1 = original_image_app_logo1.resize((400, 400))
        photo_app_logo1 = ImageTk.PhotoImage(resized_image_app_logo1)

        # Display app logo on the right side
        app_logo_label1 = CTkLabel(self,text="", image=photo_app_logo1)
        app_logo_label1.pack(side=RIGHT, padx=10)

    def open_music_player(self):
        music_player_window = MusicPlayerApp()
        music_player_window.mainloop()

    def open_task_manager(self):
        task_manager_window = TaskManager()
        task_manager_window.mainloop()

if __name__ == "__main__":
    app = TaskMix()
    app.mainloop()

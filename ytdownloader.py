from pytube import YouTube
import tkinter as tk
import sys
from tkinter import messagebox
import os

# Create a tkinter window for the message box
root = tk.Tk()
root.withdraw()  

print("Welcome to the Video Downloader")
print("Please input the YouTube video link: ")
link = input("> ")

try:
    #prints the details of the video
    yt = YouTube(link)
    print()
    print("Title: ", yt.title)
    print("Author: ", yt.author)
    print("Views: ", yt.views)
    print("Length: ", yt.length)
    print()

    while True:
        username = os.getlogin() #stores the username of the os so that it can be used in the file path

        print("Do you want the VIDEO (v) or AUDIO (a) only? ")
        print("Enter (q) to QUIT")
        answer = input("> ")

        if answer.lower() == "v":
            yd = yt.streams.get_highest_resolution()
            file_path = yd.download(f"/Users/{username}/Downloads")
            messagebox.showinfo("Save", "Your video has been saved in your Downloads folder")
            break
        elif answer.lower() == "a":
            yd = yt.streams.get_audio_only()
            file_path = yd.download(f"/Users/{username}/Downloads")
            messagebox.showinfo("Save", "Your audio has been saved in your Downloads folder")
            break
        elif answer.lower() == "q":
            print("Downloader Closed")
            sys.exit(1)
        else:
            print("Invalid input. Please try again")

except Exception as e:
    print("Error:", e)

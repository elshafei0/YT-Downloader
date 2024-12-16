from tkinter import *
from tkinter import messagebox
from yt_dlp import YoutubeDL

# Function For High_Quality
def high_Quality():
    try:
        url = myentry.get()
        ydl_opts = {
            'format': 'best'
            ,'merge_output_format':'mp4'
            ,'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "High Quality Video Has Been Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "Error To Download High Quality Video")

# Function For Low_Quality
def Low_Quality():
    try:
        url = myentry.get()
        ydl_opts = {
            'format': 'worst',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "Low Quality Video Has Been Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "Error To Download Low Quality Video")

# Function For Audio
def Audio():
    try:
        url = myentry.get()
        ydl_opts = {
            'format': 'bestaudio',
            'outtmpl': 'downloads/%(title)s.%(ext)s'
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
            messagebox.showinfo("Success", "High Quality Audio Has Been Downloaded")
    except Exception as e:
        messagebox.showerror("Error", "Error To Download High Quality Audio")

root = Tk()
root.geometry("500x500")
root.title("Video Downloader")
root.configure(bg="black")

mylabel = Label(root, text="Enter Link To Download:", font="Tahoma 25", bg="black", fg="white")
mylabel.pack()

myentry = Entry(root, width="35", font="Tahoma 15")
myentry.pack(pady="15")

high = Button(root, text="High Quality", bg="red", fg="white", font="Tahoma 15", command=high_Quality)
high.pack(pady="10")

low = Button(root, text="Low Quality", bg="red", fg="white", font="Tahoma 15", command=Low_Quality)
low.pack(pady="10")

audio = Button(root, text="Audio", bg="red", fg="white", font="Tahoma 15", command=Audio)
audio.pack(pady="10")

root.mainloop()

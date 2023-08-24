from tkinter import Tk, Label, Entry, Button, StringVar
from pytube import YouTube
# Create the main window
root = Tk()
root.geometry('500x300')
root.resizable(0, 0)
root.title('YouTube Downloader')

# Create a label
Label(root, text="Download YouTube videos for free", font='sans-serif 14 bold').pack()

# Create an entry field for the link
link = StringVar()
Label(root, text="Paste your link here", font='sans-serif 15 bold').place(x=150, y=55)
link_enter = Entry(root, width=70, textvariable=link)
link_enter.place(x=30, y=85)

# Define a function for the button's command
def download():
    # Add your download logic here based on the 'link.get()' value
    print("Downloading video from link:", link.get())

# Create a download button
Button(root, text='Download', font='sans-serif 16 bold', bg='red', padx=2, command=download).place(x=100, y=150)

root.mainloop()


def download():
    url = YouTube(str(link.get())) #This captures the link(url) and locates it from YouTube.
    video = url.streams.first() # This captures the streams available for downloaded for the video i.e. 360p, 720p, 1080p. etc.
    video.download() # This is the method with the instruction to download the video.
    Label(root, text="Downloaded", font="arial 15").place(x=100, y=120) #Once the video is downloaded, this label `downloaded` is displayed to show dowload completion.
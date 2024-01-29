from tkinter import *
from tkinter import filedialog

root = Tk()
root.title('Video Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# app label
app_label = Label(root, text="youtube downloader", fg='blue', font=('Arial',20))
canvas.create_window(200, 20, window=app_label)

# entry to accept video URL
url_label = Label(root, text="Enter video URL")
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# path to download videos
path_label = Label(root, text="select path where to download")
bath_button = Button(root, text="Select")
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=bath_button)

# download button
download_button = Button(root, text='Download')
canvas.create_window(200, 200, window=download_button)

root.mainloop()

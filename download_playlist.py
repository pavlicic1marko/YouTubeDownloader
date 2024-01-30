from tkinter import *
from pytube import Playlist


def download():
    playlist_path = url_entry.get()
    print('Downloading...')
    playlist = Playlist(playlist_path)
    print('Number of videos in playlist: %s' % len(playlist.video_urls))
    for index, video in enumerate(playlist.videos, start=1):
        try:
            # Rename the downloaded file with a number prefix
            original_filename = video.streams.get_highest_resolution().default_filename
            new_filename = f"{index:02d}_{original_filename}"
            video.streams.get_highest_resolution().download(filename=new_filename)

            print(f"Downloaded video {index}: {video.title}")
        except Exception as e:
            print(f"Error downloading video {index}: {str(e)}")


root = Tk()
root.title('Video Downloader')
canvas = Canvas(root, width=400, height=300)
canvas.pack()

# app label
app_label = Label(root, text="youtube playlist downloader", fg='blue', font=('Arial', 15))
canvas.create_window(200, 20, window=app_label)

# entry to accept video URL
url_label = Label(root, text="Enter playlist URL")
url_entry = Entry(root)
canvas.create_window(200, 80, window=url_label)
canvas.create_window(200, 100, window=url_entry)

# path to download videos
path_label = Label(root, text="select path where to download")
bath_button = Button(root, text="Select", command='get_path')
canvas.create_window(200, 150, window=path_label)
canvas.create_window(200, 170, window=bath_button)

# download button
download_button = Button(root, text='Download', command=download)
canvas.create_window(200, 200, window=download_button)

root.mainloop()

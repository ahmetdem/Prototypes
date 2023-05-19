from pytube import Playlist

SAVE_PATH = r"C:\Users\ahmet\Music\music_for_spotify\rezero"

def playlist(link):

    def download(object):
        yt = object.streams.get_audio_only()
        try:    
            yt.download(SAVE_PATH)
            print(f"Downloading {object.title}")
        except:
            print("An Error has Occured!")

    pl = Playlist(link)

    for audio in pl.videos:
        download(audio)

    print("Download has complated.")

link = input("Enter the link of the playlist: ")
playlist(link)
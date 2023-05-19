from pytube import Search, YouTube

SAVE_PATH = r"C:\Users\ahmet\Videos\Videolar"

def Download(name):

    search = Search(name)
    yt = search.results[0].streams.get_highest_resolution()

    try:    
        yt.download(SAVE_PATH)

    except:
        print("An Error has Occured!")

    print("Download has complated.")

name = input("Enter the name of the video: ")
Download(name)
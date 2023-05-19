from pytube import YouTube

SAVE_PATH = r"C:\Users\ahmet\Videos\Videolar"

def Download(link):

    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()

    try:
        youtubeObject.download(SAVE_PATH)

    except:
        print("An error has occurred")
        
    print("Download is completed successfully")


link = input("Enter the YouTube video URL: ")
Download(link)
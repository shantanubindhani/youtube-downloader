from pytube import YouTube

try:
    link = input("Paste youtube Link : ")

    yt = YouTube(link)
    name = yt.title

    strms = yt.streams.filter(mime_type= "video/mp4",progressive=True)

    print("="*40)

    print("Available resolutions : ")
    for s in strms:
        print(f"{strms.index(s) + 1}. {s.resolution}")

    r = int(input("\n --> ")) - 1

    print("\n","="*40)

    vid = strms[r]

    vid.download("./YouTube_video")
    print("\n\n        VIDEO DOWNLOADED, search for YouTube_video folder \n")
except:
    print("Some error occoured while fetching the link, Try again!.")

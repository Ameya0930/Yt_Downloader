from pytube import YouTube
print("Enter the  url:\n")
url = input()

youtube_1 = YouTube(url)

videos = youtube_1.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)
strm = int(input("enter: "))
videos[strm].download()

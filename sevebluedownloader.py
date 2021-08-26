from pytube import YouTube
from pytube import Playlist

def playlistvid(url,loc):
    try:
        playlist = Playlist(url)
        playlist.download_all(download_path=loc)
 
    except Exception as e:
        print(e)
 

def downloadnow(youtube_video_url,location,type):
    try:
        yt_obj = YouTube(youtube_video_url)
        
        if type == 'a':
            title = yt_obj.title 
            title = title[0:25] + ".mp3"
            yt_obj.streams.get_audio_only().download(output_path=location, filename=title)
            print('YouTube audio downloaded successfully')
        else:
            title = yt_obj.title 
            title = title[0:25] + ".mp4"
            filters = yt_obj.streams.filter(progressive=True, file_extension='mp4')
            filters.get_highest_resolution().download(output_path=location, filename=title)
            print('YouTube Video downloaded successfully')
    except Exception as e:
        print(e)

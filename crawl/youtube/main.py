from pytube import YouTube, Playlist
import os
import glob
from threading import Thread

def getFileMp4():
	mylist = [f for f in glob.glob("*.mp4")]
	return mylist

def downloadVideo(*urls, path = 'Video'):
	for url in urls[0][:5]:
		yt = YouTube(url)
		yt.streams.filter(file_extension='mp4')
		if yt.streams.get_by_itag(22):
			stream = yt.streams.get_by_itag(22)
			print("_____________ Download Video _____________ ")
			print("title: ", yt.title)
			print("url: ", url)
			stream.download(path)
			
		elif yt.streams.get_by_itag(18):
			stream = yt.streams.get_by_itag(18)
			print("_____________ Download Video _____________ ")
			print("title: ", yt.title)
			print("url: ", url)
			stream.download(path)
		else:
			return
		print("-------")

urls = Playlist('https://www.youtube.com/watch?v=41qgdwd3zAg&list=PLS1QulWo1RIaJECMeUT4LFwJ-ghgoSH6n')
if __name__ == "__main__":
	thread = Thread(target=downloadVideo, args={urls})
	thread.start()

from pytube import YouTube
import os

class GET:
     def __init__(self, lst:list):
          self.video:list = lst
          self.success:int = 0
          self.lose:int = 0
          self.lst:list = []

     def download_mp3(self, url:str)->str:
          video = YouTube(url=url)
          data = {'title':video.title,'url':url}
          print(data)
          if os.path.exists(video.title+".mp3"):
               pass
          else:
               out_path = video.streams.filter(only_audio=True).first().download()
               new_name = os.path.splitext(out_path)
               os.rename(out_path, new_name[0]+'.mp3')
               self.lst.append(data)
          return True
     
     def download_mp4(self, url:str)->bool:
          video = YouTube(url=url)
          data = {'title':video.title,'url':url}
          print(data)
          if os.path.exists(video.title+".mp4"):
               pass
          else:
               out_path = video.streams.filter(file_extension="mp4").first().download()
               new_name = os.path.splitext(out_path)
               os.rename(out_path, new_name[0]+'.mp4')
               self.lst.append(data)
          return 
     
     def get_data(self):
          print("1. Audio\n2. Video")
          num = int(input("Enter you choice:"))
          if num == 1:
               for i in self.video:
                    self.download_mp3(i)
          elif num == 2:
               for i in self.video:
                    self.download_mp4(i)          
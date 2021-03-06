from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os, json


class MyHandler(FileSystemEventHandler):
    i=1
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            x=0
            new_name=filename
            if filename.endswith(('.tmp','.crdownload')):
                x=1
                break
            elif filename.endswith('.pdf'):
                folder_destination=r'C:\Users\afidanso\Documents\PDF'
            elif filename.endswith(('.xls', '.xlsx', '.xlsb', '.xlsm', 'csv')):
                folder_destination=r'C:\Users\afidanso\Documents\EXCEL'
            elif filename.endswith(('.jpg', '.jpeg', '.png')):
                folder_destination=r'C:\Users\afidanso\Documents\Images'
            else:
                folder_destination=r'C:\Users\afidanso\Documents\Files'

            filename, extention = filename.split(".")
            if x==0:
                file_exists=os.path.isfile(folder_destination + "/" + new_name)
                while file_exists:
                    self.i+=1
                    new_name=  filename + "_" + str(self.i) + "." + extention
                    file_exists=os.path.isfile(folder_destination + "/" + new_name)

                src = folder_to_track + "/" + filename + "." + extention
                new_destination=folder_destination + "/" + new_name
                os.rename(src, new_destination)





folder_to_track=r'C:\Users\afidanso\Downloads\DestinationFolder'
event_handler=MyHandler()
observer=Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

#if m.endswith('.mp3'):

#elif m.endswith('.flac'):




try:
    while  True:
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()

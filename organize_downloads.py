#!/usr/local/bin/python3

"""
Oranize the donwload folder through moving files in the download folder to more
appropriate folders.
"""

from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os #operating system dependent functionalities
import json

img_formats = [".png", ".jpg", ".gif", ".HEIC"]
video_formats = ["video", ".mp4", ".MOV"]

class HandleDownloads(FileSystemEventHandler):
    #observer.schedule runs on_modified()
    def on_modified(self, event):
        try:
            for filename in os.listdir(folder_to_track):
                src= folder_to_track + "/" + filename
                if ("U10" in filename):
                    new_destination = "/Users/maximilianvorbrodt/Documents/STUDIER/TDDD91" + "/" + filename
                    os.rename(src, new_destination)

                if ("TDAB01" in filename):
                    new_destination = "/Users/maximilianvorbrodt/Documents/STUDIER/TDAB01" + "/" + filename
                    os.rename(src, new_destination)

                if ("TFYA87" in filename):
                    new_destination = "/Users/maximilianvorbrodt/Documents/STUDIER/TFYA87" + "/" + filename
                    os.rename(src, new_destination)

                if ("TDDC17" in filename):
                    new_destination = "/Users/maximilianvorbrodt/Documents/STUDIER/TDDC17" + "/" + filename
                    os.rename(src, new_destination)

                if ("TDDD37" in filename):
                    new_destination = "/Users/maximilianvorbrodt/Documents/STUDIER/TDDD37" + "/" + filename
                    os.rename(src, new_destination)

                if ("TDDD92" in filename):
                    new_destination = "/Users/maximilianvorbrodt/Documents/STUDIER/TDDD92" + "/" + filename
                    os.rename(src, new_destination)

                for i in img_formats:
                    if i in filename and filename != "Downloaded images":
                        src = folder_to_track + "/" + filename
                        new_destination = "/Users/maximilianvorbrodt/Downloads/Downloaded images" + "/" +filename
                        os.rename(src, new_destination)

                for i in video_formats:
                    if i in filename and filename != "Downloaded videos":
                        src = folder_to_track + "/" + filename
                        print ("SRC: ", src)
                        new_destination = "/Users/maximilianvorbrodt/Downloads/Downloaded videos" + "/" +filename
                        print ("DEST: ", new_destination)
                        os.rename(src, new_destination)
        except:
            pass



#where to look for modified files
folder_to_track = "/Users/maximilianvorbrodt/Downloads" #pwd - "print working directory"

event_handler = HandleDownloads()
observer = Observer()

go_recursively = True #a boolean that allow me to catch all the event that occurs even in the sub directories of my current directory

#Schedules watching a path and calls appropriate methods specified in the given event handler in response to file system events
observer.schedule(event_handler, folder_to_track, recursive = go_recursively)
observer.start()

#wait for modifications to occur
try:
    while True:
        time.sleep(30)
except KeyboardInterrupt:
    observer.stop()

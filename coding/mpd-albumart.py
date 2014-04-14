#!/usr/bin/env python
import sys,mpd,os,socket
musiclocation = '/home/randalltux/Music' #location of music       
artlocation = '~/.mpd/covers' #where you want albumart storing
tmp_path = '/tmp/mpd.jpg' #location for temporary file so conky can find it

musiclocation = os.path.expanduser(musiclocation)
artlocation = os.path.expanduser(artlocation)

client = mpd.MPDClient()  
try:
    client.connect("localhost", 6600)    
except socket.error:
    sys.exit(1)
    
song = client.currentsong() 
artist = song['artist']
album = song['album']

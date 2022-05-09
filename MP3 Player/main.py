import tkinter as tk
import pygame
import shutil
import os
from tkinter import filedialog
import time
from mutagen.mp3 import MP3

class App(tk.Frame):
    def __init__(self, root):
        root.title("MP3 Player")
        width=500
        height=440
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)
        pygame.mixer.init()
        
        self.songs = []
        self.paused = False
        self.currentSong = ""
        
        self.PlayButtonImg = tk.PhotoImage(file=os.path.join('UI', 'play.png'))
        self.PauseButtonImg = tk.PhotoImage(file=os.path.join('UI', 'pause.png'))
        self.NextButtonImg = tk.PhotoImage(file=os.path.join('UI', 'next.png'))
        self.PreviousButtonImg = tk.PhotoImage(file=os.path.join('UI', 'previous.png'))
        
        self.AppLabel = tk.Label(root, text="MP3 Player", font=("Acme", 36))
        self.AppLabel.place(x=130, y=20, width=240, height=55)
        
        self.Playlist = tk.Listbox(root, font=("Acme", 18), borderwidth=0)
        self.Playlist.place(x=30, y=80, width=444, height=250)
        
        self.PlayButton = tk.Button(root, image=self.PlayButtonImg, command=self.play, borderwidth=0)
        self.PlayButton.place(x=100, y=370, width=56, height=56)
        
        self.PauseButton = tk.Button(root, image=self.PauseButtonImg, command=self.pause, borderwidth=0)
        self.PauseButton.place(x=180, y=370, width=56, height=56)
        
        self.PreviousButton = tk.Button(root, image=self.PreviousButtonImg, command=self.PlayPrevious, borderwidth=0)
        self.PreviousButton.place(x=260, y=370, width=56, height=56)
        
        self.NextButton = tk.Button(root, image=self.NextButtonImg, command=self.PlayNext, borderwidth=0)
        self.NextButton.place(x=340, y=370, width=56, height=56)
        
        self.Duration = tk.Label(root, text="00:00 - 00:00", font=("Acme", 18))
        self.Duration.place(x=181, y=336, width=138, height=28)
        
        self.Volume = tk.Scale(root, from_=100, to=0, command=self.VolumeChange)
        self.Volume.set(100)
        self.Volume.place(x=434, y=335, width=50, height=90)
        
        self.menu = tk.Menu(root)
        root.config(menu=self.menu)
        
        self.filemenu = tk.Menu(self.menu)
        self.menu.add_cascade(label="Add Song", menu=self.filemenu)
        self.filemenu.add_command(label="Open", command=self.addSong)
        
    def addSong(self):
        song = filedialog.askopenfilenames(filetypes=[("MP3 Files", "*.mp3")])
        songs = list(song)
        for song in songs:
            shutil.copy(song, "Music")
            songName = song.split("/")[-1]
            self.songs.append(songName)
            self.Playlist.insert(tk.END, songName)
        
    def play(self):
        if len(self.songs) != 0:
            self.paused = False
            song = self.songs[self.Playlist.curselection()[0]]
            self.currentSong = song
            self.PlayTime()
            pygame.mixer.music.load(os.path.join("Music", song))
            pygame.mixer.music.play(loops=0)
    
    def pause(self):
        print(pygame.mixer.music.get_pos())
        if self.paused:
            pygame.mixer.music.unpause()
            self.paused = False
        else:
            pygame.mixer.music.pause()
            self.paused = True
            
    def PlayNext(self):
        if len(self.songs) != 0:
            if self.songs.index(self.currentSong) == len(self.songs) - 1:
                song = self.songs[0]
            elif len(self.songs) == 1:
                song = self.songs[0]
            else:
                song = self.songs[self.songs.index(self.currentSong) + 1]
            self.paused = False
            self.currentSong = song
            self.PlayTime()
            pygame.mixer.music.load(os.path.join("Music", song))
            pygame.mixer.music.play(loops=0)
    
    def PlayPrevious(self):
        if len(self.songs) != 0:
            if self.songs.index(self.currentSong) == 0:
                song = self.songs[-1]
            elif len(self.songs) == 1:
                song = self.songs[0]
            else:
                song = self.songs[self.songs.index(self.currentSong) - 1]
            self.paused = False
            self.currentSong = song
            self.PlayTime()
            pygame.mixer.music.load(os.path.join("Music", song))
            pygame.mixer.music.play(loops=0)
            
    def PlayTime(self):
        self.currentTime = pygame.mixer.music.get_pos()/1000
        self.currentTime = time.strftime("%M:%S", time.gmtime(self.currentTime))
        self.totalTime = time.strftime("%M:%S", time.gmtime(MP3(os.path.join("Music", self.currentSong)).info.length))        
        self.Duration.config(text=str(self.currentTime) + " - " + str(self.totalTime))
        self.Duration.after(1000, self.PlayTime)
        
    def VolumeChange(self, value):
        pygame.mixer.music.set_volume(int(value)/100)
        
if __name__ == '__main__':
    root = tk.Tk()
    app = App(root)
    root.mainloop()
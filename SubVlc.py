import sublime, sublime_plugin
import os, sys
from new_vlc import VLCClient

HOME_DIR = os.popen("echo $HOME").read().strip()
PLAYLIST_DIR = HOME_DIR + "/.subvlc"

def check_playlist_dir():
    if not os.path.exists(PLAYLIST_DIR):
        print "dir not found"
        os.popen("mkdir {0}".format(PLAYLIST_DIR)).read()

#Loadtime configurations
check_playlist_dir()

# global variables
global vlc
vlc = VLCClient("::1")

global playlist
global cached_music_files
playlist = set()
playlist_playing = ''
cached_music_files = []

def cache_music_files():
    global cached_music_files
    files = os.popen("find ~ -iname '*.mp*'").readlines()
    cached_music_files = map(lambda x:x.strip(), files)
    print cached_music_files

def connect():
    try:
        global vlc
        vlc = VLCClient('::1')
        vlc.connect()
        cache_music_files()
        sublime.status_message("VLC Connected")
    except Exception as e:
        print e
        vlc = VLCClient('::1')
        sublime.status_message("In terminal : vlc --intf telnet --telnet-password admin&")

def clear_playlist():
    global playlist
    playlist = set()
    print playlist
    vlc.clear()
    sublime.status_message(vlc.status())

def read_playlist_file(item_number):
    if item_number == -1:
        return
    print item_number
    playlists = os.listdir(PLAYLIST_DIR)
    path = PLAYLIST_DIR + '/' + playlists[item_number]
    vlc.clear()
    playlist = set()
    playlist_playing = os.listdir(PLAYLIST_DIR)
    with open(path, 'r') as f:
        playlist = f.readlines()
        for song in playlist:
            add_song_to_vlc(song.strip())
    sublime.status_message(vlc.status())

def add_song_to_vlc(song):
    playlist.add(song)
    vlc.add(song)
    sublime.status_message(vlc.status())

def add_song_to_vlc_new(index):
    if index == -1:
        return
    playlist.add(cached_music_files[index])
    vlc.add(cached_music_files[index])
    sublime.status_message(vlc.status())

def enqueue_song_to_vlc_new(index):
    if index == -1:
        return
    playlist.add(cached_music_files[index])
    vlc.enqueue(cached_music_files[index])
    sublime.status_message(vlc.status())

def goto_item(number):
    if number == -1:
        return
    vlc.add(list(playlist)[number])

def set_status(message):
    sublime.status_message(message)

class ShowPlaylistsCommand(sublime_plugin.WindowCommand):
    def run(self):
        print 'ShowPlaylistsCommand'
        playlists = os.listdir(PLAYLIST_DIR)
        if not playlists:
            self.window.status_message("No playlists found yet!!!")
        else:
            self.window.show_quick_panel(playlists, read_playlist_file)

class SavePlaylistCommand(sublime_plugin.WindowCommand):
    def run(self):
        print 'SavePlaylistCommand'
        self.window.show_input_panel("Enter name for the playlist", "", self.save, None, None)

    def save(self, name):
        with open(PLAYLIST_DIR + "/" + name, 'w') as f:
            print playlist
            f.write('\n'.join(list(playlist)))

class SelectSongCommand(sublime_plugin.WindowCommand):
    def run(self):
        self.window.show_quick_panel(list(playlist), goto_item)

class ShowCurrentPlaylistCommand(sublime_plugin.WindowCommand):
    def run(self):
        print 'ShowCurrentPlaylistCommand'
        print playlist

class AddSongToPlaylistCommand(sublime_plugin.WindowCommand):
    def run(self):
        global cached_music_files
        self.window.show_quick_panel(cached_music_files, add_song_to_vlc_new)

class EnqueueSongToPlaylistCommand(sublime_plugin.WindowCommand):
    def run(self):
        global cached_music_files
        self.window.show_quick_panel(cached_music_files, enqueue_song_to_vlc_new)

class PlayCommand(sublime_plugin.WindowCommand):
    def run(self):
        vlc.play()
        set_status(vlc.status())

class PauseCommand(sublime_plugin.WindowCommand):
    def run(self):
        print vlc.pause()
        set_status("VLC paused")

class PrevCommand(sublime_plugin.WindowCommand):
    def run(self):
        print vlc.prev()
        set_status(vlc.status())

class StopCommand(sublime_plugin.WindowCommand):
    def run(self):
        print vlc.stop()
        set_status("VLC stopped")

class NextCommand(sublime_plugin.WindowCommand):
    def run(self):
        print vlc.next()
        set_status("Playing Next")
        set_status(vlc.status())

class LoopCommand(sublime_plugin.WindowCommand):
    def run(self):
        print vlc.loop()
        set_status("Looping")

class FastforwardCommand(sublime_plugin.WindowCommand):
    def run(self):
        print vlc.fastforward()

class ShowStatusCommand(sublime_plugin.WindowCommand):
    def run(self):
        set_status(vlc.status().replace("\n",'::'))

class PlaylistNameCommand(sublime_plugin.WindowCommand):
    def run(self):
        set_status(playlist_playing)

class ClearPlaylistCommand(sublime_plugin.WindowCommand):
    def run(self):
        clear_playlist()

class ConnectVlcCommand(sublime_plugin.WindowCommand):
    def run(self):
        connect()

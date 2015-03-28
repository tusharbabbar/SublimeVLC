# SublimeVLC
Control your playlists from your favourite Editor. Sublime plugin to Control VLC. 
> Tested for OSX only.

## Prerequisites
* VLC player must be installed.
* For OSX create an alias `alias vlc='/Applications/VLC.app/Contents/MacOS/VLC -I rc'`
* Before one can use SublimeVLC they must enable VLC on telnet with : `vlc --intf telnet --telnet-password admin&`

## Installation
* For OSX: `cd ~/Library/Application\ Support/Sublime\ /Text\ 2/Packages && git clone git@github.com:tusharbabbar/SublimeVLC.git`
> This is not a registered plugin yet.

## Usage
### Enable Plugin/Connect to VLC
* `ctrl+alt+o` Connects the plugin to the VLC Telnet server.

### Add songs to VLC playlist
* `ctrl+alt+a` Provides mechanism to choose songs from all the songs with `.mp*` extension in your machine and play immidiately.
* `ctrl+alt+e` Provides mechanism to choose songs from all the songs with `.mp*` extension in your machine and play in sequence.

### Manage playlists
* `ctrl+alt+s` Provides list of saved playlist and loads them on selection.
* `ctrl+alt+shift+s` Saves the current playlist.
* `ctrl+alt+c` Clears current playlist.
* `ctrl+alt+l` Loop in current playlist.

### Manage Songs
* `ctrl+alt+z` Select song from loaded playlist.
* `ctrl+alt+p` Play song.
* `ctrl+alt+q` Pause song.
* `ctrl+alt+n` Next song.
* `ctrl+alt+b` Prev song.
* `ctrl+alt+shift+.` Fastforward song.

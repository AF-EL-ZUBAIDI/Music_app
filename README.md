# Music Cloud
Music Cloud is a desktop application built with Python and Tkinter, designed to play your favorite music tracks. 
It allows you to add songs to a playlist, control playback (play, pause, stop), and navigate through your playlist with ease. 
The application also displays the current song's playback time and lets you jump to any part of the song using a slider.

## Features
- Add individual songs or multiple songs to your playlist.
- Play, pause, and stop music playback.
- Navigate to the next or previous song in the playlist.
- Delete a song or clear the entire playlist.
- Display the current playback time and total duration of the song.
- Seek to any position in the song using the slider.

## Setup
To run Music Cloud, you need Python and the following packages installed:

- `pygame` for music playback.
- `mutagen` for handling MP3 metadata.
- `Tkinter` for the GUI.

Install the required packages using pip:
```bash
pip install pygame mutagen
```

## Running the Application
1. Clone this repository to your local machine.
2. Navigate to the project directory.
3. Run the application with Python:

```bash
python music_cloud.py
```

## Usage
- Add Songs: Use the "Add Songs" menu to add individual or multiple songs to your playlist.
- Playback Controls: Use the control buttons below the playlist to play, pause, stop, or navigate through your songs.
- Delete Songs: Use the "Remove Songs" menu to delete a song from the playlist or clear the entire playlist.

## Note
Ensure you have your songs in the `./audio` directory relative to the script, or adjust the initial directory path in the file dialog options to match your music directory.

from tkinter import *
import pygame
from tkinter import filedialog
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk
import subprocess
import os


root = Tk()
root.title('Music Cloud')
root.iconbitmap('/Users/abedelzubaidi/Desktop/all/music/buttons/play.png')
root.geometry("800x750")

# Initialise Pygame Mixer
pygame.mixer.init()


# Colors
ROSE='#FF00E8'
RED='#FF0070'
BG_BLACK='#121212'
BLUE='#1FFFFC'


# Get Song Time Infos
def play_time():
    # Get the current time 
    current_time = pygame.mixer.music.get_pos() / 1000

    # throw up temporary label to get data
    slider_label.config(text=f'Slider: {int(my_slider.get())} and Song pos: {int(current_time)}')
   
   # Convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))  #to add hours %H:%M:%S

    # Get currently Playing song
    #current_song = song_box.curselection()

    # Get Song title from playlist
    song = song_box.get(ACTIVE)
    
    # Add back the directory to play the next song
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    # Load Song with Mutagen
    song_mut = MP3(song)

    # Get Song Length
    global song_length
    song_length = song_mut.info.length

    # Convert to time format
    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))  #to add hours %H:%M:%S

    # Increase cuurent time by 1 second
    current_time += 1

    if int(my_slider.get()) == int(song_length):
        status_bar.config(text=f'Time Elapsed: {converted_song_length}')

    elif int(my_slider.get()) == int(current_time):
        # Update Slider to Position
        slide_position = int(song_length)
        my_slider.config(to=slide_position, value=int(current_time))
    else:
        # Update Slider to Position
        slide_position = int(song_length)
        my_slider.config(to=slide_position, value=int(my_slider.get()))

        # Convert to time format
        converted_current_time = time.strftime('%M:%S', time.gmtime(int(my_slider.get())))

        # Output time ins Status Bar
        status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')

        # Move this thing along by 1 second
        next_time = int(my_slider.get()) + 1
        my_slider.config(value=next_time)


    # Output time ins Status Bar
    #status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')

    # Update slider position value to current song position
    #my_slider.config(value=int(current_time))


    # Update time 
    status_bar.after(1000, play_time)

    # Place the timer of the song at the left of Slide Bar
    time_runing = Label(root, text=f'{converted_current_time}', font=("CLIP", 24), fg=ROSE)
    time_runing.place(x=110, y=523)

    duration_song = Label(root, text=f'{converted_song_length}', font=("CLIP", 24), fg=BLUE)
    duration_song.place(x=690, y=523)


    # Get the reset of time for the of the Song
    timer = song_length - current_time 
    print('#######################',timer) #back end


    # Converte the timer from ms to 00:00
    converted_timer = time.strftime('%M:%S', time.gmtime(timer))
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$",converted_timer)  # back end

    # Position the the timer on the screen
    minus_time = Label(root, text=f'{converted_timer}', font=("CLIP", 24), fg=ROSE)
    minus_time.place(x=610, y=523)

    #test minus time from song 
    # while song_length > 0:
    #     timer = int(converted_song_length) - int(converted_current_time)
    #     minus_time = Label(root, text=f'{timer}', font=("CLIP", 24), fg=ROSE)
    #     minus_time.place(x=710, y=623)

# Add song Function
# def add_song():
#     song  = filedialog.askopenfilename(initialdir='audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),("mv4 Files","*.mv4"),("mp4 Files", "*.mp4") ))
    
#     # Replace the unecessary path directory to only the song name
#     song = song.replace("/Users/abedelzubaidi/Desktop/all/music/audio/", "")
#     song = song.replace(".mp3", "")
#     song = song.replace(".mv4", "")
#     song = song.replace(".mp4", "")

#     # Add the song at the end of the song box
#     song_box.insert(END, song)
    
    # path = '/Users/abedelzubaidi/Desktop/all/music/audio'
    # if os.path.exists(path):
    #     subprocess.call(["open", path])
    

#Add Many Songs to Playlist
# def add_many_songs():
#     songs = filedialog.askopenfilenames(initialdir='audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),("mv4 Files","*.mv4"),("mp4 Files", "*.mp4") ))
    
#     # Loop to change all the songs names
#     for song in songs:
#         song = song.replace("/Users/abedelzubaidi/Desktop/all/music/audio/", "")
#         song = song.replace(".mp3", "")

#         # Insert into song box
#         song_box.insert(END, song)

def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose Songs", filetypes=(("mp3 Files", "*.mp3"), ("mv4 Files", "*.mv4"), ("mp4 Files", "*.mp4")))
    for song in songs:
        song = os.path.basename(song)  # This will get the file name only
        song, _ = os.path.splitext(song)  # This will remove the file extension
        song_box.insert(END, song)


# PLay Function
def play():
    song = song_box.get(ACTIVE)
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Call the playy_time function to get the lenght of the song
    play_time()

    # Update Slider to Position
    #slide_position = int(song_length)
    #my_slider.config(to=slide_position, value=0)


# Stop playing current song function
# def stop():
#     pygame.mixer.music.stop()
#     song_box.select_clear(ACTIVE)

#     # Clear the Status Bar
#     status_bar.config(text='')

def stop():
    # Stop the music
    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    # Reset the status bar text
    status_bar.config(text='')
    # Reset the slider value
    my_slider.config(value=0)
    # Cancel the scheduled play_time function if needed
    # This part requires you to manage the after schedule ID from the play_time function


# Play the next Song
def next_song():
    # Get the current song number in tuple
    next_one = song_box.curselection()

    # Add one to the current song number
    next_one = next_one[0]+1

    # Get Song title from playlist
    song = song_box.get(next_one)
    
    # Add back the directory to play the next song
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    # Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear the Active Bar in the Playlist
    song_box.select_clear(0, END)

    # Active new Song Bar
    song_box.activate(next_one)

    # Set Active Bar to Next song
    song_box.selection_set(next_one, last=None) 


# Play the previous song in the Playlist
def previous_song():
    # Get the current song number in tuple
    last_one = song_box.curselection()

    # Remove one to the current song number
    last_one = last_one[0]-1

    # Get Song title from playlist
    song = song_box.get(last_one)
    
    # Add back the directory to play the next song
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    # Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    # Clear the Active Bar in the Playlist
    song_box.select_clear(0, END)

    # Active new Song Bar
    song_box.activate(last_one)

    # Set Active Bar to Next song
    song_box.selection_set(last_one, last=None)

# Delete A Song
def delete_song():
    # Take the Selected Song
    song_box.delete(ANCHOR)

    # Stop playing songs
    pygame.mixer.music.stop()


# Delete All Songs from Playlist
def delete_all_songs():
    song_box.delete(0, END)

    # Stop playing songs
    pygame.mixer.music.stop()


# Global pause variable 
global paused
paused = False


# Pause and Unpause the playing song Function
# def pause(is_paused):
#     global paused
#     paused = is_paused

#     if paused:
#         # Unpause
#         pygame.mixer.music.unpause()
#         paused = False
#     else:
#         # Pause
#         pygame.mixer.music.pause()
#         paused = True


def pause(is_paused):
    global paused
    paused = is_paused
    if paused:
        pygame.mixer.music.pause()
        paused = False
    else:
        pygame.mixer.music.unpause()
        paused = True



# Create Slider Function
def slide(x):
    #slider_label.config(text=f'{int(my_slider.get())} of {int(song_length)}')
    
    song = song_box.get(ACTIVE)
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get()))



# Create Playlist Box
song_box = Listbox(root, bg="black", fg="white", width=75, height=20, selectbackground="white", selectforeground="black")
song_box.pack(pady=125)

# Define player Control buttons Images
back_btn_img = PhotoImage(file='./buttons/back.png')
stop_btn_img = PhotoImage(file='./buttons/stop.png')
play_btn_img = PhotoImage(file='/Users/abedelzubaidi/Desktop/all/music/buttons/play.png')
pause_btn_img = PhotoImage(file='/Users/abedelzubaidi/Desktop/all/music/buttons/pause.png')
forward_btn_img = PhotoImage(file='/Users/abedelzubaidi/Desktop/all/music/buttons/forward.png')

# Create player Control Frames
controls_frame = Frame(root)
controls_frame.pack()

# Create player Control Buttons
back_button = Button(controls_frame, image=back_btn_img,borderwidth=0, command=previous_song)
stop_button = Button(controls_frame, image=stop_btn_img,borderwidth=0, command=stop)
play_button = Button(controls_frame, image=play_btn_img,borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img,borderwidth=0, command=lambda: pause(paused))
forward_button = Button(controls_frame, image=forward_btn_img,borderwidth=0, command=next_song)

back_button.grid(row=0, column=0, padx=15)
stop_button.grid(row=0, column=1, padx=15)
play_button.grid(row=0, column=2, padx=15)
pause_button.grid(row=0, column=3, padx=15)
forward_button.grid(row=0, column=4, padx=15)

# Create a Menu
my_menu = Menu(root)
root.config(menu=my_menu)

# Add Song Menu
add_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)
# add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)

# Add many song to playlist
add_song_menu.add_command(label="Add Many Songs to Playlist", command=add_many_songs)

# Create a Delete Song Menu
remove_song_menu = Menu(my_menu)
my_menu.add_cascade(label="Remove Songs", menu=remove_song_menu)
remove_song_menu.add_command(label="Delete A Song from Playlist", command=delete_song)
remove_song_menu.add_command(label="Delete All Songs from Playlist", command=delete_all_songs)

# Create Status Bar 
status_bar = Label(root, text='', bd=1, relief=GROOVE, anchor=E)
status_bar.pack(fill=X, side=BOTTOM, ipady=2)

# Create Music Position Slider 
my_slider = ttk.Scale(root, from_=0, to=100, orient=HORIZONTAL, value=0, length=380, command=slide)
my_slider.pack()
my_slider.place(x=200, y=530)

# Create Temporary Slider label
slider_label = Label(root, text="0")
slider_label.pack(pady=10)

# Music Cloud Label
music_cloud = Label(root, text=" Music Cloud ", font=("CLIP", 63), fg=ROSE, bg='black', borderwidth=3, relief="groove")
music_cloud.place(x=210, y=20)

root.mainloop()

from tkinter import *
from tkinter import filedialog
import pygame
import time
from mutagen.mp3 import MP3
import tkinter.ttk as ttk

root = Tk()
root.title('Music Cloud')
root.iconbitmap('/Users/abedelzubaidi/Desktop/all/music/buttons/play.png')
root.geometry("800x750")

pygame.mixer.init()


# Get Song Time Infos
def play_time():
    if stopped:
        return
    
    # Get the current time 
    current_time = pygame.mixer.music.get_pos() / 1000

    # Convert to time format
    converted_current_time = time.strftime('%M:%S', time.gmtime(current_time))  #to add hours %H:%M:%S

    # Get Song title from playlist
    song = song_box.get(ACTIVE)
    
    # Add back the directory to play the next song
    song = f'./audio/{song}.mp3'    

    # Load Song with Mutagen
    song_mut = MP3(song)

    global song_length
    song_length = song_mut.info.length

    converted_song_length = time.strftime('%M:%S', time.gmtime(song_length))  #to add hours %H:%M:%S

    current_time += 1
    if int(my_slider.get()) == int(song_length):
            status_bar.config(text=f'Time Elapsed: {converted_song_length}')

    elif int(my_slider.get()) == int(current_time):
        # Update Slider to Position
        slide_position = int(song_length)
        my_slider.config(to=slide_position, value=int(current_time))

    elif paused:
        pass
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


    status_bar.config(text=f'Time Elapsed: {converted_current_time} of {converted_song_length}')
    my_slider.config(value=int(current_time))

    status_bar.after(1000, play_time)


def add_song():
    song  = filedialog.askopenfilename(initialdir='audio', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"),("mv4 Files","*.mv4"),("mp4 Files", "*.mp4") ))
    song = song.replace("./audio/", "")
    song = song.replace(".mp3", "")
    song = song.replace(".mv4", "")
    song = song.replace(".mp4", "")
    
    song_box.insert(END, song)


def add_many_songs():
    songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose Songs", filetypes=(("mp3 Files", "*.mp3"), ("mv4 Files", "*.mv4"), ("mp4 Files", "*.mp4")))
    for song in songs:
        song = song.replace("./audio/", "")
        song = song.replace(".mp3", "")
        song = song.replace(".mv4", "")
        song = song.replace(".mp4", "")

        song_box.insert(END, song)
    

def play():
    global stopped
    stopped = False
    song = song_box.get(ACTIVE)
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

    play_time()
    
global stopped
stopped = False

def stop():
    status_bar.config(text='')
    my_slider.config(value=0)

    pygame.mixer.music.stop()
    song_box.select_clear(ACTIVE)
    status_bar.config(text='')
    
    global stopped
    stopped = True
    


# Play the next Song
def next_song():
    status_bar.config(text='')
    my_slider.config(value=0)

    next_one = song_box.curselection()
    next_one = next_one[0]+1
    song = song_box.get(next_one)
    
    # Add back the directory to play the next song
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    # Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.select_clear(0, END)

    song_box.activate(next_one)
    song_box.selection_set(next_one, last=None) 


# Play the previous song in the Playlist
def previous_song():
    status_bar.config(text='')
    my_slider.config(value=0)

    last_one = song_box.curselection()
    last_one = last_one[0]-1
    song = song_box.get(last_one)
    
    # Add back the directory to play the next song
    song = f'/Users/abedelzubaidi/Desktop/all/music/audio/{song}.mp3'

    # Play the song
    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)
    song_box.select_clear(0, END)

    song_box.activate(last_one)
    song_box.selection_set(last_one, last=None)


# Delete A Song
def delete_song():
    stop()
    song_box.delete(ANCHOR)
    pygame.mixer.music.stop()


# Delete All Songs from Playlist
def delete_all_songs():
    stop()
    song_box.delete(0, END)
    pygame.mixer.music.stop()

   
# Global pause variable
global paused
paused = False

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
    song = song_box.get(ACTIVE)
    song = f'./audio/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0, start=int(my_slider.get())) 


# Create Playlist Box
song_box = Listbox(root, bg="black", fg="white", width=75, height=20, selectbackground="white", selectforeground="black")
song_box.pack(pady=125)

# Define player Control buttons Images
back_btn_img = PhotoImage(file='./buttons/back.png')
stop_btn_img = PhotoImage(file='./buttons/stop.png')
play_btn_img = PhotoImage(file='./buttons/play.png')
pause_btn_img = PhotoImage(file='./buttons/pause.png')
forward_btn_img = PhotoImage(file='./buttons/forward.png')

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
add_song_menu.add_command(label="Add One Song to Playlist", command=add_song)

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

root.mainloop()

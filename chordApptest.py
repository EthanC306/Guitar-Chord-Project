#Guitar Chord Application
#Author: Ethan Claybourn
#Date: 2/17/2026

#This application allows user to :
# randomly generate a chord
# see the name of the chord
# see the fingering pattern for the chord

import tkinter as tk
import customtkinter as Ctk
import random
from PIL import Image
import os

# Set appearance mode
Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

# Get the directory where this script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Create the main application window
app = Ctk.CTk()
app.title("Guitar Chord Picker App")
app.geometry("800x600")

# Title label
title_label = Ctk.CTkLabel(master=app, text="Guitar Chord Picker", font=("Melt Swashes", 56, "bold"))
title_label.pack(pady=20)

# Frame to hold two chords side by side
chords_frame = Ctk.CTkFrame(master=app)
chords_frame.pack(pady=20, padx=20, fill="both", expand=True)

# Chord 1 frame (left side)
chord1_frame = Ctk.CTkFrame(master=chords_frame)
chord1_frame.pack(side="left", padx=10, fill="both", expand=True)

chord1_label = Ctk.CTkLabel(master=chord1_frame, text="", font=("Melt Swashes", 32))
chord1_label.pack(pady=5)

fingering1_label = Ctk.CTkLabel(master=chord1_frame, text="", font=("Melt Swashes", 32))
fingering1_label.pack(pady=5)

image1_label = Ctk.CTkLabel(master=chord1_frame, text="")
image1_label.pack(pady=10, expand=True)

# Chord 2 frame (right side)
chord2_frame = Ctk.CTkFrame(master=chords_frame)
chord2_frame.pack(side="right", padx=10, fill="both", expand=True)

chord2_label = Ctk.CTkLabel(master=chord2_frame, text="", font=("Melt Swashes", 32))
chord2_label.pack(pady=5)

fingering2_label = Ctk.CTkLabel(master=chord2_frame, text="", font=("Melt Swashes", 32))
fingering2_label.pack(pady=5)

image2_label = Ctk.CTkLabel(master=chord2_frame, text="")
image2_label.pack(pady=10, expand=True)
#
# Dictionary of chords and their fingering patterns (tab notation)
fingering_patterns = {
    "C Major": "x32010",
    "G Major": "320003",
    "D Major": "xx0232",
    "A Major": "x02220",
    "E Major": "022100",
    "A Minor": "x02210",
    "E Minor": "022000",
    "D Minor": "xx0231",
}
image_paths = {
    "C Major": os.path.join(script_dir, "images/C_major.png"),
    "G Major": os.path.join(script_dir, "images/G_major.png"),
    "D Major": os.path.join(script_dir, "images/D_major.png"),
    "A Major": os.path.join(script_dir, "images/A_major.png"),
    "E Major": os.path.join(script_dir, "images/E_major.png"),
    "A Minor": os.path.join(script_dir, "images/A_minor.png"),
    "E Minor": os.path.join(script_dir, "images/E_minor.png"),
    "D Minor": os.path.join(script_dir, "images/D_minor.png"),
}

# List of chord names
chords = list(fingering_patterns.keys())
images = list(image_paths.values())

# Function to generate two random chords
def generate_chord():
    try:
        # Generate two different random chords
        random_chords = random.sample(chords, 2)
        chord1 = random_chords[0]
        chord2 = random_chords[1]
        
        # Update chord 1
        chord1_label.configure(text=f"Play: {chord1}")
        fingering1_label.configure(text=f"Fingering: {fingering_patterns[chord1]}")
        
        image_path1 = image_paths[chord1]
        print(f"Loading image 1 from: {image_path1}")
        chord_image1 = Image.open(image_path1)
        chord_image1 = chord_image1.resize((200, 200), Image.Resampling.LANCZOS)
        chord_photo1 = Ctk.CTkImage(chord_image1, size=(200, 200))
        image1_label.configure(image=chord_photo1)
        image1_label.image = chord_photo1
        
        # Update chord 2
        chord2_label.configure(text=f"Play: {chord2}")
        fingering2_label.configure(text=f"Fingering: {fingering_patterns[chord2]}")
        
        image_path2 = image_paths[chord2]
        print(f"Loading image 2 from: {image_path2}")
        chord_image2 = Image.open(image_path2)
        chord_image2 = chord_image2.resize((200, 200), Image.Resampling.LANCZOS)
        chord_photo2 = Ctk.CTkImage(chord_image2, size=(200, 200))
        image2_label.configure(image=chord_photo2)
        image2_label.image = chord_photo2
        
        print(f"Images loaded successfully: {chord1} and {chord2}")
    except Exception as e:
        print(f"Error loading images: {e}")
        chord1_label.configure(text=f"Error: {str(e)}")
        chord2_label.configure(text=f"Error: {str(e)}")

# Button to generate random chord
btn = Ctk.CTkButton(master=app, text="Generate Random Chord", corner_radius=10, fg_color="black",
                    hover_color="lightgray", command=generate_chord,)
btn.pack(pady=20)

# Start the application
app.mainloop()



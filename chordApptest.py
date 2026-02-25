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

# Set appearance mode
Ctk.set_appearance_mode("dark")
Ctk.set_default_color_theme("blue")

# Create the main application window
app = Ctk.CTk()
app.title("Guitar Chord Picker App")
app.geometry("500x400")

# Title label
title_label = Ctk.CTkLabel(master=app, text="Guitar Chord Picker", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

# Label to display the chord name
chord_label = Ctk.CTkLabel(master=app, text="Click 'Generate Chord' to start", font=("Arial", 16))
chord_label.pack(pady=10)

# Label to display the fingering pattern
fingering_label = Ctk.CTkLabel(master=app, text="", font=("Courier", 14))  # Monospace for tab
fingering_label.pack(pady=10)

# Label to display the chord image
image_label = Ctk.CTkLabel(master=app)
image_label.pack(pady=10)
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
    "C Major": "images/C_major.png",
    "G Major": "images/G_major.png",
    "D Major": "images/D_major.png",
    "A Major": "images/A_major.png",
    "E Major": "images/E_major.png",
    "A Minor": "images/A_minor.png",
    "E Minor": "images/E_minor.png",
    "D Minor": "images/D_minor.png",
}

# List of chord names
chords = list(fingering_patterns.keys())
images = list(image_paths.values())

# Function to generate a random chord
def generate_chord():
    random_chord = random.choice(chords)
    random_image = random.choice(images)
    chord_label.configure(text=f"Play this chord: {random_chord}")
    image_label.configure(image=chord_photo)
    fingering_label.configure(text=f"Fingering: {fingering_patterns[random_chord]}")

    # Load and display the chord image
    image_path = image_paths[random_chord]
    chord_image = Image.open(image_path)
    chord_image = chord_image.resize((200, 200), Image.ANTIALIAS)
    chord_photo = Ctk.CTkImage(chord_image)
    
    image_label.image = chord_photo  # Keep a reference to prevent garbage collection

# Button to generate random chord
btn = Ctk.CTkButton(master=app, text="Generate Random Chord", corner_radius=10, fg_color="black",
                    hover_color="lightgray", command=generate_chord,)
btn.pack(pady=20)

# Start the application
app.mainloop()



#Guitar Chord Application
#Author: Ethan Claybourn
#Date: 2/17/2026

#This application allows user to :
# randomly generate a chord 
# see the name of the chord
# see the fingering pattern for the chord



#-------------------------------------
# THIS IS THE GUI PROTOTYPE, NOT FUNCTIONAL YET
#-------------------------------------
#import tkinter as tk
#window = tk.Tk()
#label = tk.Label(text="Welcome to the Guitar Chord Picker App!")
#label.pack()
#window.mainloop()

#window.title("Guitar Chord Picker App")
#window.geometry("400x300")
#-------------------------------------
#WORKING PROTOTYPE WITHOUT GUI 
#-------------------------------------

print("Welcome to the Guitar Chord Picker App!")
print("This application will randomly generate a guitar chord for you to play.")
print("Let's get started!")

print("Generating a random chord...")

# Here we  have code to randomly select a chord from a list of chords
# For example:
import random
chords = ["C Major", "G Major", "D Major", "A Minor", "E Minor"]
random_chord = random.choice(chords)



print(f"The chord you should play is: {random_chord}")
print("Here is the fingering pattern for the chord:")

# Here we have code to display the fingering pattern for the selected chord
# For example:
fingering_patterns = {
    "C Major": "x32010",
    "G Major": "320003",
    "D Major": "xx0232",
    "A Minor": "x02210",
    "E Minor": "022000"
}
print(fingering_patterns[random_chord])
print("Enjoy playing your chord!")



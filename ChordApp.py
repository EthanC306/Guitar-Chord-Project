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

import tkinter as tk
import customtkinter as Ctk

app = Ctk.CTk()
#window = tk.Tk()
#window.geometry("400x300")
app.title("Guitar Chord Picker App")
app.geometry("400x300")

Ctk.set_appearance_mode("dark")

btn = Ctk.CTkButton(master=app, text="Generate Random Chord", corner_radius=10, fg_color="black",
                    hover_color="lightgray",)
btn.place(relx=0.5, rely=0.5, anchor="center")
app.mainloop()
# app = CT


# label = tk.Label(text="Welcome to the Guitar Chord Picker App!")
# label.pack()




# #Add a button to generate a random chord
# generate_button = tk.Button(text="Generate Random Chord")
# generate_button.pack()

#Add functionality to the button to display the name of the chord and the fingering pattern when clicked
def generate_chord():
    import random
chords = ["C Major", "G Major", "D Major", "A Minor", "E Minor"]
random_chord = random.choice(chords)
chord_label.config(text=f"The chord you should play is: {random_chord}")
fingering_patterns = {
        "C Major": "x32010",
        "G Major": "320003",
        "D Major": "xx0232",
        "A Minor": "x02210",
        "E Minor": "022000"
    }
    
fingering_label.config(text=f"Fingering pattern: {fingering_patterns[random_chord]}")

# generate_button.config(command=generate_chord)
# chord_label = tk.Label(text="")
# chord_label.pack()
# fingering_label = tk.Label(text="")
# fingering_label.pack()
# window.mainloop()







# #-------------------------------------
# #WORKING PROTOTYPE WITHOUT GUI 
# #-------------------------------------

# print("Welcome to the Guitar Chord Picker App!")
# print("This application will randomly generate a guitar chord for you to play.")
# print("Let's get started!")

# print("Generating a random chord...")

# # Here we  have code to randomly select a chord from a list of chords
# # For example:

# import random
# chords = ["C Major", "G Major", "D Major", "A Minor", "E Minor"]
# random_chord = random.choice(chords)



# print(f"The chord you should play is: {random_chord}")
# print("Here is the fingering pattern for the chord:")

# # Here we have code to display the fingering pattern for the selected chord
# # For example:
# fingering_patterns = {
#     "C Major": "x32010",
#     "G Major": "320003",
#     "D Major": "xx0232",
#     "A Minor": "x02210",
#     "E Minor": "022000"
# }
# print(fingering_patterns[random_chord])
# print("Enjoy playing your chord!")



import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import random

# File paths for assets
ASSETS_PATH = "E:/py-misa/assets/"
BACKGROUND_IMG = ASSETS_PATH + "background.jpg"
ROCK_IMG = ASSETS_PATH + "rock_button.png"
PAPER_IMG = ASSETS_PATH + "paper_button.png"
SCISSORS_IMG = ASSETS_PATH + "scissors_button.png"
EXIT_IMG = ASSETS_PATH + "exit.png"
WIN_IMG = ASSETS_PATH + "win.png"
LOSE_IMG = ASSETS_PATH + "lose.png"
TIE_IMG = ASSETS_PATH + "tie.png"

# Function to determine the winner
def determine_winner(player_choice, misa_choice):
    if player_choice == misa_choice:
        return "tie"
    elif (
        (player_choice == "rock" and misa_choice == "scissors") or
        (player_choice == "paper" and misa_choice == "rock") or
        (player_choice == "scissors" and misa_choice == "paper")
    ):
        return "win"
    else:
        return "lose"

# Main game logic
def play_game(player_choice):
    misa_choice = random.choice(["rock", "paper", "scissors"])
    result = determine_winner(player_choice, misa_choice)

    # Update result images
    if result == "win":
        result_img = win_image
    elif result == "lose":
        result_img = lose_image
    else:
        result_img = tie_image

    # Update labels
    result_label.config(image=result_img)
    result_label.image = result_img
    misa_label.config(text=f"Misa chose: {misa_choice.capitalize()}")

# Exit game
def exit_game():
    root.quit()

# Initialize Tkinter window
root = tk.Tk()
root.title("Rock Paper Scissors - Misa Game")
root.geometry("800x600")

# Background image
background_image = ImageTk.PhotoImage(Image.open(BACKGROUND_IMG).resize((800, 600)))
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Buttons
rock_image = ImageTk.PhotoImage(Image.open(ROCK_IMG).resize((150, 150)))
paper_image = ImageTk.PhotoImage(Image.open(PAPER_IMG).resize((150, 150)))
scissors_image = ImageTk.PhotoImage(Image.open(SCISSORS_IMG).resize((150, 150)))
exit_image = ImageTk.PhotoImage(Image.open(EXIT_IMG).resize((100, 50)))

button_style = {"bd": 5, "relief": "solid"}  # Black thick border for buttons

# Rock, Paper, Scissors buttons with spacing
rock_button = tk.Button(root, image=rock_image, command=lambda: play_game("rock"), **button_style)
rock_button.place(x=150, y=350)  # Left button

paper_button = tk.Button(root, image=paper_image, command=lambda: play_game("paper"), **button_style)
paper_button.place(x=325, y=350)  # Centered button

scissors_button = tk.Button(root, image=scissors_image, command=lambda: play_game("scissors"), **button_style)
scissors_button.place(x=500, y=350)  # Right button

# Exit button in the top-right corner
exit_button = tk.Button(root, image=exit_image, command=exit_game, **button_style)
exit_button.place(x=700, y=10)

# Result images
win_image = ImageTk.PhotoImage(Image.open(WIN_IMG).resize((200, 100)))
lose_image = ImageTk.PhotoImage(Image.open(LOSE_IMG).resize((200, 100)))
tie_image = ImageTk.PhotoImage(Image.open(TIE_IMG).resize((200, 100)))

result_label = tk.Label(root, image=None, bg="white")
result_label.place(x=300, y=50)  # Displayed at the top

# Misa's choice section
misa_label = tk.Label(
    root,
    text="",
    font=("Arial", 16, "bold"),
    bg="grey",
    fg="black",
    relief="solid",
    bd=2,  # Black border
    padx=10,
    pady=5
)
misa_label.place(x=300, y=200)  # Below the result display

# Run the GUI loop
root.mainloop()
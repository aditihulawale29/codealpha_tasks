import tkinter as tk
import random

# Predefined list of words
WORDS = ["python", "hangman", "programming", "challenge", "computer", "interface", "optimize", "algorithm","codealpha"]

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        
        # Game variables
        self.word = random.choice(WORDS).upper()
        self.guessed = set()
        self.chances = 6
        
        # GUI Elements
        self.word_display = tk.Label(root, text=self.get_display_word(), font=("Helvetica", 24))
        self.word_display.pack(pady=20)
        
        self.message = tk.Label(root, text="Guess a letter:", font=("Helvetica", 16))
        self.message.pack()
        
        self.input_box = tk.Entry(root, font=("Helvetica", 18), justify="center")
        self.input_box.pack()
        self.input_box.bind("<Return>", self.make_guess)
        
        self.hangman_display = tk.Label(root, text=self.get_hangman_graphic(), font=("Courier", 24))
        self.hangman_display.pack(pady=20)
        
        self.restart_button = tk.Button(root, text="Restart", font=("Helvetica", 14), command=self.restart_game)
        self.restart_button.pack()
        
    def get_display_word(self):
        return " ".join([letter if letter in self.guessed else "_" for letter in self.word])
    
    def get_hangman_graphic(self):
        stages = [
            """
               ------
               |    |
               |    
               |   
               |    
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   
               |    
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |    |
               |    
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|
               |    
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |    
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / 
               |
            --------
            """,
            """
               ------
               |    |
               |    O
               |   /|\\
               |   / \\
               |
            --------
            """,
        ]
        return stages[6 - self.chances]
    
    def make_guess(self, event):
        guess = self.input_box.get().upper()
        self.input_box.delete(0, tk.END)
        
        if len(guess) == 1 and guess.isalpha():
            if guess in self.guessed:
                self.message.config(text="You already guessed that letter.")
            elif guess in self.word:
                self.guessed.add(guess)
                self.message.config(text="Correct guess!")
            else:
                self.guessed.add(guess)
                self.chances -= 1
                self.message.config(text="Incorrect guess.")
            
            self.update_display()
        else:
            self.message.config(text="Please enter a single letter.")
    
    def update_display(self):
        self.word_display.config(text=self.get_display_word())
        self.hangman_display.config(text=self.get_hangman_graphic())
        
        if "_" not in self.get_display_word():
            self.message.config(text="Congratulations! You won!")
            self.input_box.config(state="disabled")
        elif self.chances == 0:
            self.message.config(text=f"You lost! The word was: {self.word}")
            self.input_box.config(state="disabled")
    
    def restart_game(self):
        self.word = random.choice(WORDS).upper()
        self.guessed.clear()
        self.chances = 6
        self.input_box.config(state="normal")
        self.update_display()
        self.message.config(text="Guess a letter:")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

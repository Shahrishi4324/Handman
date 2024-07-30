import tkinter as tk
from tkinter import messagebox

class HangmanGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Hangman Game")
        self.root.geometry("600x400")
        self.root.resizable(False, False)

        self.canvas = tk.Canvas(root, width=200, height=200, bg="white")
        self.canvas.place(x=50, y=50)

        self.word_label = tk.Label(root, text="", font=("Arial", 24))
        self.word_label.place(x=300, y=100)

        self.entry = tk.Entry(root, font=("Arial", 18))
        self.entry.place(x=300, y=200)

        self.guess_button = tk.Button(root, text="Guess", command=self.guess_letter, font=("Arial", 18))
        self.guess_button.place(x=450, y=200)

        self.words = ["PYTHON", "JAVA", "KOTLIN", "JAVASCRIPT"]
        self.secret_word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.secret_word)
        self.attempts = 6
        self.guessed_letters = []

        self.update_display()

    def update_display(self):
        self.word_label.config(text=" ".join(self.guessed_word))
        self.canvas.delete("all")
        self.draw_hangman()

    def guess_letter(self):
        letter = self.entry.get().upper()
        self.entry.delete(0, tk.END)

        if not letter.isalpha() or len(letter) != 1:
            messagebox.showwarning("Invalid Input", "Please enter a single alphabet letter.")
            return

        if letter in self.guessed_letters:
            messagebox.showinfo("Already Guessed", "You already guessed this letter.")
            return

        self.guessed_letters.append(letter)
        if letter in self.secret_word:
            for i, char in enumerate(self.secret_word):
                if char == letter:
                    self.guessed_word[i] = letter
        else:
            self.attempts -= 1

        self.update_display()
        self.check_game_over()

    def draw_hangman(self):
        parts = [
            lambda: self.canvas.create_line(50, 180, 150, 180, width=3),  # Base
            lambda: self.canvas.create_line(100, 180, 100, 50, width=3),  # Pole
            lambda: self.canvas.create_line(100, 50, 150, 50, width=3),   # Top bar
            lambda: self.canvas.create_line(150, 50, 150, 70, width=3),   # Rope
            lambda: self.canvas.create_oval(140, 70, 160, 90, width=3),   # Head
            lambda: self.canvas.create_line(150, 90, 150, 130, width=3),  # Body
            lambda: self.canvas.create_line(150, 100, 130, 110, width=3), # Left arm
            lambda: self.canvas.create_line(150, 100, 170, 110, width=3), # Right arm
            lambda: self.canvas.create_line(150, 130, 130, 150, width=3), # Left leg
            lambda: self.canvas.create_line(150, 130, 170, 150, width=3)  # Right leg
        ]
        for i in range(6 - self.attempts):
            parts[i]()

    def check_game_over(self):
        if self.attempts == 0:
            messagebox.showinfo("Game Over", f"You lost! The word was: {self.secret_word}")
            self.reset_game()
        elif "_" not in self.guessed_word:
            messagebox.showinfo("Congratulations", "You guessed the word!")
            self.reset_game()

    def reset_game(self):
        self.secret_word = random.choice(self.words)
        self.guessed_word = ["_"] * len(self.secret_word)
        self.attempts = 6
        self.guessed_letters = []
        self.update_display()

def main():
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()

if __name__ == "__main__":
    main()
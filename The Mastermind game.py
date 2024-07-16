import tkinter as tk
from tkinter import messagebox

class MastermindGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Mastermind Game")

        self.secret_number = ""
        self.attempts = 0
        self.max_digits = 4

        self.create_instruction_page()
        self.create_game_page()
        self.show_instruction_page()

    def create_instruction_page(self):
        self.instruction_page = tk.Toplevel(self.root)
        self.instruction_page.title("Instructions")
        self.instruction_page.geometry("600x400")
        self.instruction_page.withdraw()  # Hide instruction page initially

        font_large = ("Helvetica", 16)
        font_medium = ("Helvetica", 14)

        # Instructions Text
        instruction_text = """
Welcome to Mastermind!

Player 1 will set a secret 4-digit number.
Player 2 will guess the number.

After Player 1 sets the number, Player 2 will start guessing.
Player 2 will enter a 4-digit number in the guess box and click 'Guess'.

For each guess:
- A number in blue means it's correct but in the wrong position.
- A number in green means it's correct and in the correct position.

Player 2 continues guessing until they correctly guess the number.
Player 2 wins if they guess in fewer attempts than Player 1.

Have fun playing Mastermind!
        """
        instruction_label = tk.Label(self.instruction_page, text=instruction_text, font=("Helvetica", 12), justify='center')
        instruction_label.pack(pady=20)

        start_button = tk.Button(self.instruction_page, text="Start Game", command=self.show_game_page, font=font_medium)
        start_button.pack(pady=20)

    def show_instruction_page(self):
        self.instruction_page.deiconify()  # Show instruction page
        self.root.withdraw()  # Hide main game window

    def show_game_page(self):
        self.instruction_page.withdraw()  # Hide instruction page
        self.root.deiconify()  # Show main game window

    def create_game_page(self):
        font_large = ("Helvetica", 16)
        font_medium = ("Helvetica", 14)

        # Game elements in the main root window
        self.instructions_game = tk.Label(self.root, text="Player 1, set a secret number (4 digits):", font=font_large)
        self.instructions_game.pack(pady=10)

        self.secret_entry = tk.Entry(self.root, show="*", font=font_medium)
        self.secret_entry.pack(pady=5)

        self.set_button = tk.Button(self.root, text="Set Number", command=self.set_number, font=font_medium)
        self.set_button.pack(pady=5)

        self.guess_label = tk.Label(self.root, text="", font=font_large)
        self.guess_label.pack(pady=10)

        self.guess_entry = tk.Entry(self.root, font=font_medium, state='disabled')  # Initially disabled
        self.guess_entry.pack(pady=5)

        self.guess_button = tk.Button(self.root, text="Guess", command=self.make_guess, font=font_medium, state='disabled')  # Initially disabled
        self.guess_button.pack(pady=5)

        self.create_table()

    def create_table(self):
        self.table_frame = tk.Frame(self.root)
        self.table_frame.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

        self.scrollbar = tk.Scrollbar(self.table_frame)
        self.scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        self.table = tk.Text(self.table_frame, height=10, width=40, wrap=tk.NONE, yscrollcommand=self.scrollbar.set, font=("Helvetica", 16))
        self.table.pack(fill=tk.BOTH, expand=True)
        self.scrollbar.config(command=self.table.yview)

        self.table.tag_configure("center", justify='center')
        self.table.tag_configure("correct_place", foreground="green")
        self.table.tag_configure("correct_number", foreground="blue")

        # Disable text editing
        self.table.config(state='disabled')

    def set_number(self):
        self.secret_number = self.secret_entry.get()
        if len(self.secret_number) == self.max_digits and self.secret_number.isdigit():
            self.instructions_game.config(text="Player 1's secret number:")
            self.secret_entry.config(state='disabled')
            self.set_button.config(state='disabled')
            self.guess_label.config(text="Player 2, guess the number:")
            self.guess_entry.config(state='normal')  # Enable guess entry
            self.guess_button.config(state='normal')  # Enable guess button
            self.table.config(state='normal')
            self.table.insert(tk.END, f"Secret Number: {self.secret_number}\n")
            self.table.config(state='disabled')
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")

    def make_guess(self):
        guess = self.guess_entry.get()
        if len(guess) == self.max_digits and guess.isdigit():
            self.attempts += 1
            if guess == self.secret_number:
                messagebox.showinfo("Congratulations!", f"You guessed the number in {self.attempts} attempts!")
                self.reset_game()
            else:
                self.display_guess_with_feedback(guess)
                self.guess_entry.delete(0, 'end')
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid 4-digit number.")

    def display_guess_with_feedback(self, guess):
        formatted_guess = ""
        for i, digit in enumerate(guess):
            if digit == self.secret_number[i]:
                formatted_guess += f"{digit} "
            elif digit in self.secret_number:
                formatted_guess += f"{digit} "
            else:
                formatted_guess += f"{digit} "

        start_index = self.table.index("end-1c")
        self.table.config(state='normal')  # Enable editing temporarily to insert text
        self.table.insert(tk.END, formatted_guess + "\n")
        end_index = self.table.index("end-1c")
        self.table.config(state='disabled')  # Disable editing again

        self.table.tag_add("center", start_index, end_index)
        for i, digit in enumerate(guess):
            if digit == self.secret_number[i]:
                self.table.tag_add("correct_place", f"{self.attempts}.{i*2}", f"{self.attempts}.{i*2+1}")
            elif digit in self.secret_number:
                self.table.tag_add("correct_number", f"{self.attempts}.{i*2}", f"{self.attempts}.{i*2+1}")

    def reset_game(self):
        self.secret_number = ""
        self.attempts = 0
        self.secret_entry.config(state='normal')
        self.secret_entry.delete(0, 'end')
        self.set_button.config(state='normal')
        self.instructions_game.config(text="Player 1, set a secret number (4 digits):")
        self.guess_label.config(text="")
        self.guess_entry.config(state='disabled')  # Disable guess entry
        self.guess_entry.delete(0, 'end')
        self.guess_button.config(state='disabled')  # Disable guess button
        self.table.config(state='normal')  # Enable editing temporarily to clear text
        self.table.delete(1.0, tk.END)
        self.table.config(state='disabled')  # Disable editing again

if __name__ == "__main__":
    root = tk.Tk()
    game = MastermindGame(root)
    root.mainloop()

import tkinter as tk
import random

class QuotesGenerator:
    def __init__(self, master):
        self.master = master

        self.quotes = [
            "The best way to predict the future is to create it.",
            "You miss 100% of the shots you don't take.",
            "Life is what happens when you're busy making other plans.",
            "Get busy living or get busy dying."
        ]

        self.quote_label = tk.Label(master, text="", wraplength=300, font=('Arial', 14))
        self.quote_label.pack(pady=20)

        self.generate_button = tk.Button(master, text="Generate Quote", command=self.generate_quote)
        self.generate_button.pack(pady=5)

    def generate_quote(self):
        quote = random.choice(self.quotes)
        self.quote_label.config(text=quote)

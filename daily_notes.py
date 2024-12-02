import tkinter as tk

class DailyNotes:
    def __init__(self, root):
        self.frame = root  
        self.create_ui()

    def create_ui(self):
        label = tk.Label(self.frame, text="Daily Notes", font=("Arial", 16))
        label.pack(pady=20)

        self.text_area = tk.Text(self.frame, height=10, width=50)
        self.text_area.pack(pady=10)

        save_button = tk.Button(self.frame, text="Save Notes", command=self.save_notes)
        save_button.pack(pady=10)

    def save_notes(self):
        notes = self.text_area.get("1.0", tk.END)
        with open("daily_notes.txt", "w") as file:
            file.write(notes)

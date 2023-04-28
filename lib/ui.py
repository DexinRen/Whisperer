import tkinter as tk

class ChatAppUI:
    def __init__(self):
        self.window = tk.Tk()
        self.history = []
        self.notes = {}

        # Chat history window
        self.history_frame = tk.Frame(self.window)
        self.history_scrollbar = tk.Scrollbar(self.history_frame)
        self.history_scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.history_text = tk.Text(self.history_frame, height=20, width=50, yscrollcommand=self.history_scrollbar.set)
        self.history_text.pack(side=tk.LEFT, fill=tk.BOTH)
        self.history_frame.pack()

        # Text input bar
        self.input_frame = tk.Frame(self.window)
        self.input_text = tk.Entry(self.input_frame, width=50)
        self.input_text.pack(side=tk.LEFT)
        self.send_button = tk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.LEFT)
        self.input_frame.pack()

        # Notes sidebar
        self.notes_frame = tk.Frame(self.window)
        self.notes_text = tk.Text(self.notes_frame, height=20, width=30)
        self.notes_text.pack(side=tk.LEFT, fill=tk.BOTH)
        self.new_note_button = tk.Button(self.notes_frame, text="New Note", command=self.create_note)
        self.new_note_button.pack(side=tk.BOTTOM)
        self.notes_frame.pack(side=tk.RIGHT)

        # Start the GUI loop
        self.window.mainloop()

    def send_message(self):
        message = self.input_text.get()
        self.history.append(("User", message))
        # TODO: Send message to responder and get response
        # response = ...
        # self.history.append(("Responder", response))
        self.update_history()

    def update_history(self):
        self.history_text.delete(1.0, tk.END)
        for sender, message in self.history:
            self.history_text.insert(tk.END, f"{sender}: {message}\n")
        self.history_text.see(tk.END)

    def create_note(self):
        note_title = tk.simpledialog.askstring("Note Title", "Enter a title for your note:")
        if note_title:
            note_text = self.notes_text.get(1.0, tk.END)
            self.notes[note_title] = note_text
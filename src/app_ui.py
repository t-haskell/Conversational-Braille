import tkinter as tk
from tkinter import messagebox
import threading
from audio.record_audio import record_audio
from audio.transcribe import transcribe_audio
from braille.text_to_braille import text_to_braille
from braille.save_braille import save_braille
class AudioTranscriptionApp:
    def __init__(self, root):
        self.save_conversation = False
        self.root = root
        self.root.title("Real-Time Audio to Braille Transcription")
        self.root.geometry("600x600")

        # Variables to store transcription and braille output
        self.transcription_text = tk.StringVar()
        self.braille_text = tk.StringVar()
        
        # Header
        header = tk.Label(root, text="Audio to Braille Transcription", font=("Arial", 16))
        header.pack(pady=10)
        #frame for record/save
        frame = tk.Frame(root)
        frame.pack(pady=40)
          # Create the "Start Recording" button (left-aligned in the frame)
        self.start_button = tk.Button(frame, text="Start Recording", command=self.start_recording, font=("Arial", 16), bg="green", fg="white")
        self.start_button.pack(side=tk.LEFT, padx=10)  # Side-left and padding for spacing

          
        self.stop_button = tk.Button(frame, text="Stop Recording", command=self.stop_recording, font=("Arial", 16), bg="red", fg="white", state="disabled")
        self.stop_button.pack(pady=5,side=tk.LEFT, padx=10)
        # Create the toggle button for saving conversation (right-aligned in the frame)
        self.toggle_button = tk.Button(frame, text="OFF", command=self.toggle_save, width=10, height=2)
        self.toggle_button.pack(side=tk.RIGHT, padx=20)
        # Display for transcription text
        tk.Label(root, text="Transcription:", font=("Arial", 24)).pack(pady=(10, 2))
        self.transcription_label = tk.Label(root, textvariable=self.transcription_text, wraplength=450, font=("Arial", 16), relief="sunken", bg="lightyellow", fg="black", height=4)
        self.transcription_label.pack(fill="both", padx=10, pady=5)

        # Display for braille output
        tk.Label(root, text="Braille Output:", font=("Arial", 24)).pack(pady=(10, 2))
        self.braille_label = tk.Label(root, textvariable=self.braille_text, wraplength=450, font=("Arial", 16), relief="sunken", bg="lightblue", fg="black", height=4)
        self.braille_label.pack(fill="both", padx=10, pady=5)
    def toggle_save(self):
        """Toggle the state between On and Off"""
        if self.save_conversation:
            self.save_conversation = False
            self.toggle_button.config(text="OFF", bg="red")  # Change button to OFF state
        else:
            self.save_conversation = True
            self.toggle_button.config(text="ON", bg="green")  # Change button to ON state

    def start_recording(self):
        # Update button states
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        
        # Start recording in a separate thread to avoid freezing the UI
        threading.Thread(target=lambda: record_audio("output.wav", duration=5)).start()
        
    def stop_recording(self):
        # Stop recording and process audio
        self.stop_button.config(state="disabled")
        self.start_button.config(state="normal")

        
        # Start transcription in a separate thread to keep UI responsive
        threading.Thread(target=self.process_audio).start()
        
    def process_audio(self):
        try:
            # Transcribe audio and convert to braille
            # transcription = transcribe_audio("output.wav")
            transcription = "Hello my name is Tommy!"
            braille = text_to_braille(transcription)
            save_braille("test",transcription,self.save_conversation)
            # Update text variables (for display)
            self.transcription_text.set(transcription)
            self.braille_text.set(braille)
        
        except Exception as e:
            # Display error message if transcription fails
            messagebox.showerror("Error", f"An error occurred: {e}")
            self.transcription_text.set("Error transcribing audio.")
            self.braille_text.set("")

# Initialize the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = AudioTranscriptionApp(root)
    root.mainloop()

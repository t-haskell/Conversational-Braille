import time
import tkinter as tk
from tkinter import messagebox
import threading
import sounddevice as sd
from braille.get_conversations import get_conversations
from audio.record_audio import record_audio
from audio.transcribe import transcribe_audio
from braille.text_to_braille import text_to_braille
from braille.save_braille import save_braille
class AudioTranscriptionApp:
    def __init__(self, root):
        self.save_conversation = False
        self.root = root
        self.root.configure(bg="white")
        self.root.title("Real-Time Audio to Braille Transcription")
        self.root.geometry("600x700")

        # Variables to store transcription and braille output
        self.transcription_text = tk.StringVar()
        self.braille_text = tk.StringVar()
        self.transcription_time = tk.StringVar()
        self.transcription_time.set("Transcription Time: 0.00s")
        tk.Label(root, textvariable=self.transcription_time, font=("Arial", 10), bg="white", fg="black").place(relx=0.8, rely=0.05, anchor="ne")
        
        # Header
        header = tk.Label(root, text="Audio to Braille Transcription", font=("Arial", 16), bg="white", fg="black")
        header.pack(pady=10)
        #frame for record/save
        frame = tk.Frame(root, bg="white", height=200)
        frame.pack(pady=40)

        #frame for bringing up previous conversations
        frame2 = tk.Frame(root, bg="white")
        frame2.pack(pady=40)
          # Create the "Start Recording" button (left-aligned in the frame)
        # Create a canvas for the start button (circle)
        self.start_canvas = tk.Canvas(frame, width=60, height=60, bg="white", highlightthickness=0)
        self.start_canvas.create_oval(5, 5, 45, 45, fill="green", outline="darkgreen")
        self.start_canvas.create_text(25, 25, text="Start", fill="white", font=("Arial", 10))  # Add text inside the circle
        self.start_canvas.bind("<Button-1>", lambda event: self.start_recording())  # Bind Start Recording
        self.start_button = tk.Button(frame, text="Start", command=self.start_recording, font=("Arial", 16), bg="green", activebackground="darkgreen", fg="white", borderwidth=0)
        self.start_button_window = self.start_canvas.create_window(30, 60, window=self.start_button)

        self.start_canvas.pack(side=tk.LEFT, padx=10)  # Side-left and padding for spacing

        # Create a canvas for the stop button (square)
        self.stop_canvas = tk.Canvas(frame, width=60, height=60, bg="white", highlightthickness=0)
        self.stop_canvas.create_rectangle(5, 5, 45, 45, fill="red", outline="darkred")
        self.stop_canvas.create_text(25, 25, text="Stop", fill="white", font=("Arial", 10))  # Add text inside the square
        self.stop_canvas.bind("<Button-1>", lambda event: self.stop_recording())  # Bind Stop Recording
        self.stop_canvas.unbind("<Button-1>")  # Initially disable Stop button
        self.stop_button = tk.Button(frame, text="Stop", command=self.stop_recording, font=("Arial", 16), bg="red", activebackground="darkred", fg="white", borderwidth=0)
        self.stop_button_window = self.stop_canvas.create_window(30, 60, window=self.stop_button)

        self.stop_canvas.pack(side=tk.LEFT, padx=30)  # Side-left and padding for spacing
        # Create the toggle button for saving conversation (right-aligned in the frame)
        header = tk.Label(frame, text="Save", font=("Arial", 16), bg="white", activebackground="black", fg="black")
        header.pack(pady=10)
        self.toggle_button = tk.Button(frame, text="OFF", command=self.toggle_save, width=10, height=2, bg="red", fg="white",)
        self.toggle_button.pack(side=tk.RIGHT, padx=20)
        # Display for transcription text
        tk.Label(root, text="Transcription:", font=("Arial", 24), bg="white", fg="black").pack(pady=(10, 2))
        self.transcription_label = tk.Label(root, textvariable=self.transcription_text, wraplength=450, font=("Arial", 16), relief="sunken", bg="lightyellow", fg="black", height=4)
        self.transcription_label.pack(fill="both", padx=10, pady=5)
        # Scroll colors button
        self.conversation_button = tk.Button(frame2, text="Scroll Conversations",width=20, command=self.scroll_conversations, font=("Arial", 16), bg="gray", fg="white")
        self.conversation_button.pack(side=tk.RIGHT, padx=20)

        # Choose color button
        self.choose_button = tk.Button(frame2, text="Choose Conversation", command=self.choose_conversation, font=("Arial", 16), bg="blue", fg="white")
        self.choose_button.pack(side=tk.RIGHT, padx=20)

        def configure_button_styles(self):
            """Configure consistent button styles to avoid platform-specific quirks."""
            button_style = {
                "bg": "green",
                "activebackground": "lightgray",
                "fg": "black",
                "activeforeground": "black",
                "relief": "raised",
            }
            self.toggle_button.config(**button_style)
            self.conversation_button.config(**button_style)
            self.choose_button.config(**button_style)
        start_style = {
                "bg": "green",
                "activebackground": "lightgray",
                "fg": "black",
                "activeforeground": "black",
                "relief": "raised",
            }
        stop_style = {
                "bg": "red",
                "activebackground": "lightgray",
                "fg": "white",
                "activeforeground": "black",
                "relief": "raised",
            }
        configure_button_styles(self)
        self.stop_button.config(**stop_style)
        self.start_button.config(**start_style)

        self.conversations = get_conversations()
        print(self.conversations)
        self.conversation_index = 0
    
        

        # Display for braille output
        tk.Label(root, text="Braille Output:", font=("Arial", 24), bg="white", fg="black").pack(pady=(10, 2))
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
    def scroll_conversations(self):
       
        self.conversation_index = (self.conversation_index + 1) % len(self.conversations)

        self.conversation_button.config(text=self.conversations[self.conversation_index])

    def choose_conversation(self):
        """Set the current text conversation as the user's chosen conversation."""
        self.selected_conversation = self.conversations[self.conversation_index]
        print(f"Chosen conversation: {self.selected_conversation}")

        # Load the content of the selected conversation file (assuming text file format)
        try:
            with open(self.selected_conversation, 'r') as file:
                conversation_content = file.read()

            # Process the content (e.g., transcribe and convert to braille)
            transcription = conversation_content
            braille = text_to_braille(transcription)

            # Update the text variables with the transcription and braille
            self.transcription_text.set(transcription)
            self.braille_text.set(braille)

            # Optionally, save or display the conversation's braille representation
            save_braille(self.selected_conversation, transcription, self.save_conversation)

        except FileNotFoundError:
            print(f"Error: File '{self.selected_conversation}' not found.")
        except Exception as e:
            print(f"Error reading file: {e}")

    def start_recording(self):
        # Update button states
        self.start_button.config(state="disabled")
        self.stop_button.config(state="normal")
        # Disable Start Recording
        self.start_canvas.unbind("<Button-1>")
        # Enable Stop Recording
        self.stop_canvas.bind("<Button-1>", lambda event: self.stop_recording())

        # Check if an audio input device is available
        devices = sd.query_devices()
         # Check for devices with input capability
        input_devices = [device for device in devices if device["max_input_channels"] > 0]
        if not input_devices:
            # No microphone detected
            messagebox.showerror("Error", "No microphones detected. Please connect an audio input device.")
            self.start_button.config(state="normal")
            self.stop_button.config(state="disabled")
            return

        # Print input devices for debugging
        print("Available input devices:")
        for idx, device in enumerate(input_devices):
            print(f"{idx}: {device['name']}")

        # Use the default input device (or allow the user to choose from input_devices)
        default_device = input_devices[0]
        print(f"Using default microphone: {default_device['name']}")
        
        status_update = "Recording in progress..."
        self.transcription_text.set(status_update)
        self.braille_text.set(text_to_braille(status_update)[0])
        # Start recording in a separate thread to avoid freezing the UI
        threading.Thread(target=lambda: record_audio("output.wav", duration=5)).start()
        
    def stop_recording(self):
        # Stop recording and process audio
        self.stop_button.config(state="disabled")
        self.start_button.config(state="normal")
        self.conversations = get_conversations()
        
        # Start transcription in a separate thread to keep UI responsive
        threading.Thread(target=self.process_audio).start()
    
    def process_audio(self):
        try:
            # Transcribe audio and convert to braille
            # TODO: Create success metric for total time for transcription
            # transcription = transcribe_audio("output.wav")
            transcription = "This is a bigger test using multiple sentences. Lets see what happens."
            braille, runtime = text_to_braille(transcription)
            print(f"Transcription: {transcription}")
            print(f"Braille: {braille}")
            save_braille("test.txt",transcription,self.save_conversation)
            # Update text variables (for display)
            self.transcription_text.set(transcription)
            self.braille_text.set(braille)
            self.transcription_time.set(f"Transcription Time: {runtime:.6f}s")

            # Force widgets to refresh
            self.transcription_label.update_idletasks()
            self.braille_label.update_idletasks()
        
            print(f"Transcription StringVar: {self.transcription_text.get()}")
            print(f"Braille StringVar: {self.braille_text.get()}")
        
        except Exception as e:
            # Display error message if transcription fails
            messagebox.showerror("Error", f"An error occurred: {e}")
            print("Error on processing audio.")
            self.transcription_text.set("Error transcribing audio.")
            self.braille_text.set("")

# Initialize the Tkinter app
if __name__ == "__main__":
    root = tk.Tk()
    app = AudioTranscriptionApp(root)
    root.mainloop()

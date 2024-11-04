import sounddevice as sd
import wavio

def record_audio(filename, duration=5, fs=44100):
    print("Recording...")
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
    sd.wait()  # Wait until recording is finished
    print("Recording finished.")
    wavio.write(filename, recording, fs, sampwidth=2)  # Save as WAV file

# Usage:
# record_audio("output.wav", duration=5)  # Record for 5 seconds

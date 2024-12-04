import sounddevice as sd
import wavio
# def record_audio(filename, duration=5, fs=44100):
#     print("Recording...")
#     recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
#     sd.wait()  # Wait until recording is finished
#     print("Recording finished.")
#     wavio.write(filename, recording, fs, sampwidth=2)  # Save as WAV file


def record_audio(filename, duration=60, fs=44100):
    """Record audio and save to a WAV file."""
    if duration <= 0:
        raise ValueError("Duration must be greater than 0 seconds.")
    if fs <= 0:
        raise ValueError("Sampling rate must be greater than 0.")

    print("Recording...")
    try:
        # Context manager ensures proper resource management
        with sd.InputStream(samplerate=fs, channels=1, dtype='int16') as stream:
            recording = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='int16')
            sd.wait()  # Wait until recording is finished
        print("Recording finished.")
        wavio.write(filename, recording, fs, sampwidth=2)  # Save as WAV file
    except Exception as e:
        print(f"An error occurred during recording: {e}")
        raise  # Re-raise the exception for higher-level handling
# Usage:
# record_audio("output.wav", duration=5)  # Record for 5 seconds

# Audio-to-Braille Transcription Project

This project provides real-time transcription of audio into text, which is then converted to braille for display. Users can start and stop recording to receive a transcription and braille representation of the recorded audio. Built using IBM Watson’s Speech-to-Text API, the program currently displays braille output visually.

## Table of Contents
- [Features](#features)
- [Technologies](#technologies)
- [Getting Started](#getting-started)
  - [1. Prerequisites](#1-prerequisites)
  - [2. Installation](#2-installation)
  - [3. Running the Application](#3-running-the-application)
- [Future Development](#future-development)
- [Contributing](#contributing)

---

## Features
- **Audio Recording**: Capture audio via microphone for real-time transcription.
- **Speech-to-Text**: Converts audio to text using IBM Watson’s Speech-to-Text API.
- **Text-to-Braille Conversion**: Translates transcribed text into braille representation.
- **Visual Display**: Shows both the text and braille output on the interface.

## Technologies
- **Python**
- **IBM Watson Speech-to-Text API** for transcription
- **Tkinter** for GUI
- **SoundDevice** and **Wavio** for audio recording
- **IBM Watson SDK** for integrating with the Speech-to-Text API

## Getting Started

### 1. Prerequisites
- **Python 3.7+** is required for this project.
- **IBM Watson API Key and URL**: You will need an IBM Cloud account and a Speech-to-Text service instance.
  - Place your `API_KEY` and `API_URL` in `src/utils/config.py` for secure and easy access:

    ```python
    # src/utils/config.py
    API_KEY = 'your_ibm_watson_api_key'
    API_URL = 'your_ibm_watson_service_url'
    ```

### 2. Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/yourusername/audio-to-braille-transcription.git
   cd audio-to-braille-transcription
   ```

2. **Create a Virtual Environment** (recommended):

   ```bash
   python -m venv env
   source env/bin/activate  # macOS/Linux
   env\Scripts\activate     # Windows
   ```

3. **Install Dependencies**:

   Install the necessary packages using `pip`:

   ```bash
   pip install -r requirements.txt
   ```

### 3. Running the Application

To start the application, simply run the UI script:

```bash
python src/ui/app_ui.py
```

### Usage
1. **Start Recording**: Click "Start Recording" to begin capturing audio.
2. **Stop Recording**: Click "Stop Recording" to end the audio capture. The transcription and braille output will be displayed in the application interface.

## Future Development
- **Persistent Storage**: Add a feature to save audio and transcription data for historical reference.
- **Braille Output Device Integration**: Interface with hardware braille displays when available.
- **Web Interface**: Develop a web interface for greater accessibility and platform compatibility.

## Contributing
Contributions are welcome! If you find a bug or have a suggestion, please open an issue. For major changes, consider creating a new branch and submitting a pull request with a detailed description of the changes.

1. **Fork the Repository**
2. **Create a Feature Branch**:
   ```bash
   git checkout -b feature-name
   ```
3. **Commit Changes**:
   ```bash
   git commit -m "Add new feature"
   ```
4. **Push to Branch**:
   ```bash
   git push origin feature-name
   ```
5. **Open a Pull Request**: Submit a pull request for review.

---

This README provides a comprehensive guide to understanding, setting up, and contributing to the project. If you have any questions or encounter issues, feel free to reach out.

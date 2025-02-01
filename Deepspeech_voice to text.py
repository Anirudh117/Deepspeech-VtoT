import pyaudio
import wave
import deepspeech
import numpy as np
import os

# Function to record audio
def record_audio(filename="audio.wav"):
    chunk = 1024  # Record in chunks of 1024 samples
    sample_format = pyaudio.paInt16  # 16-bit resolution
    channels = 1  # Single channel for mono audio
    fs = 16000  # Sample rate (16kHz)
    seconds = 5  # Length of audio to record

    p = pyaudio.PyAudio()

    print("Recording...")
    stream = p.open(format=sample_format,
                    channels=channels,
                    rate=fs,
                    input=True,
                    frames_per_buffer=chunk)

    frames = []

    # Record the audio in chunks
    for i in range(0, int(fs / chunk * seconds)):
        data = stream.read(chunk)
        frames.append(data)

    # Stop recording
    print("Recording complete.")
    stream.stop_stream()
    stream.close()
    p.terminate()

    # Save the audio as a .wav file
    wf = wave.open(filename, 'wb')
    wf.setnchannels(channels)
    wf.setsampwidth(p.get_sample_size(sample_format))
    wf.setframerate(fs)
    wf.writeframes(b''.join(frames))
    wf.close()
    print(f"Audio saved to {filename}")

# Load DeepSpeech model
def load_model():
    model_path = "C:/Users/Anirudhan/OneDrive/Desktop/Voice to text/Deepspeech/deepspeech-0.9.3-models.pbmm"
    scorer_path = "C:/Users/Anirudhan/OneDrive/Desktop/Voice to text/Deepspeech/deepspeech-0.9.3-models.scorer"
    model = deepspeech.Model(model_path)
    model.enableExternalScorer(scorer_path)
    print("Model loaded.")
    return model

# Function to transcribe audio
def transcribe_audio(model, audio_file):
    # Read audio file
    with wave.open(audio_file, 'rb') as wf:
        frames = wf.readframes(wf.getnframes())
        audio_data = np.frombuffer(frames, dtype=np.int16)

    # Transcribe the audio
    print("Transcribing...")
    text = model.stt(audio_data)
    return text

# Main function to record and transcribe
def main():
    audio_file_path = "C:/Users/Anirudhan/OneDrive/Desktop/Voice to text/Deepspeech/audio.wav"

    # Record audio
    record_audio(audio_file_path)

    # Load the DeepSpeech model
    model = load_model()

    # Transcribe the audio
    transcription = transcribe_audio(model, audio_file_path)

    # Print transcription
    print(f"Transcription: {transcription}")

# Run the main function
if __name__ == "__main__":
    main()

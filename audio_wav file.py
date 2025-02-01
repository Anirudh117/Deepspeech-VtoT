import pyaudio
import wave

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

# Call the function to record audio and save it as a .wav file
audio_file_path = "C:/Users/Anirudhan/OneDrive/Desktop/Voice to text/Deepspeech/audio.wav"
record_audio(audio_file_path)

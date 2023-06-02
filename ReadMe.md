# ElevenLabs Text-to-Speech API Script

This script demonstrates how to use the Text-to-Speech API to convert text into audio using the ElevenLabs API. It takes an input text from a file, sends a request to the API, and saves the generated audio as a WAV file.

> **Note:** This script can be used with Virtual Audio Cables to stream the `output.wav` file through your microphone onto programs like Discord.

## Prerequisites

- Python
- `requests` library
- `pydub` library

## Getting Started

1. Obtain an API key from ElevenLabs and replace `'Your ElevenLabs API Key'` in the script with your actual API key.

2. Edit the text file named `ReadThis.txt` and enter the text you want to convert to audio.

3. Install the required libraries by running the following commands:
    ```shell
    pip install requests
    pip install pydub
    ```

4. Run the script using the following command:
    ```shell
    python Main.py
    ```

## How It Works

1. Import the necessary libraries:
    ```python
    import requests
    from pydub import AudioSegment
    ```

2. Set up the API endpoint, headers, and other necessary variables:
    ```python
    url = 'https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream'
    headers = {
        'accept': '*/*',
        'xi-api-key': 'Your ElevenLabs API Key',
        'Content-Type': 'application/json'
    }
    ```
> **Note:** In ElevenLabs API Playground, you can get the VoiceIDs of all the voices, including the cloned ones you made. One you have the VoiceID you want, just change "21m00Tcm4TlvDq8ikWAM" in the URL to whatever the VoiceID is. The current VoiceID is "Rachel".

3. Read the input text from the file `ReadThis.txt`:
    ```python
    with open('ReadThis.txt', 'r') as f:
        input_text = f.read()
    ```

4. Set up the API request data:
    ```python
    data = {
        'text': input_text,
        'voice_settings': {
            'stability': 0.50,
            'similarity_boost': 0.75
        }
    }
    ```

5. Send a POST request to the API and save the audio output to a file:
    ```python
    response = requests.post(url, headers=headers, json=data)
    if response.status_code == 200:
        with open('output.wav', 'wb') as f:
            f.write(response.content)
        print('Audio saved as output.wav')
    else:
        print('Error:', response.text)
    ```

6. Optionally, convert the audio file to a 16-bit 44100 Hz WAV format:
    ```python
    audio = AudioSegment.from_file('output.wav')
    audio = audio.set_frame_rate(44100)
    audio = audio.set_sample_width(2)  # 16-bit
    audio.export('output_processed.wav', format='wav')
    ```

> **Note:** Conversion of the audio file to a specific format (Step 6) is optional and designed for use with Voicemeeter Banana. You can remove step 6 and the script will still function the same.

That's it! Running this script will generate an audio file based on the text provided in `ReadThis.txt`.

Feel free to modify the script and adjust the API parameters according to your requirements.

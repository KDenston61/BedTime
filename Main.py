import requests
from pydub import AudioSegment

# set up API endpoint and headers
url = 'https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM/stream'
headers = {
    'accept': '*/*',
    'xi-api-key': 'Your ElevenLabs API Key',
    'Content-Type': 'application/json'
}

# read input text from file
with open('ReadThis.txt', 'r') as f:
    input_text = f.read()

# set up API request data
data = {
    'text': input_text,
    'voice_settings': {
        'stability': 0.50,
        'similarity_boost': 0.75
    }
}

# Send API request and save audio output to file
response = requests.post(url, headers=headers, json=data)
if response.status_code == 200:
    with open('output.wav', 'wb') as f:
        f.write(response.content)
    print('Audio saved as output.wav')

    # Convert audio file to 16-bit 44100 Hz WAV
    audio = AudioSegment.from_file('output.wav')
    audio = audio.set_frame_rate(44100)
    audio = audio.set_sample_width(2)  # 16-bit
    audio.export('output_processed.wav', format='wav')
    
else:
    print('Error:', response.text)
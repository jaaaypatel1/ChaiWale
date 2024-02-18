from gtts import gTTS
from flask import Flask, request, render_template 
import os

app = Flask(__name__)

def text_to_speech(text):
    # Initialize gTTS with the text to convert
    speech = gTTS(text)

    # Save the audio file to a temporary file
    speech_file = 'speech.mp3'
    speech.save(speech_file)

    # Play the audio file
    os.system('start ' + speech_file)
    
    
text_to_speech('Hello, world! This is a test.')


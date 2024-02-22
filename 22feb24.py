import speech_recognition as sr
from textblob import TextBlob

audio_file = "sample.wav"

recognizer = sr.Recognizer()

with sr.AudioFile(audio_file) as source:

    recognizer.adjust_for_ambient_noise(source)

    audio_data = recognizer.record(source)
try:
    text = recognizer.recognize_google(audio_data)
    print("Transcription:",text)
except sr.UnknownValueError:
    print("Unknown Sorry")
text = "This is very excellent"
blob = TextBlob(text)
sentiment = blob.sentiment
# (-1 is for negative, 0 is for neutral, 1 is for positive")
print("Sentiment Score:", sentiment.polarity)
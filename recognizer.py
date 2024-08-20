import json
import speech_recognition as sr

filename = "input.wav"

r = sr.Recognizer()


def recognize():
    with sr.AudioFile(filename) as source:
        audio_data = r.record(source)
        voice = r.recognize_vosk(audio_data, language="ru-RU")
        json_data = json.loads(voice)
        prompt = json_data.get("text")
        print("flmxn: " + prompt.capitalize())

        return prompt

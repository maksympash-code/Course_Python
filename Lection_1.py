import speech_recognition
import pyttsx3

def voice_recognizer(microphone, recognizer):
    with microphone:
        recognize_text = ""
        print("Listening...")
        recognizer.adjust_for_ambient_noise(microphone, 2)

        print("Recording...")
        audio = recognizer.listen(microphone, timeout=2)
        print("Recognizing...")
        recognize_text = recognizer.recognize_google(audio, language="en-US")

    return recognize_text

def play_voice(tta_engine: pyttsx3.Engine, text):
    tta_engine.say(text)
    tta_engine.runAndWait()



microphone = speech_recognition.Microphone()
recognizer = speech_recognition.Recognizer()

tts_engine = pyttsx3.init()


voice_input_text = voice_recognizer(microphone, recognizer)
print("You said: " + voice_input_text)

command = voice_input_text.split()[0].lower()

if command == "hi":
    play_voice(tts_engine, "Hello")
elif command == "repeat":
    play_voice(tts_engine, voice_input_text)
else:
    play_voice(tts_engine, "I didn't understand")
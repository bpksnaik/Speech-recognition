import speech_recognition as sr
import pyttsx3


def text_to_speech(text: str) -> None:
    text_speech = pyttsx3.init()
    text_speech.say(text)
    text_speech.runAndWait()


def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Something.. : ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        text = r.recognize_google(audio)
        print(f"This is what you said :\n {text}")
        return text


if __name__ == '__main__':
    text_to_speech(speech_to_text())

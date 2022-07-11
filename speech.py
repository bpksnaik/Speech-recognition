import speech_recognition as sr


def speech_to_text():
    r = sr.Recognizer()

    with sr.Microphone() as source:
        print("Speak Something.. : ")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

        text = r.recognize_google(audio)
        print(f"This is what you said :\n {text}")


if __name__ == '__main__':
    speech_to_text()

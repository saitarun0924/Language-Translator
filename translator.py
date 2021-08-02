import speech_recognition as sr
from translate import Translator
from gtts import gTTS
import os

r=sr.Recognizer()
with sr.Microphone() as source:
    print('Speak anything to translate....')
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print('You said : {}'.format(text))
        f_lang = str(input("Enter input language : "))
        t_lang = str(input("Enter translating language : ")) 
        translator = Translator(from_lang = f_lang, to_lang = t_lang)
        result = translator.translate(text)
        print("Transalated text :", result)
        output2=gTTS(text=result,slow=False)
        output2.save("transaudio.mp3")
        os.system("transaudio.mp3")

    except:
        print('sorry could not recognize your voice')
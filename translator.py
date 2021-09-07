import speech_recognition as sr
from translate import Translator
from gtts import gTTS, lang

import os

r=sr.Recognizer()

with sr.Microphone() as source:
    print('Speak anything to translate....')
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print('You said : {}'.format(text))
        print(lang.tts_langs())
        f_lang = str(input("Enter input language from the above list :"))
        t_lang = str(input("Enter translating language from the above list :")) 
        translator = Translator(from_lang = f_lang, to_lang = t_lang)
        result = translator.translate(text)
        print("Transalated text :", result)
        output2=gTTS(text=result,slow=False)
        output2.save("transaudio.mp3")
        os.system("transaudio.mp3")

    except:
        print('sorry could not recognize your voice')
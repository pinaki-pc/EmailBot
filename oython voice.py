import pyttsx3

engine = pyttsx3.init()


def voice_change():
    voices = engine.getProperty('voices')
    for voice in voices:
        engine.setProperty('voice', voice.id)
        engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


def change_speech_rate():
    rate = engine.getProperty('rate')
    engine.setProperty('rate', rate - 100)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


def change_volume():
    volume = engine.getProperty('volume')
    engine.setProperty('volume', volume + 9.25)
    engine.say('The quick brown fox jumped over the lazy dog.')
    engine.runAndWait()


voice_change()

import speech_recognition as sr

rec = sr.Recognizer()
# print(sr.Microphone().list_microphone_names())
with sr.Microphone() as mic:
    rec.adjust_for_ambient_noise(mic)
    print("Fale algo que vou gravar em texto: ")
    audio = rec.listen(mic, timeout=5, phrase_time_limit=10)
    texto = rec.recognize_google(audio, language="pt-BR")
    print(texto)

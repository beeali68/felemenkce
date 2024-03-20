# çevrimiçi ve çevrim dışı bir şekilde çalışan konuşma tanıma kütüphanesi
from flask import Flask, render_template, request, redirect, url_for, session, send_file
from gtts import gTTS  # text i ses e çevirmek için
from playsound import playsound  # ses dosyasını çalmak için
import os  # sistem ayarları değiştirmk için



def speak(string):  # speak adlı bir fonksiyon oluştuyoruz
    # sesi text e nl olarak çevirip tts adlı değişkene tanımlıyoruz
    try:
        tts = gTTS(string, lang='nl')
        # .mp3 uzantılı bir ses dosyası oluşturuyoruz
        file = 'static/{}.mp3'.format(string)
        tts.save(file)  # dosyayı kayıt ediyoruz
        playsound(file)
        os.remove(file)  # dosyayı siliyouz
        # os.system('mpg123 -q {}'.format(file))
    except:
        pass

    return string

# speak("duur")  # speak fonksiyonunu çağırıyoruz


#!/usr/bin/env python3
# coding: utf8
import PySimpleGUIWeb as sg
import pyopenjtalk
import numpy
import simpleaudio as sa
from scipy.io import wavfile

#print(dir(sg))
#print(sg.theme_list())

sg.theme('DarkGreen')

layout = [
    [sg.Text('PySimpleGUIWeb＋PyOpenJTalk テスト')],
    [sg.Text('テキスト', size=(10, 1)), sg.InputText('しゃべらせたい言葉をここに入力します。')],
    [sg.Submit(button_text='話す')]
]

window = sg.Window('PySimpleGUIWeb＋PyOpenJTalk テスト', layout)

while True:
    event, values = window.read()
    if event is None:
        print('exit')
        break
    if event == '実行':
        text = values[0]
        x, sr = pyopenjtalk.tts(text)
        wavfile.write("test.wav", sr, x.astype(numpy.int16))

        play_obj = sa.play_buffer(x.astype(numpy.int16), 1, 2, 44100)
        play_obj.wait_done()
        #if play_obj.is_playing(): play_obj.stop()

        #wavfile.write("test.wav", sr, x.astype(np.int16))

        #x = wave_file.readframes(wave_file.getnframes()) #frameの読み込み
        #x = np.frombuffer(x, dtype= "int16") #numpy.arrayに変換

        sg.popup(text + '<br>' + pyopenjtalk.g2p(text))


window.close()


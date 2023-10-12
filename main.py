import PySimpleGUI as sg
import random

sg.theme("DarkBrown3")

layout = [
    [sg.Text("さあ、おみくじを引きましょう！")],
    [sg.Image(filename="futada0.png", key="img")],
    [sg.Text("", key="txt")],
    [sg.Button("おみくじをひく", key="btn")]
]

window = sg.Window('おみくじアプリ', layout, font=(None, 14))

def omikuji():
    kuji = ["大吉", "中吉", "小吉", "凶"]
    kekka = random.choice(kuji)
    txt = f"結果は{kekka}でした～"
    window["txt"].update(txt)

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == "btn":
        omikuji()

window.close()

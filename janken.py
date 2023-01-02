import tkinter
import json
import time
import random

window = tkinter.Tk()
window.title("じゃんけん")
window.minsize(300, 380)

canvas = tkinter.Canvas(bg = "sky blue", width=300, height=480)
canvas.place(x=0, y=0)

#画像を読み込む
pa_img = tkinter.PhotoImage(file = "game/img/pa.png")
gu_img = tkinter.PhotoImage(file = "game/img/gu.png")
tyoki_img = tkinter.PhotoImage(file = "game/img/tyoki.png")

top_label = tkinter.Label(text = "じゃんけん", bg = "sky blue", fg = "black", font = ("メイリオ",20,"bold"))
top_label.place(x=100, y=40)
secand_label = tkinter.Label(text = "自分の出す手を選んでください", bg = "sky blue", fg = "red", font = ("メイリオ",22,"bold"))
secand_label.place(x=10, y=100)

#手ボタン
gu_button = tkinter.Button(image = gu_img)
gu_button.place(x=10, y=170)
tyoki_button = tkinter.Button(image = tyoki_img)
tyoki_button.place(x=110, y=165)
pa_button = tkinter.Button(image = pa_img)
pa_button.place(x=210, y=170)

def start():
    secand_label.destroy()
    gu_button.destroy()
    tyoki_button.destroy()
    pa_button.destroy()

    window.minsize(300, 480)

    top_label["text"] = "結果"
    top_label["font"] = "メイリオ",80,"bold"
    top_label.place(x=70, y=10) 

    my_te_label = tkinter.Label(text = "", bg = "sky blue", fg = "black", font = ("メイリオ",35,"bold"))
    my_te_label.place(x=85, y=130)
    your_te_label = tkinter.Label(text = "", bg = "sky blue", fg = "black", font = ("メイリオ",35,"bold"))
    your_te_label.place(x=85, y=230)
    win_or_lose_label1 = tkinter.Label(text = "勝敗", bg = "sky blue", fg = "black", font = ("メイリオ",50,"bold"))
    win_or_lose_label1.place(x=100, y=320)
    win_or_lose_label2 = tkinter.Label(text = "", bg = "sky blue", fg = "red", font = ("メイリオ",35,"bold"))
    win_or_lose_label2.place(x=110, y=400)

    #自分の手を表示する
    with open("game/my_te.json", "r", encoding="utf-8") as file:
        my_te = json.load(file)

    if my_te == 1:
        my_te_label["text"] = "自分の手\nグー"
    elif my_te == 2:
        my_te_label["text"] = "自分の手\nチョキ"
    elif my_te == 3:
        my_te_label["text"] = "自分の\nパー"

    window.update()
    time.sleep(2)
    window.update()

    #相手の手を表示する
    aite_te = random.randint(1,3)

    if aite_te == 1:
        your_te_label["text"] = "相手の手\nグー"
        your_te = 1
        with open("gameyour_te.json", "w", encoding="utf-8") as file:
            json.dump(your_te, file)
    if aite_te == 2:
        your_te_label["text"] = "相手の手\nチョキ"
        your_te = 2
        with open("game/your_te.json", "w", encoding="utf-8") as file:
            json.dump(your_te, file)
    if aite_te == 3:
        your_te_label["text"] = "相手の手\nパー"
        your_te = 3
        with open("game/your_te.json", "w", encoding="utf-8") as file:
            json.dump(your_te, file)
    time.sleep(2)
    window.update()

    #勝敗
    with open("game/my_te.json", "r", encoding="utf-8") as file:
        my_te = json.load(file)
    with open("game/your_te.json", "r", encoding="utf-8") as file:
        your_te = json.load(file)

    time.sleep(2)
    window.update()

    if (my_te == 1) and (your_te == 1) or (my_te == 2) and (your_te == 2) or (my_te == 3) and (your_te == 3):
        win_or_lose_label2["text"] = "あいこ"
        win_or_lose_label2["fg"] = "black"
    if (my_te == 1) and (your_te == 2) or (my_te == 2) and (your_te == 3) or (my_te == 3) and (your_te == 1):
        win_or_lose_label2["text"] = "勝ち"
        win_or_lose_label2["fg"] = "red"
    if (my_te == 1) and (your_te == 3) or (my_te == 2) and (your_te == 1) or (my_te == 3) and (your_te == 2):
        win_or_lose_label2["text"] = "負け"
        win_or_lose_label2["fg"] = "blue"

def gu_te():
    with open("game/my_te.json", "r", encoding="utf-8") as file:
        my_te = json.load(file)
    my_te = 1
    with open("game/my_te.json", "w", encoding="utf-8") as file:
        json.dump(my_te, file)
    start()
gu_button["command"] = gu_te

def tyoki_te():
    with open("game/my_te.json", "r", encoding="utf-8") as file:
        my_te = json.load(file)
    my_te = 2
    with open("game/my_te.json", "w", encoding="utf-8") as file:
        json.dump(my_te, file)
    start()
tyoki_button["command"] = tyoki_te

def pa_te():
    with open("game/my_te.json", "r", encoding="utf-8") as file:
        my_te = json.load(file)
    my_te = 3
    with open("game/my_te.json", "w", encoding="utf-8") as file:
        json.dump(my_te, file)
    start()
pa_button["command"] = pa_te

window.mainloop()
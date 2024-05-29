import datetime
import json
import os
import random
import numpy as np
import pytz
import requests
#from develop.db import databases
from deve.randoming import shibari, tsuika


from colorama import Fore, Style
from replit import db
from flask import Flask, abort, request
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import ImageSendMessage, MessageAction, MessageEvent, QuickReply, QuickReplyButton, TextMessage, TextSendMessage

app = Flask(__name__)

#ボットの読み込み
line_bot_api = LineBotApi(os.getenv("YOUR_CHANNEL_ACCESS_TOKEN"))
handler = WebhookHandler(os.getenv("YOUR_CHANNEL_SECRET"))


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@app.route("/")
def index():
    os.system("clear")
    print("success")
    return "Running now"




text = ""
list = json.load(open("deve/Data/shibari.json"))
f = open('deve/Data/word.txt', 'r')

words = f.read()


def choose():
      text = ""
      lists = json.load(open("deve/Data/shibari.json"))
      list = lists["shibari"]
      shibari = random.choice(list)
      text += shibari + "\n"


#メッセージがとどいた時
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    message = event.message.text  #メッセージ
    user_id = event.source.user_id  # ID
    profile = line_bot_api.get_profile(user_id)
    now = datetime.datetime.now(pytz.timezone("Asia/Tokyo"))  # 時間

    print(
        f'{Fore.GREEN}[{now.strftime("%m/%d %H:%M:%S")}] {Style.RESET_ALL}{Style.DIM}[{profile.display_name}]{Style.RESET_ALL}   {Style.DIM}{message}{Style.RESET_ALL}'
    )

    def send():
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=text))



    if message.startswith("インベントリ"):
        l = message.split()
        n = len(l)
        buki = json.load(open('deve/Data/shibari.json'))
        b = buki["buki"]
        text = ""
        if n == 2:
            try:
                if int(message[1]) <= 5 and int(message[1]) >= 1:
                    for i in range(int(message[1])):
                        text += f"{random.choice(b)}\n"
                else:
                    text = "Error\n1～5で入力してください"
            except:
                text = "Error\n数字で入力して"
        else:
            text = "Error 400"
        send()

    elif message == "サーバー":
        server = [
            "Asia", "EU", "中東", "アメリカ東", "アメリカ西", "アメリカ中部", "オセアニア", "ブラジル"
        ]
        text = random.choice(server)
        send()

    elif message == "縛り":
        from deve.randoming import shibari, tsuika
        if random.randint(1,319) == 1:
            tsuika()
            send()
            return
        else:
            shibari()
            if "再ロール禁止" in text:
                send()
            else:
                line_bot_api.reply_message(
                    event.reply_token,
                    TextSendMessage(
                    text=text,
                        quick_reply=QuickReply(items=[
                            QuickReplyButton(
                                action=MessageAction(label="再ロール", text="再ロール"))
                        ])))


    elif message == "期間":
        a = random.randint(1, 8)
        text = f"第{a}安置収縮終了まで攻撃禁止"
        send()


    elif message.startswith("再ロール"):
        n = message.split()
        l = len(n)
        if l == 1:
            shibari = json.load(open('deve/Data/shibari.json'))
            b = shibari["shibari"]
            text1 = random.choice(b)
            text2 = random.choice(b)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text=text1 + "\n" + text2,
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(
                            action=MessageAction(label="再ロール", text="再ロール 2")),
                        QuickReplyButton(
                            action=MessageAction(label="矛盾してる？", text="再ロール"))
                    ])))

        elif l == 2 and n[1] == "2":
            shibari = json.load(open('deve/Data/shibari.json'))
            b = shibari["shibari"]
            text1 = random.choice(b)
            text2 = random.choice(b)
            text3 = random.choice(b)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text=text1 + "\n" + text2 + "\n" + text3,
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(
                            action=MessageAction(label="再ロール", text="再ロール 3")),
                        QuickReplyButton(action=MessageAction(label="矛盾してる？",
                            text="再ロール 2"))
                    ])))
        elif l == 2 and n[1] == "3":
            shibari = json.load(open('deve/Data/shibari.json'))
            b = shibari["shibari"]
            text1 = random.choice(b)
            text2 = random.choice(b)
            text3 = random.choice(b)
            text4 = random.choice(b)
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(
                    text=text1 + "\n" + text2 + "\n" + text3 + "\n" + text4,
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(action=MessageAction(label="矛盾してる？",
                            text="再ロール 3"))
                    ])))

        send()


    elif message.startswith("ポイント"):
        point = random.randint(25, 200)
        url = json.load(open('deve/Data/shibari.json'))
        if "デュオ" in message:
            a = url["duo"]
            b = random.choice(a)
            line_bot_api.reply_message(event.reply_token, [
                TextSendMessage(text=f"{point}ポイント必要"),
                TextSendMessage(text="ルール:"),
                TextSendMessage(text=b)
            ])
        elif "トリオ" in message:
            a = url["trio"]
            b = random.choice(a)
            line_bot_api.reply_message(event.reply_token, [
                TextSendMessage(text=f"{point}ポイント必要"),
                TextSendMessage(text="ルール:"),
                TextSendMessage(text=b)
            ])
        elif "スクワッド" in message:
            a = url["squ"]
            b = random.choice(a)
            line_bot_api.reply_message(event.reply_token, [
                TextSendMessage(text=f"{point}ポイント必要"),
                TextSendMessage(text="ルール:"),
                TextSendMessage(text=b)
            ])
        else:
            line_bot_api.reply_message(
                event.reply_token,
                TextSendMessage(text='どれ？',
                                quick_reply=QuickReply(items=[
                                    QuickReplyButton(action=MessageAction(
                                        label="デュオ", text="ポイント デュオ")),
                                    QuickReplyButton(action=MessageAction(
                                        label="トリオ", text="ポイント トリオ")),
                                    QuickReplyButton(action=MessageAction(
                                        label="スクワッド", text="ポイント スクワッド"))
                                ])))

    elif message == "体力":
        text = random.randint(90, 210)
        if text >= 200:
            text = 200
        elif text <= 90:
            text = 100
        send()

    elif message == "HUD" or message == "hud":
        a = random.randint(25, 125)
        text = f"{a}%"
        send()

    elif message == "人数":
        a = random.randint(10, 90)
        text = f"残り{a}人になるまで攻撃禁止"
        send()

    elif message in words:
        list = json.load(open("deve/Data/rule.json"))
        text = list[message]
        send()

    elif message == "用語":
        pass

    elif message.startswith("戦績"):
        n = message.split()
        l = len(n)
        name = ""
        if l >= 2:
            if l == 2:
                name = n[l - 1]
            else:
                x = 1
                for i in range(l - 1):
                    name += n[x] + " "
                    x += 1
            req = requests.get(
                "https://fortnite-api.com/v2/stats/br/v2?language=ja",
                headers={"Authorization": os.getenv("fn-api-key")},
                params={
                    "name": name,
                    "image": "all"
                })
            userDate = req.json()
            image = userDate["data"]["image"]
            line_bot_api.reply_message(
                event.reply_token,
                ImageSendMessage(original_content_url=image,
                                 preview_image_url=image))
        else:
            text = "error"
            send()

    elif message == "マップ":
        req = requests.get("https://fortnite-api.com/v1/map?language=ja")
        map = req.json()
        image = map["data"]["images"]["pois"]
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=image,
                             preview_image_url=image))

    elif message == "ニュース":
        req = requests.get("https://fortnite-api.com/v2/news/br?language=ja")
        map = req.json()
        image = map["data"]["image"]
        line_bot_api.reply_message(
            event.reply_token,
            ImageSendMessage(original_content_url=image,
                             preview_image_url=image))

    elif message.startswith("!"):
        if event.source.user_id == (os.getenv("SheRidge")):
            if "clear" in message:
                os.system("clear")
                text = "success"
                print(text)
            elif "back" in message:
                if hasattr(event.source, "group_id"):
                    line_bot_api.leave_group(event.source.group_id)

                # ルームからの退出処理
                if hasattr(event.source, "room_id"):
                    line_bot_api.leave_room(event.source.room_id)

                else:
                    line_bot_api.reply_message(event.reply_token,
                                               TextSendMessage(text="error"))

        else:
            pass
        send()

    elif "get_id" == message:
        if event.source.type == "user":
            got_id = event.source.user_id
        elif event.source.type == "group":
            got_id = event.source.group_id
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=f"id: {got_id}"))

    elif "get_myid" == message:
        got_id = event.source.user_id
        line_bot_api.reply_message(event.reply_token,
                                   TextSendMessage(text=f"id: {got_id}"))

    

    elif message == "モード":
        text = np.random.choice(["ランク", "通常", "ゼロ"], p=[0.9, 0.05, 0.05])
        send()

    else:
        list = json.load(open("shibari.json"))
        if message in list["data"]:
            pass
        else:
            if event.source.type == "user":
                line_bot_api.reply_message(
                    event.reply_token,
                    quick_reply=QuickReply(items=[
                        QuickReplyButton(
                            action=MessageAction(label="使い方", text="使い方")),
                    ]))


if __name__ == "__main__":
    app.run(debug=False,host="0.0.0.0", port=8000)

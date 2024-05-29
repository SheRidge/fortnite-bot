import random
import json
import os
import datetime
import pytz
from flask import Flask
from colorama import Fore, Style
from linebot import LineBotApi, WebhookHandler
from linebot.models import ImageSendMessage, MessageAction, MessageEvent, QuickReply, QuickReplyButton, TextMessage, TextSendMessage

app = Flask(__name__)

text = ""
n = 0
message = ""


def inv():
  global tx
  tx = "\n"
  lists = json.load(open("shibari.json"))
  for i in range(random.randint(1,5)):
    tx += random.choice(lists["inv"]) + "\n"
  tx += "\n以上のもの以外持つべからず\n"


def shibari():
  global text
  text = ""
  lists = json.load(open("deve/Data/shibari.json"))
  shibari = random.choice(lists["shibari"])
  if shibari == "インベントリ":
    inv()
    text.replace("インベントリ",tx)
  elif shibari == "期間":
    a = random.randint(1, 8)
    text.replace("期間",f"第{a}安置収縮終了まで攻撃禁止")
  elif shibari == "人数":
    a = random.randint(15, 90)
    text.replace("期間",f"残り人数{a}人以下になるまで攻撃禁止")
  elif shibari == "hud":
    a = random.randint(25,125)
    text.replace("hud",f"hud{a}%")
  elif shibari == "体力":
    a = random.randint(100,200)
    text.replace("体力",f"体力{a}以上になるの禁止")
  text += shibari + "\n"

  if random.randint(1, 15) == 1:
    a = random.randint(2,10)
    text += f'\n一定ポイント行くまで継続(send me \"ポイント\")\n{a}マッチごとリセット'
  if random.randint(1, 15) == 1:
    text += "\n再ロール禁止"

  if random.randint(1,50) == 1:
    a = random.randint(1000,6000)
    text += f"\n{a}ダメージ行くまで継続"

  if random.randint(1, 99) == 1:
    text += "\nランク"


def tsuika():
  tsuika = ""
  kill = random.randint(5,15)
  butai = kill + random.randint(5,15)
  heal = random.randint(100,200)
  lists = json.load(open("Data/shibari.json"))
  rare = random.choice(lists["rare"])
  for i in range(random.randint(1,3)):
    tsuika += random.choice(list["tsuika"]) + "\n"
  text = f"{rare}限定\n体力上限{heal}\n{tsuika}\nマッチ内で個人キル{kill}以上かつ部隊キル{butai}以上でビクロイするまで継続"


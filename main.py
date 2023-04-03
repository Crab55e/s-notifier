import ctypes
from datetime import datetime as dt

ctypes.windll.kernel32.SetConsoleMode(ctypes.windll.kernel32.GetStdHandle(-11),0x0007)

# selfを使った良い感じな書き方にしたかったけどNameErrorが絶えないので止めた
class console():
    def info(content: str = "Empty") -> None:
        now = dt.now().strftime("%H:%M.%S")
        print(f"\033[092m[{now}] [INFO]: {content}")
    def warn(content: str = "Empty") -> None:
        now = dt.now().strftime("%H:%M.%S")
        print(f"\033[093m[{now}] [WARN]: {content}")
    def error(content: str = "Empty") -> None:
        now = dt.now().strftime("%H:%M.%S")
        print(f"\033[091m[{now}] [ERROR]: {content}")
    def debug(content: str = "Empty") -> None:
        now = dt.now().strftime("%H:%M.%S")
        print(f"\033[094m[{now}] [DEBUG]: {content}")

console.info("Loading...")
from time import sleep
from win11toast import toast

# important task max length: 3
# TODO: 3つまで対応してるとか言っておきながら対応していないのでこれを治す
settings = {
    "importants": [
        {
            "title": "必修授業を受ける時間ですよ～",
            "description":"Chromeをを使ってN予備校を開きましょう",
            "time": {
                "start": {
                    "hours": 14,
                    "minutes":30
                },
                "end": {
                    "hours":16,
                    "minutes":30
                }
            }
        }
    ]
}
console.info("trying main task")
try:
    while True:
        sleep(15)
        now = dt.now()
        if now.hour == settings["importants"][0]["time"]["start"]["hours"] and now.minute == settings["importants"][0]["time"]["start"]["minutes"]:
            toast(settings["importants"][0]["title"], settings["importants"][0]["description"])
            console.info("Called start notify")

        elif now.hour == settings["importants"][0]["time"]["end"]["hours"] and now.minute == settings["importants"][0]["time"]["end"]["minutes"]:
            toast("お勉強の時間が終わりましたよ")
            console.info("Called end notify")
except KeyError as e:
    console.error(f"KeyError. \"settings\" variable is missing?\n{e}")
    sleep(30)
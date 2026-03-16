import time
import threading
import keyboard

spamming = False
worker = None


def spam_lctrl():
    global spamming
    while spamming:
        keyboard.press_and_release("left ctrl")
        time.sleep(0.03)


def start_spam():
    global spamming, worker
    if not spamming:
        spamming = True
        worker = threading.Thread(target=spam_lctrl, daemon=True)
        worker.start()


def stop_spam():
    global spamming
    spamming = False


keyboard.on_press_key("right ctrl", lambda _: start_spam())
keyboard.on_release_key("right ctrl", lambda _: stop_spam())

print("ค้าง RCtrl เพื่อ spam LCtrl, กด ESC เพื่อออก")
keyboard.wait("esc")

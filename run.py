import time
import threading
import keyboard

spamming = False
worker = None


def spam_lctrl():
    global spamming
    while spamming and keyboard.is_pressed("right shift"):
        keyboard.press_and_release("left ctrl")
        time.sleep(0.03)

    spamming = False


def start_spam():
    global spamming, worker
    if not spamming:
        spamming = True
        worker = threading.Thread(target=spam_lctrl, daemon=True)
        worker.start()


def stop_spam():
    global spamming
    spamming = False


keyboard.on_press_key("right shift", lambda _: start_spam())
keyboard.on_release_key("right shift", lambda _: stop_spam())

print("ค้าง Right Shift เพื่อ spam Left Ctrl, กด ESC เพื่อออก")
keyboard.wait("esc")

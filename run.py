import time
import threading
import keyboard

spamming = False


def spam_lctrl():
    global spamming
    while spamming:
        keyboard.send("left ctrl")
        time.sleep(0.03)  # 30 ms


def on_press(event):
    global spamming
    if event.name == "right ctrl" and not spamming:
        spamming = True
        threading.Thread(target=spam_lctrl, daemon=True).start()


def on_release(event):
    global spamming
    if event.name == "right ctrl":
        spamming = False


keyboard.on_press(on_press)
keyboard.on_release(on_release)

print("เริ่มทำงานแล้ว: ค้าง RCtrl เพื่อ spam LCtrl")
keyboard.wait()

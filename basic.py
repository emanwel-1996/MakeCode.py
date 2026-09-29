from microbit import display, sleep, Image
from classes import IconNames
import math


def show_number(value: float, interval: float = 150) -> None:
    if math.isnan(value):
        display.show('?')
    elif len(str(value)) == 1:
        display.show(value)
    else:
        display.scroll(round(value, 2), round(interval))
        
def show_leds(leds: str, interval: float = 0) -> None:
    display.show(Image(leds.replace('.', '0').replace('#', '9').replace('\n', ':').replace(' ', '')), round(interval))

def show_icon(icon: IconNames, interval: float = 0) -> None:
    display.show(icon.inner_image)
    if interval > 0:
        sleep(interval)

def show_string(text: str, interval: float = 150) -> None:
    if len(text) == 1:
        display.show(text)
    else:
        display.scroll(text, round(interval))

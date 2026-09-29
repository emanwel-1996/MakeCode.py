from microbit import display, sleep, Image
from typing import Callable
from classes import IconNames, ArrowNames
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

def clear_screen() -> None:
    display.clear()

def forever(body: Callable[[], None]) -> None:
    while True:
        body()
        sleep(20)
    
def show_arrow(direction: ArrowNames, interval: float = 0) -> None:
    display.show(direction.inner_image)

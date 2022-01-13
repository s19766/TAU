# Damian Eggert s19766

from calculator import Calculator
from termcolor import colored


def colored_text():
    sentence = "Hello You are using calculator"
    return colored(sentence, "red")


def add(a, b):
    cal = Calculator()
    return cal.addition(a, b)

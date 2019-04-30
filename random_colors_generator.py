from random import randint

# Function generating random  HEX color in a certain range of integers

def generate_random_color():
    number = randint(10242874,16746513)
    hex_color = str(hex(number))
    hex_color = '#' + hex_color[2:]
    return hex_color
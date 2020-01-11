
COLORS = {
    'Black': '\x1b[0;30m',
    'Blue': '\x1b[1;34m',
    'Green': '\x1b[0;32m',
    'Cyan': '\x1b[0;36m',
    'Red': '\x1b[1;31m',
    'Purple': '\x1b[0;35m',
    'Brown': '\x1b[0;33m',
    'Gray': '\x1b[0;37m',
    'Pink': '\x1b[38;5;200m',
    'Dark Gray': '\x1b[1;30m',
    'Light Blue': '\x1b[1;34m',
    'Light Green': '\x1b[1;32m',
    'Light Cyan': '\x1b[1;36m',
    'Light Red': '\x1b[1;31m',
    'Light Purple': '\x1b[1;35m',
    'Yellow': '\x1b[1;33m',
    'Light Grey': '\x1b[1;37m',

    'Top Bar': '\x1b[1;97;44m',
    'Bottom Bar': '\x1b[1;97;44m',
    'Normal': '\x1b[0;40;49m',
    
    'Bridge Color': '\x1b[48;5;130m',

    'Bullets Color': '\x1b[38;5;208m',
    'Extras Bridge': '\x1b[38;5;82m',
    'Water Color': '\x1b[48;5;39m',
    'Fish Color': '\x1b[38;5;130m',
    'Moving Bridges': '\x1b[48;5;94m'
}
END_COLOR = '\033[m'


def color_text(text, color):
    if '\x1b' in color:
        return color + text + END_COLOR
    else:
        try:
            letter = color[0]
            if letter.islower():
                letter = letter.upper()
            color = letter + color[1:]
            return COLORS[color] + text + END_COLOR
        except:
            return text

if __name__ == "__main__":
    print(color_text("Hello",'Water Color'),end="")
    print('Hello')
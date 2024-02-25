import os, re

#ForeGround
BLACK           = '\033[30m'
RED             = '\033[31m'
GREEN           = '\033[32m'
YELLOW          = '\033[33m'
BLUE            = '\033[34m'
MAGENTA         = '\033[35m'
CYAN            = '\033[36m'
WHITE           = '\033[37m'
RESET           = '\033[39m'
LIGHTBLACK   = '\033[90'
LIGHTRED     = '\033[91m'
LIGHTGREEN   = '\033[92m'
LIGHTYELLOW  = '\033[93m'
LIGHTBLUE    = '\033[94m'
LIGHTMAGENTA = '\033[95m'
LIGHTCYAN    = '\033[96m'
LIGHTWHITE   = '\033[97m'


#BackGround
BACK_BLACK           = '\033[40m'
BACK_RED             = '\033[41m'
BACK_GREEN           = '\033[42m'
BACK_YELLOW          = '\033[43m'
BACK_BLUE            = '\033[44m'
BACK_MAGENTA         = '\033[45m'
BACK_CYAN            = '\033[46m'
BACK_WHITE           = '\033[47m'
BACK_RESET           = '\033[49m'
BACK_WHITE2          = '\033[7m'
BACK_LIGHTBLACK   = '\033[100m'
BACK_LIGHTRED     = '\033[101m'
BACK_LIGHTGREEN   = '\033[102m'
BACK_LIGHTYELLOW  = '\033[103m'
BACK_LIGHTBLUE    = '\033[104m'
BACK_LIGHTMAGENTA = '\033[105m'
BACK_LIGHTCYAN    = '\033[106m'
BACK_LIGHTWHITE   = '\033[107m'

#Style
BRIGHT    = '\033[1m'
DIM       = '\033[2m'
NORMAL    = '\033[22m'
RESET_ALL = '\033[0m'
UNDERLINE = '\033[4m'
CROSSED = '\033[9m'
bold_underline = "\033[21m"
box_1 = "\033[51m"
box_2 = "\033[52m"
underline = '\033[4m'
underline_remove = '\033[24m'
bold = "\033[1m"
bold_remove = "\033[21m"
dim = "\033[2"
dim_remove = "\033[22"
blink = "\033[5m"
blink_remove = "\033[5m"
reverse = "\033[7m"
reverse_remvoe = "\033[27m"
hide = "\033[8m"
hide_remove = "\033[28m"

#Windows Terminal
Win_Black = "0"
Win_Blue = "1"
Win_Green = "2"
Win_BlueGray = "3"
Win_Red = "4"
Win_Purlple = "5"
Win_Yellow = "6"
Win_White = '7'
Win_Grey = "8"
Win_LightBlue = '9'
Win_LightGreen = "A"
Win_Cyan = "B"
Win_LightRed = "C"
Win_LightPurple = "D"
Win_LightYellow = 'E'
Win_LightWhite = 'F'
Win_bg = "0"



# Cursor movement
up          = '\x1b[A'
down        = '\x1b[B'
forward     = '\x1b[C'
back        = '\x1b[D'
next_line   = '\x1b[E'
prev_line   = '\x1b[F'
goto_x      = '\x1b[G'
erase       = '\x1b[J'
erase_line  = '\x1b[K'
clear_line = "\033[2K"
scroll_up   = '\x1b[S'
scroll_down = '\x1b[T'
save_cursor = '\x1b[s'
load_cursor = '\x1b[u'
show        = '\x1b[?25h'
hide        = '\x1b[?25l'
cursor_pos = lambda l, c: f"\033[{l};{c}H"
cursor_pos2 = lambda l, c: f"\033[{l};{c}f"
cursor_pos3 = lambda l, c: cursor_pos2(l, 0)+(c*forward)
cursor_lineup = lambda n: f"\033[{n}A"
cursor_linedown = lambda n: f"\033[{n}B"
cursor_column_right = lambda n: f"\033[{n}C"
cursor_column_left = lambda n: f"\033[{n}D"
clear_x0_y0 = "\033[2J"
clear_endline = "\033[K"
save_cursor_pos = "\033[s"
restore_cursor_pos = "\033[u"




def clear():
    """clear the terminal"""
    os.system("cls" if os.name == "nt" else "clear")


class Color:
    def __init__(self, colors:list=[], end_colors:list=[]) -> None:
        self.colors = colors
        self.end_colors = colors

    def print(self, *args, **kargs):
        print("".join(self.colors), *args, ''.join(self.end_colors), **kargs)


def cprint(*args, **kwargs):
    end = "\n"
    msg = ""
    for arg in args:
        try:
            if str(arg).startswith("\033[") and str(arg).endswith("m"):
                msg += f"{arg}"
            else:
                msg += f" {arg}"
        except ValueError:
            raise ValueError(f"Cannot convert {arg} into str")
    if kwargs.get('end'):
        end = kwargs.get('end')
        kwargs.pop('end')
    print(msg, **kwargs, end=f"{RESET_ALL}{end}{RESET_ALL}")




def hex_to_rgb(hex: str) -> tuple:
    """convert hexadecimal color to rgb"""
    rgb = []
    hex = hex.replace('#', '')
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)


def rgb_to_hex(r, g, b) -> str:
    """convert rgb color to hex"""
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)




def set_bg_color(color: str):
    """set background color of the terminal using the os default functions
    For windows, use the Win_... colors.
    """
    if os.name == 'nt':
        os.system(f'color {color}')
    else:
        os.system('setterm -term linux -back $'+color+' -fore white -clear')


def tinput(text: str = '', w: int = 30) -> str:
    """ask the user in a boxed input"""
    if len(text) > w:
        w = len(text)+5
    value = input(f"""╔{"═"*w}╗\n║{" "*w}║\n╚{"═"*w}╝{prev_line}║ {text}""")
    print()
    return value

    
def hex_bg_color(hex: str):
    """set this hexadecimal color as backgound"""
    print(f"\033]11;#{hex.replace('#', '')}\007", end="\r")

    
def rgb_bg_color(r, g, b):
    hex_bg_color(rgb_to_hex(r, g, b))

def bg_color(*args):
    if len(args) == 3:
        rgb_bg_color(*args)
    elif type(args[0]) in [list, tuple]:
        rgb_bg_color(args)
    else:
        hex_bg_color(args[0])
        
        
        


def get_rgb_print(r, g, b, background=False):
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def rgbprint(r, g, b, *args, background=False, **kwargs):
    """print the text with the rgb color"""
    cprint(get_rgb_print(r, g, b, background), *args, **kwargs)

def hexprint(hex, *args, background=False, **kwargs):
    """print the text with the exadecimal color"""
    rgbprint(*hex_to_rgb(hex), *args, background=background, **kwargs)


def colorless(text: str):
    pattern = re.compile("(\\x1b\[((\d;)*\d)*[a-zA-Z]{1})+")
    return pattern.sub("", text)


if __name__ == "__main__":
    clear()
    bg_color(*[50]*3)
    cprint(underline, "Welcome in color!")
    name = tinput(f'What is your name ?{RED}')
    cprint("Hello", YELLOW, name, RESET, "!")
    
import re
import os

reset = "\x1b[0m"

# Style add                 Style remove
underline = '\x1b[4m';      underline_remove = '\x1b[24m'
bold = "\x1b[1m";           bold_remove = "\x1b[21m"
dim = "\x1b[2";             dim_remove = "\x1b[22"
blink = "\x1b[5m";          blink_remove = "\x1b[25m"
reverse = "\x1b[7m";        reverse_remove = "\x1b[27m"
hide = "\x1b[8m";           hide_remove = "\x1b[28m"

# Text color:               Background Color
black = "\x1b[30m";         black_bg = "\x1b[40m"
black_bright = "\x1b[90m";  black_bg = "\x1b[100m"
red = "\x1b[31m";           red_bg = "\x1b[41m"
red_bright = "\x1b[91m";    red_bright_bg = "\x1b[101m"
green = "\x1b[32m";         green_bg = "\x1b[42m"
green_bright = "\x1b[92m";  green_bright_bg = "\x1b[102m"
yellow = "\x1b[33m";        yellow_bg = "\x1b[43m"
yellow_bright = "\x1b[93m"; yellow_bright_bg = "\x1b[103m"
blue = "\x1b[34m";          blue_bg = "\x1b[44m"
blue_bright = "\x1b[94m";   blue_bright_bg = "\x1b[104m"
magenta = "\x1b[35m";       magenta_bg = "\x1b[45m"
magenta_bright = "\x1b[95m";magenta_bright_bg = "\x1b[105m"
cyan = "\x1b[36m";          cyan_bg = "\x1b[46m"
cyan_bright = "\x1b[96m";   cyan_bright_bg = "\x1b[106m"
white = "\x1b[37m";         white_bg = "\x1b[47m"
white_bright = "\x1b[97m";  white_bright_bg = "\x1b[107m"
default = "\x1b[109m"


# Windows Terminal
Win_Black       = "0"
Win_Blue        = "1"
Win_Green       = "2"
Win_BlueGray    = "3"
Win_Red         = "4"
Win_Purlple     = "5"
Win_Yellow      = "6"
Win_White       = '7'
Win_Grey        = "8"
Win_LightBlue   = '9'
Win_LightGreen  = "A"
Win_Cyan        = "B"
Win_LightRed    = "C"
Win_LightPurple = "D"
Win_LightYellow = 'E'
Win_LightWhite  = 'F'
Win_bg          = "0"


# Cursor movement
up                  = '\x1b[A'
down                = '\x1b[B'
forward             = '\x1b[C'
back                = '\x1b[D'
next_line           = '\x1b[E'
prev_line           = '\x1b[F'
erase               = '\x1b[J'
erase_line          = '\x1b[K'
clear_line          = "\033[2K"
scroll_up           = '\x1b[S'
scroll_down         = '\x1b[T'
save_cursor         = '\x1b[s'
load_cursor         = '\x1b[u'
show_cursor         = '\x1b[?25h'
hide_cursor         = '\x1b[?25l'
cursor_pos          = lambda l, c: f"\x1b[{l};{c}H"
cursor_pos2         = lambda l, c: f"\x1b[{l};{c}f"
cursor_pos3         = lambda l, c: cursor_pos2(l, 0)+(c*forward)
cursor_lineup       = lambda n: f"\x1b[{n}A"
cursor_linedown     = lambda n: f"\x1b[{n}B"
cursor_column_right = lambda n: f"\x1b[{n}C"
cursor_column_left  = lambda n: f"\x1b[{n}D"
clear_x0_y0         = "\x1b[2J"
clear_endline       = "\x1b[K"
save_cursor_pos     = "\x1b[s"
restore_cursor_pos  = "\x1b[u"
flush               = "\x1b[F"

pattern = re.compile(r"\x1b\[(\d*;)*\d*[a-zA-Z]{1}\ ?")

def clear() -> None:
    """
    clear the terminal
    """
    os.system("cls" if os.name == "nt" else "clear")

def terminal_size() -> tuple[int, int]:
    """
    get the terminal size: colums, lines
    """
    return int(os.get_terminal_size().columns), int(os.get_terminal_size().lines)


def is_color(string: str) -> bool:
    """
    Check if a string has a color.
    """
    return bool(re.search(pattern, string))


def colorless(text: str) -> str:
    """
    Remove all colors.
    """
    return pattern.sub("", text)


def cprint(*args, **kwargs) -> str:
    """
    Prints normally but accept colors:
    - Doesn't add wierd spaces when printing consecutive colors separated by a comma
    - Resets the color at the end
    - Returns a colorless version of the printed text
    """
    end = "\n"
    msg = ""
    for i in range(len(args)):
        word = str(args[i])
        nxt = str(args[i+1]) if i+1 < len(args) else None
        if is_color(word) or is_color(str(nxt)):
            msg += word
        elif nxt:
            msg += word+" "
        else:
            msg += word
    if kwargs.get('end') is not None:
        end = kwargs.get('end')
        kwargs.pop('end')

    print(msg, **kwargs, end=f"{reset}{end}{reset}")
    return colorless(msg)


def custom(r: int, g: int, b: int, bg: bool = False) -> str:
    return "\x1b[{};2;{};{};{}m".format(48 if bg else 38, r, g, b)

def hex_to_rgb(hex: str) -> tuple:
    """
    convert hexadecimal color to rgb
    """
    rgb = []
    hex = hex.replace('#', '')
    for i in (0, 2, 4):
        decimal = int(hex[i:i+2], 16)
        rgb.append(decimal)
    return tuple(rgb)


def rgb_to_hex(r, g, b) -> str:
    """
    convert rgb color to hex
    """
    return '#{:02x}{:02x}{:02x}'.format(r, g, b)




def set_bg_color(color: str) -> None:
    """
    set background color of the terminal using the os default functions
    For windows, use the Win_... colors.
    """
    if os.name == 'nt':
        os.system(f'color {color}')
    else:
        os.system('setterm -term linux -back $'+color+' -fore white -clear')


def tinput(text: str = '', w: int = 30) -> str:
    """
    ask the user in a boxed input
    """
    if len(text) > w:
        w = len(text)+5
    value = input(f"""╔{"═"*w}╗\n║{" "*w}║\n╚{"═"*w}╝{cursor_lineup}║ {text}""")
    print()
    return value

    
def hex_bg_color(hex: str) -> None:
    """
    set this hexadecimal color as backgound
    """
    print(f"\033]11;#{hex.replace('#', '')}\007", end="\r")

    
def rgb_bg_color(r, g, b) -> None:
    hex_bg_color(rgb_to_hex(r, g, b))

def bg_color(*args) -> None:
    if len(args) == 3:
        rgb_bg_color(*args)
    elif type(args[0]) in [list, tuple]:
        rgb_bg_color(args)
    else:
        hex_bg_color(args[0])
        
        
        
def get_rgb_print(r, g, b, background=False) -> str:
    return '\033[{};2;{};{};{}m'.format(48 if background else 38, r, g, b)

def rgbprint(r, g, b, *args, background=False, **kwargs) -> None:
    """
    print the text with the rgb color
    """
    cprint(get_rgb_print(r, g, b, background), *args, **kwargs)

def hexprint(hex, *args, background=False, **kwargs) -> None:
    """
    print the text with the exadecimal color
    """
    rgbprint(*hex_to_rgb(hex), *args, background=background, **kwargs)



if __name__ == "__main__":
    # You can extract a colorless version of the printed text
    print("Colored:",end="")
    colorless_print = cprint("\t", bold, black, "You", red_bg, "Tube")
    print(f"Uncolored:{colorless_print}")
    print("\nCustom color:")
    cprint(custom(200, 120, 0), "Orange")
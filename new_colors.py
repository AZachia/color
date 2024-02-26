
import re

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

# Other:
clear_line = "\x1b[2K"
cursor_pos = lambda l, c: f"\x1b[{l};{c}H"
cursor_pos2 = lambda l, c: f"\x1b[{l};{c}f"
cursor_lineup = lambda n: f"\x1b[{n}A"
cursor_linedown = lambda n: f"\x1b[{n}B"
cursor_column_right = lambda n: f"\x1b[{n}C"
cursor_column_left = lambda n: f"\x1b[{n}D"
clear_x0_y0 = "\x1b[2J"
clear_endline = "\x1b[K"
save_cursor_pos = "\x1b[s"
restore_cursor_pos = "\x1b[u"
flush = "\x1b[F"
pattern = re.compile(r"\x1b\[(\d*;)*\d*[a-zA-Z]{1}\ ?")


def is_color(string: str):
    """
    Check if a string is a color.
    """
    return bool(re.search(pattern, string))


def colorless(*args):
    """
    Remove all colors and additionnal spaces.
    """
    text = ""
    for arg in args:
        text+=f"{arg}"
    return pattern.sub("", text)


def cprint(*args, **kwargs):
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


def custom(r: int, g: int, b: int, bg: bool = False):
    return "\x1b[{};2;{};{};{}m".format(48 if bg else 38, r, g, b)


if __name__ == "__main__":
    # You can extract a colorless version of the printed text
    print("Colored:",end="")
    colorless_print = cprint("\t", bold, black, "You", red_bg, "Tube")
    print(f"Uncolored:{colorless_print}")
    print("\nCustom color:")
    cprint(custom(200, 120, 0), "Orange")
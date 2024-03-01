import color
from color import cprint

print("\nNormal print:")
print(color.red, color.underline, "Hello ", color.green, "World !")
print(f"{color.reset}↑↑      ↑↑\nWierd spaces (expected only the first space) and you have to manually reset the color at the end")

print("\ncprint:")
clrless = cprint(color.red, color.underline, "Hello ", color.green, "World !")
print("No wierd spaces, and no need to manually reset color")
print("\nAnd you can also extract a colorless version of the printed text:")
print(clrless)

for style in color.decorations:
    color.table([[style]], style=style)

import new_colors as colors
from new_colors import cprint

print("\nNormal print:")
print(colors.red, colors.underline, "Hello ", colors.green, "World !")
print(f"{colors.reset}↑↑      ↑↑\nWierd spaces (expected only the first space) and you have to manually reset the color at the end")

print("\ncprint:")
clrless = cprint(colors.red, colors.underline, "Hello ", colors.green, "World !")
print("No wierd spaces, and no need to manually reset color")
print("\nAnd you can also extract a colorless version of the printed text:")
print(clrless)

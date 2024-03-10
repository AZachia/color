# color
color tools for terminal written in python

<img src="https://skillicons.dev/icons?i=py&perline=12" />

![image](screenshot.PNG)

## Installation

Copy the [color.py](https://github.com/AZachia/color/blob/main/color.py) file in your directory.

## Documentation
### Displaying colors

 - import the library:
```python
import color
from color import cprint
```

 - to display colored text:
```python
cprint(color.red + "red text")
# or
cprint(color.blue, "blue text")
# or
cprint(f"{color.yellow}yellow text")
```

 - clear the terminal:

 ```python
color.clear()
```

 - Print Hexadecimal or RGB colors:

```python
# Foreground
cprint(color.get_rgb_print(200, 120, 0), "Orange text")
cprint(color.get_hex_print("#0000FF"), "Blue text")

# Background
cprint(color.get_rgb_print(200, 120, 0, True), "Orange background")
cprint(color.get_hex_print("#0000FF", True), "Blue background")
```

### Cursor movement

with this library, you can control the cursor easily.

 - Show and hide the cursor:
  ```python
print(color.hide_cursor)
print("You don't see the cursor")
print(color.show_cursor)
print("You see it now !")
```
- Moving the cursor:
 ```python
print("hello ", end="")
print(color.next_line, end="")
print("I am down")
print(color.prev_line*2, end="")
print(color.forward*6 + "world")
print(color.next_line, end="")
```

### Miscellaneous

 - dispay a table: 
 ```python
 color.table([["You can also", "Print tables"], ["in a few steps", "and with a nice result"]], samesize=True, align="center", padding=2)
 ```
result: 
```
╭────────────────────────┬────────────────────────╮
│      You can also      │      Print tables      │
├────────────────────────┼────────────────────────┤
│     in a few steps     │ and with a nice result │
╰────────────────────────┴────────────────────────╯
```

 - get nice user inputs:
 ```python
 name = color.tinput("What is your name ? ", 30, True, "rounded", bold, green)
 print(name)
 ```

## Styles:

```
╔══════╗
║double║      
╚══════╝      
╭───────╮     
│rounded│     
╰───────╯     
┌─────┐       
│light│       
└─────┘       
┏━━━━┓        
┃bold┃        
┗━━━━┛        
              
 none         
              
┌┄┄┄┄┄┄┄┄┄┄┄┄┐
┊dotted-light┊
└┄┄┄┄┄┄┄┄┄┄┄┄┘
┏┅┅┅┅┅┅┅┅┅┅┅┓
┋dotted-bold┋
┗┅┅┅┅┅┅┅┅┅┅┅┛
.....
.dot.
.....

••••••••••
•dot-bold•
••••••••••

╔══════╗      
║double║      
╚══════╝      

╭───────╮     
│rounded│     
╰───────╯     

┌─────┐       
│light│       
└─────┘       

┏━━━━┓        
┃bold┃        
┗━━━━┛        


 none


┌┄┄┄┄┄┄┄┄┄┄┄┄┐
┊dotted-light┊
└┄┄┄┄┄┄┄┄┄┄┄┄┘

┏┅┅┅┅┅┅┅┅┅┅┅┓ 
┋dotted-bold┋ 
┗┅┅┅┅┅┅┅┅┅┅┅┛ 

.....
.dot.
.....

••••••••••
•dot-bold•
••••••••••

⋚≋≋≋≋≋≋⋛
∣zigzag∣
⋝≋≋≋≋≋≋⋜

⋜≈≈≈≈≈⋝
∥waves∥
⋟≈≈≈≈≈⋞

✵✶✶✶✶✶✵
✷stars✷
✵✶✶✶✶✶✵

○○○○○○○○○
○circles○
○○○○○○○○○

██████
█hash█
██████

■■■■■■■■■■■■■
■dots-square■
■■■■■■■■■■■■■

▓▓▓▓▓▓▓▓▓
▓checker▓
▓▓▓▓▓▓▓▓▓
```

Used in [Termial Video player](https://github.com/AZachia/Terminal-Video-player)


Written by [Galky](https://github.com/Gvlky) & [me](https://github.com/AZachia)

<img src="https://github.com/gvlky.png" width="60px;" style="border-radius:100px"/><img src="https://github.com/AZachia.png" width="60px;" style="border-radius:100px"/>

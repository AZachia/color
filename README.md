# color
color tools for terminal written in python

<img src="https://skillicons.dev/icons?i=py&perline=12" />

![image](screenshot.PNG)

## Installation

Copy the [color.py](https://github.com/AZachia/color/blob/main/color.py) file in your directory.

## Documentation

 - import the library:
```python
import color
from color import cprint
```

 - to display colored text:
```python
import color
from color import cprint

cprint(color.red + "red text")
# or
cprint(color.blue, "blue text")
# or
cprint(f"{color.yellow}yellow text")
```

 - clear the terminal:

 ```python
import color
color.clear()
```



Written by [Galky](https://github.com/Gvlky) & [me](https://github.com/AZachia)

<img src="https://github.com/gvlky.png" width="60px;" style="border-radius:100px"/><img src="https://github.com/AZachia.png" width="60px;" style="border-radius:100px"/>
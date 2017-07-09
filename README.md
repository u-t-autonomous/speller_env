# speller_env

# GUI

##### Launching GUI

```bash
python config_gui.py [configFile]
```

The GUI prompts for inputs on the command line while running

##### Parameters:

configFile (optional) - open a config file to edit



## Dependencies

* Python 3.5
* Pygame
* csv

## Documentation

### Instantiating

```python
P300(s_x = 640, s_y = 480)
```

##### Parameters:

s_x = int

s_y = int

##### Returns:

An instance of P300()

##### Usage:
```python
P3 = P300(640, 480)
```

### Getting Current State

```python
P3.get_state()
```

##### Parameters:

None

##### Returns:

List

### Move Command

```python
P3.move(num)
```

##### Parameters:

num = 0, num = 1, or num = 2
##### Returns:

Int: the current row or column number

Int: the current letter coordinate

String: the current output string

##### Usage:
```python
P3.move(1)
```

### Getting the log

Simulation.show_log()

##### Parameters:

None

##### Returns:

Dictionary: The entire log

##### Usage:

```python
P3.show_log()
```

## Usage Example

```python
from Speller import P300
import pygame
import csv
pygame.init()
P3 = P300(800, 800)
done = False
while not done:
    x = int(input("enter 0, 1, or 2: "))
    if x != 0 and x != 1 and x != 2:
        done = True
    else:
        P3.move(x)
        P3.get_state()
P3.show_log()
```

## Developers

* [@batman13524](https://github.com/batman13524)
* [@sahabi](https://github.com/sahabi)


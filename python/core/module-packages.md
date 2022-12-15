# Modules & Packages

## Modules

Modules in python are simply python files. Importing python module is simply as importing the python file:

```py
# points.py
class Point():
    def __ini__(self):
        # Provides point initialization code
        pass

# main.py
from points import Point

def main():
    p = Point()

    pass

if __name__ == '__main__':
    main()
```

**Note**
When a module is imported in a calling program or module, the imported module is part of the calling program/module `namespace`

**Note** `as` keyword
Python support class or type alising using as keyword:

```py
# main.py
from points import Point as Pt

def main():
    p = Pt()

    pass

if __name__ == '__main__':
    main()
```

**Utils**

> type(module) -> returns a python object

> isinstance(module_name, types.ModuleType) -> Returns true if module_name is an imported module

> hex(id(module_name)) -> Return the memory address of the module object

```py
import module1
from types import ModuleType

print(type(module1)) # Returns an object

isinstance(module1, ModuleType) # Returns true

print(hex(id(module_name))) # Memory address of the module object

__file__ # GLobal object which the name of the current python script
__package__ # Package name
__name__ # Name of the module
__loader__ # Module loader global
__cached__ # Indicates whether the module is cached
__doc__ # Returns the docstring of the module

module.__dict__['__file__'] # Returns the absolute path to the module file
```

## Packages

Python treat directory containing module files as package. In each folder that might be considered a package, a `__init__.py` file is placed:

```py
# /root_dir
# /root_dir/main.py


# /root_dir/drawing/
# /root_dir/drawing/__init__.py


# /root_dir/drawing/point.py

# /root_dir/drawing/maths/
# /root_dir/drawing/maths/__init__.py
# /root_dir/drawing/maths/distance.py
```

- relative import

Relative import specific the location of the classes to be imported relative to the current package:

```py

# /root_dir/drawing/point.py
from .maths.distance import get_distance

# /root_dir/drawing/maths/distance.py
import ..types import Algo

# /root_dir/main.py
def main():
    p = Pt()

    pass

if __name__ == '__main__':
    main()
```

- absolute import

```py
# main.py
# Absolute import specifying full dot seperateed path to the module
from drawing.points import Point


def main():
    p = Point()

    pass

if __name__ == '__main__':
    main()
```

- __init__.py

Use the `__init__.py` to import code directly from a package instead of a module. `__init__.py` are similar to `index.ts` in typescript for exporting classes from a subfolder.

```py
# /root_dir/drawing/__init__.py
from .points import Point

# /root_dir/main.py

# we can now import point from package level instead of module level
from drawing import Point

def main():
    p = Point()

    pass

if __name__ == '__main__':
    main()
```

- __path__

`__path__` return the path to the package directory.

## Python Garbage collector

```py
import socket

del socket
```

`del` keyword unset the module object as it will doe with any variable. Python does not remove the objec from the global, cache in order to fast build it when requested by the application user, the deleted module or variable is kepts in cache until the garbage collected is called to free memory.


```py
import importlib

importlib.reload(module) # Reuse existing module if exist else create a new reference

importlib.import_module(module) # Import module without using import statement like require() js
```

-- Manually loading python module

```py
import sys
from types import ModuleType

name='my_module'
file='/workspaces/module.py'

mod = ModuleType(name)
mod.__file__ = file

# Set the module reference in sys modules
sys.modules[name] = mod

with open(file, 'r') as source_code:
    content = source_code.read()

    # Compile the source code into executable
    code = compile(content, filename=file, mode='exec')

    # Execute the compiled code. Here we need to sepecufy the module dictionary
    exec(code, mod.__dict__)

    # Call module function
    mod.func_name()
```

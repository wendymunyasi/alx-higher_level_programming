# Project Name
**0x0C. Python - Almost a circle**

## Author's Details
Name: *Wendy Munyasi.*

Email: *wendymunyasi@gmail.com*

Tel: *+254707240068.*

##  Requirements

### Python Scripts
*   Allowed editors: `vi`, `vim`, `emacs`.
*   All your files will be interpreted/compiled on Ubuntu 20.04 LTS using gcc, using python3 (version 3.8.5).
*   All your files should end with a new line.
*   The `main.py` files are used to test your functions, but you don’t have to push them to your repo.
*   The first line of all your files should be exactly `#!/usr/bin/python3`.
*   Your code should use the pycodestyle (version `2.8.*`).
*   All your files must be executable.
*   All your test files should be inside a folder `tests`.
*   All your test files should be text files (extension: `.txt`).
*   All your tests should be executed by using this command: `python3 -m doctest ./tests/*`.
*   The length of your files will be tested using `wc`.
*   All your modules should have a documentation (`python3 -c 'print(__import__("my_module").__doc__)'`).
*   All your classes should have a documentation (`python3 -c 'print(__import__("my_module").MyClass.__doc__)'`).
*   All your functions (inside and outside a class) should have a documentation (`python3 -c 'print(__import__("my_module").my_function.__doc__)`' and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)'`).
*   A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified).


## Project Description
What is Unit testing and how to implement it in a large project.
How to serialize and deserialize a Class.
How to write and read a JSON file.
What is `*args` and how to use it.
What is `**kwargs` and how to use it.
How to handle named arguments in a function.


* **0. If it's not tested it doesn't work** - All your files, classes and methods must be unit tested and be PEP 8 validated. `tests/`.
* **1. Base class** - Write the first class `Base`. - `models/base.py`, `models/__init__.py`.
* **2. First Rectangle** - Write the class `Rectangle` that inherits from `Base`. - `models/rectangle.py`.
* **3. Validate attributes** - Update the class `Rectangle` by adding validation of all setter methods and instantiation (`id` excluded). - `models/rectangle.py`.
* **4. Area first** - Update the class `Rectangle` by adding the public method `def area(self):` that returns the area value of the `Rectangle` instance. - `models/rectangle.py`.
* **5. Display #0** - Update the class `Rectangle` by adding the public method `def display(self):` that prints in stdout the `Rectangle` instance with the character `#` - you don’t need to handle `x` and `y` here. - `models/rectangle.py`.
* **6. __str__** - Update the class `Rectangle` by overriding the `__str__` method so that it returns `[Rectangle] (<id>) <x>/<y> - <width>/<height>`. - `models/rectangle.py`.
* **7. Display #1** - Update the class `Rectangle` by improving the public method `def display(self):` to print in stdout the `Rectangle` instance with the character `#` by taking care of `x` and `y`. - `models/rectangle.py`.
* **8. Update #0** - Update the class `Rectangle` by adding the public method `def update(self, *args):` that assigns an argument to each given attribute. - `models/rectangle.py`.
* **9. Update #1** - Update the class `Rectangle` by updating the public method `def update(self, *args):` by changing the prototype to `update(self, *args, **kwargs)` that assigns a key/value argument to attributes -. `models/rectangle.py`.
* **10. And now, the Square!** - Write the class `Square` that inherits from `Rectangle`. - `models/square.py`.
* **11. Square size** - Update the class `Square` by adding the public getter and setter `size`. - `models/square.py`.
* **12. Square update** - Update the class `Square` by adding the public method `def update(self, *args, **kwargs):` that assigns the given attributes. - `models/square.py`.
* **13. Rectangle instance to dictionary representation** - Update the class `Rectangle` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Rectangle`. This dictionary must contain `id`, `width`, `height`, `x` and `y`. - `models/rectangle.py`.
* **14. Square instance to dictionary representation** - Update the class `Square` by adding the public method `def to_dictionary(self):` that returns the dictionary representation of a `Square`. This dictionary must contain `id`, `size`, `x`, and `y`. - `models/square.py`.
* **15. Dictionary to JSON string** - Update the class `Base` by adding the static method `def to_json_string(list_dictionaries):` that returns the JSON string representation of `list_dictionaries`. - `models/base.py`.
* **16. JSON string to file** - Update the class `Base` by adding the class method `def save_to_file(cls, list_objs):` that writes the JSON string representation of `list_objs` to a file. - `models/base.py`.
* **17. JSON string to dictionary** - Update the class `Base` by adding the static method `def from_json_string(json_string):` that returns the list of the JSON string representation `json_string`. - `models/base.py`.
* **18. Dictionary to Instance** - Update the class `Base` by adding the class method `def create(cls, **dictionary):` that returns an instance with all attributes already set. - `models/base.py`.
* **19. File to instances** - Update the class `Base` by adding the class method `def load_from_file(cls):` that returns a list of instances. - `models/base.py`.
* **20. JSON ok, but CSV?** - Update the class `Base` by adding the class methods `def save_to_file_csv(cls, list_objs):` and `def load_from_file_csv(cls):` that serializes and deserializes in CSV. - `models/`.
* **21. Let's draw it** - Update the class `Base` by adding the static method `def draw(list_rectangles, list_squares):` that opens a window and draws all the `Rectangles` and `Squares`. - `models/base.py`.


## Collaborate

To collaborate, reach me through my email address wendymunyasi@gmail.com.

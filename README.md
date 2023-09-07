# Python

Python is a popular programming language. It was created by Guido van Rossum, and released in 1991.

It is used for:

* `web development (server-side),`
* `software development,`
* `mathematics,`
* `system scripting.`


**What can Python do?**

* Python can be used on a server to create web applications.
* Python can be used alongside software to create workflows.
* Python can connect to database systems. It can also read and modify files.
* Python can be used to handle big data and perform complex mathematics.
* Python can be used for rapid prototyping, or for production-ready software development.


**Why Python?**

* Python works on different platforms (Windows, Mac, Linux, Raspberry Pi, etc).
* Python has a simple syntax similar to the English language.
* Python has syntax that allows developers to write programs with fewer lines than some other programming languages.
* Python runs on an interpreter system, meaning that code can be executed as soon as it is written. This means that prototyping can be very quick.
* Python can be treated in a procedural way, an object-oriented way or a functional way.

**Good to know**

* The most recent major version of Python is Python 3, which we shall be using in this tutorial. However, Python 2, although not being updated with anything other than security updates, is still quite popular.
* In this tutorial Python will be written in a text editor. It is possible to write Python in an Integrated Development Environment, such as Thonny, Pycharm, Netbeans or Eclipse which are particularly useful when managing larger collections of Python files.

**Python Syntax compared to other programming languages**

* Python was designed for readability, and has some similarities to the English language with influence from mathematics.
* Python uses new lines to complete a command, as opposed to other programming languages which often use semicolons or parentheses.
* Python relies on indentation, using whitespace, to define scope; such as the scope of loops, functions and classes. Other programming languages often use curly-brackets for this purpose.

**Python Comments**

* Comments can be used to explain Python code.
* Comments can be used to make the code more readable.
* Comments can be used to prevent execution when testing code.

**Python Variables**

* Variables are containers for storing data values. A variable is created the moment you first assign a value to it. Variables do not need to be declared with any particular type, and can even change type after they have been set.

* `Casting:` If you want to specify the data type of a variable, this can be done with casting.

* `Get the Type:` You can get the data type of a variable with the `type()` function.

* `Single or Double Quotes:` String variables can be declared either by using single or double quotes

* `Case-Sensitive:` Variable names are case-sensitive.

* `Variable Names:` A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume). Rules for Python variables:

    * A variable name must start with a letter or the underscore character
    * A variable name cannot start with a number
    * A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
    * Variable names are case-sensitive (age, Age and AGE are three different variables)
    * A variable name cannot be any of the Python keywords.
    * Python allows you to assign values to multiple variables in one line
                        `x, y, z = "Orange", "Banana", "Cherry"`
    * If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

    * `Global Variable:` Variables that are created outside of a function (as in all of the examples above) are known as global variables. Global variables can be used by everyone, both inside of functions and outside. If you create a variable with the same name inside a function, this variable will be local, and can only be used inside the function. The global variable with the same name will remain as it was, global and with the original value.

**Built-in Data Types:**
Variables can store data of different types, and different types can do different things. Python has the following data types built-in by default, in these categories:

| **Data Type**      | **Python Type**     |
|-----------------|-----------------|
| Text Type       | `str`           |
| Numeric Types   | `int`, `float`, `complex` |
| Sequence Types  | `list`, `tuple`, `range` |
| Mapping Type    | `dict`          |
| Set Types       | `set`, `frozenset` |
| Boolean Type    | `bool`          |
| Binary Types    | `bytes`, `bytearray`, `memoryview` |
| None Type       | `NoneType`      |


**Strings in python**
Strings in python are surrounded by either single quotation marks, or double quotation marks. In python `'hello'` is the same as `"hello"`. You can display a string literal with the `print()` function.

* `Assigning a variable to the string:` Assigning a string to a variable is done with the variable name followed by an equal sign and the string.
* `Multiline string:` You can assign a multiline string to a variable by using three quotes.
* `Strings are Arrays:` Like many other popular programming languages, strings in Python are arrays of bytes representing unicode characters. However, Python does not have a character data type, a single character is simply a string with a length of 1. Square brackets can be used to access elements of the string.
* `Looping Through a String:` Since strings are arrays, we can loop through the characters in a string, with a `for` loop.
* `String Length:` To get the length of a string, use the `len()` function.
* `Check String:` To check if a certain phrase or character is present in a string, we can use the keyword `in`.
* `Check if NOT:` To check if a certain phrase or character is NOT present in a string, we can use the keyword `not in`.
* `Slicing:` You can return a range of characters by using the slice syntax. Specify the start index and the end index, separated by a colon, to return a part of the string.
* `Slice From the Start:` By leaving out the start index, the range will start at the first character.
* `Slice To the End:` By leaving out the end index, the range will go to the end.
* `Negative Indexing:` Use negative indexes to start the slice from the end of the string.
* `Modify Strings:` Python has a set of built-in methods that you can use on strings.
* `Upper Case:` The `upper()` method returns the string in upper case.
* `Lower Case`: The `lower()` method returns the string in lower case
* `Remove Whitespace:` Whitespace is the space before and/or after the actual text, and very often you want to remove this space. The `strip()` method removes any whitespace from the beginning or the end.
* `Replace String:` The `replace()` method replaces a string with another string.
* `Split String:` The `split()` method returns a list where the text between the specified separator becomes the list items.
* `String Concatenation:` To concatenate, or combine, two strings you can use the + operator.
*` String Format:` As we learned in the Python Variables chapter, we cannot combine strings and numbers like this But we can combine strings and numbers by using the `format()` method! The format() method takes the passed arguments, formats them, and places them in the string where the placeholders {} are The format() method takes unlimited number of arguments, and are placed into the respective placeholders. You can use index numbers {0} to be sure the arguments are placed in the correct placeholders
* `Escape Character:` To insert characters that are illegal in a string, use an escape character. An escape character is a backslash `\` followed by the character you want to insert. An example of an illegal character is a double quote inside a string that is surrounded by double quotes

| **Escape Sequence** | **Result**         |
|-----------------|----------------|
| `\'`            | Single Quote   |
| `\\`            | Backslash      |
| `\n`            | New Line       |
| `\r`            | Carriage Return|
| `\t`            | Tab            |
| `\b`            | Backspace      |
| `\f`            | Form Feed      |
| `\ooo`          | Octal value    |
| `\xhh`          | Hex value      |

* String Methods: Python has a set of built-in methods that you can use on strings. They are

| **Method**         | **Description**                                               |
| -------------- | --------------------------------------------------------- |
| capitalize()   | Converts the first character to upper case               |
| casefold()     | Converts string into lower case                           |
| center()       | Returns a centered string                                 |
| count()        | Returns the number of times a specified value occurs in a string |
| encode()       | Returns an encoded version of the string                 |
| endswith()     | Returns true if the string ends with the specified value |
| expandtabs()   | Sets the tab size of the string                           |
| find()         | Searches the string for a specified value and returns the position of where it was found |
| format()       | Formats specified values in a string                      |
| format_map()   | Formats specified values in a string                      |
| index()        | Searches the string for a specified value and returns the position of where it was found |
| isalnum()      | Returns True if all characters in the string are alphanumeric |
| isalpha()      | Returns True if all characters in the string are in the alphabet |
| isascii()      | Returns True if all characters in the string are ascii characters |
| isdecimal()    | Returns True if all characters in the string are decimals |
| isdigit()      | Returns True if all characters in the string are digits  |
| isidentifier() | Returns True if the string is an identifier               |
| islower()      | Returns True if all characters in the string are lower case |
| isnumeric()    | Returns True if all characters in the string are numeric |
| isprintable()  | Returns True if all characters in the string are printable |
| isspace()      | Returns True if all characters in the string are whitespaces |
| istitle()      | Returns True if the string follows the rules of a title  |
| isupper()      | Returns True if all characters in the string are upper case |
| join()         | Joins the elements of an iterable to the end of the string |
| ljust()        | Returns a left justified version of the string           |
| lower()        | Converts a string into lower case                         |
| lstrip()       | Returns a left trim version of the string                 |
| maketrans()    | Returns a translation table to be used in translations    |
| partition()    | Returns a tuple where the string is parted into three parts |
| replace()      | Returns a string where a specified value is replaced with a specified value |
| rfind()        | Searches the string for a specified value and returns the last position of where it was found |
| rindex()       | Searches the string for a specified value and returns the last position of where it was found |
| rjust()        | Returns a right justified version of the string          |
| rpartition()   | Returns a tuple where the string is parted into three parts |
| rsplit()       | Splits the string at the specified separator, and returns a list |
| rstrip()       | Returns a right trim version of the string                |
| split()        | Splits the string at the specified separator, and returns a list |
| splitlines()   | Splits the string at line breaks and returns a list      |
| startswith()   | Returns true if the string starts with the specified value |
| strip()        | Returns a trimmed version of the string                   |
| swapcase()     | Swaps cases, lower case becomes upper case and vice versa |
| title()        | Converts the first character of each word to upper case   |
| translate()    | Returns a translated string                               |
| upper()        | Converts a string into upper case                         |
| zfill()        | Fills the string with a specified number of 0 values at the beginning |



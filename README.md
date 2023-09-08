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


**Boolean Values**

In programming you often need to know if an expression is `True or False`. You can evaluate any expression in Python, and get one of two answers, `True or False`. When you compare two values, the expression is evaluated and Python returns the Boolean answer.

When you run a condition in an if statement, Python returns `True or False`.

* `Evaluate Values and Variables:`The bool() function allows you to evaluate any value, and give you True or False in return.

* `Most Values are True:` Almost any value is evaluated to True if it has some sort of content. Any string is True, except empty strings. Any number is True, except 0. Any list, tuple, set, and dictionary are True, except empty ones.

* `Some Values are False:` In fact, there are not many values that evaluate to `False`, except empty values, such as `(), [], {}, ""`, the number `0`, and the value `None`. And of course the value `False` evaluates to `False`.

**Operators:** Operators are used to perform operations on variables and values. Python divides the operators in the following groups:

* `Arithmetic operators:` Arithmetic operators are used with numeric values to perform common mathematical operations

| Operator        | Name            | Example    |
|-----------------|-----------------|------------|
| +               | Addition        | `x + y`    |
| -               | Subtraction     | `x - y`    |
| *               | Multiplication  | `x * y`    |
| /               | Division        | `x / y`    |
| %               | Modulus         | `x % y`    |
| **              | Exponentiation  | `x ** y`   |
| //              | Floor division  | `x // y`   |

* `Assignment operators:` Assignment operators are used to assign values to variables

| Operator | Example | Same As |
| -------- | ------- | ------- | 
| =        | x = 5   | x = 5   |
| +=       | x += 3  | x = x + 3 |
| -=       | x -= 3  | x = x - 3 |
| *=       | x *= 3  | x = x * 3 |
| /=       | x /= 3  | x = x / 3 |
| %=       | x %= 3  | x = x % 3 |
| //=      | x //= 3 | x = x // 3 |
| **=      | x **= 3 | x = x ** 3 |
| &=       | x &= 3  | x = x & 3 | 
| |=       | x |= 3  | x = x | 3 | 
| ^=       | x ^= 3  | x = x ^ 3 | 
| >>=      | x >>= 3 | x = x >> 3 | 
| <<=      | x <<= 3 | x = x << 3 | 
* `Comparison operators:` Comparison operators are used to compare two values

| Operator                | Name                           | Example        |
|-------------------------|--------------------------------|----------------|
| `==`                    | Equal                          | `x == y`       |
| `!=`                    | Not equal                      | `x != y`       |
| `>`                     | Greater than                   | `x > y`        |
| `<`                     | Less than                      | `x < y`        |
| `>=`                    | Greater than or equal to       | `x >= y`       |
| `<=`                    | Less than or equal to          | `x <= y`       |

* `Logical operators:` Logical operators are used to combine conditional statements.

| Operator | Description                                  | Example                     |
| -------- | -------------------------------------------- | --------------------------- |
| `and`    | Returns True if both statements are true    | `x < 5 and x < 10`          |
| `or`     | Returns True if one of the statements is true | `x < 5 or x < 4`            |
| `not`    | Reverse the result, returns False if true    | `not(x < 5 and x < 10)`     |

* `Identity operators:` Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location.

| Operator  | Description                                       | Example        |
|-----------|---------------------------------------------------|----------------|
| is        | Returns True if both variables are the same object | `x is y`       |
| is not    | Returns True if both variables are not the same object | `x is not y`  |

* `Membership operators:` Membership operators are used to test if a sequence is presented in an object.

| Operator | Description                                     | Example         |
|----------|-------------------------------------------------|-----------------|
| `in`     | Returns True if a sequence with the specified  | `x in y`        |
|          | value is present in the object                  |                 |
| `not in` | Returns True if a sequence with the specified  | `x not in y`    |
|          | value is not present in the object              |                 |


* `Bitwise operators:` Bitwise operators are used to compare (binary) numbers

| Operator | Description                                     | Example         |
|----------|-------------------------------------------------|-----------------|
| `in`     | Returns True if a sequence with the specified  | `x in y`        |
|          | value is present in the object                  |                 |
| `not in` | Returns True if a sequence with the specified  | `x not in y`    |
|          | value is not present in the object              |                 |

* `Precedence Operator:` Operator precedence describes the order in which operations are performed.

| Operator                    | Description                                       |
| ----------------------------| ------------------------------------------------- |
| ()                          | Parentheses                                       |
| **                          | Exponentiation                                    |
| +x, -x, ~x                  | Unary plus, unary minus, and bitwise NOT         |
| * / // %                    | Multiplication, division, floor division, and modulus |
| + -                         | Addition and subtraction                         |
| << >>                        | Bitwise left and right shifts                    |
| &                            | Bitwise AND                                       |
| ^                            | Bitwise XOR                                       |
| \|                           | Bitwise OR                                        |
| == != > >= < <= is is not in not in | Comparisons, identity, and membership operators |
| not                          | Logical NOT                                       |
| and                          | AND                                               |
| or                           | OR                                                |

**Python Lists**

Lists are used to store multiple items in a single variable. Lists are one of 4 built-in data types in Python used to store collections of data, the other 3 are `Tuple, Set, and Dictionary`, all with different qualities and usage.

* `List Items:` List items are ordered, changeable, and allow duplicate values. List items are indexed, the first item has index [0], the second item has index [1] etc.
* `Ordered:` When we say that lists are ordered, it means that the items have a defined order, and that order will not change. If you add new items to a list, the new items will be placed at the end of the list.
* `Changeable:` The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.
* `Allow Duplicates:` Since lists are indexed, lists can have items with the same value
* `List Length:` To determine how many items a list has, use the len() function
* `List Items - Data Types:` List items can be of any data type.
* `type():`From Python's perspective, lists are defined as objects with the data type 'list'
* `The list() Constructor:` It is also possible to use the list() constructor when creating a new list.
* `Python Collections (Arrays):` There are four collection data types in the Python programming language:

* **List** is a collection which is ordered and changeable. Allows duplicate members.
* **Tuple** is a collection which is ordered and unchangeable. Allows duplicate members.
* **Set** is a collection which is unordered, unchangeable*, and unindexed. No duplicate members.
* **Dictionary** is a collection which is ordered** and changeable. No duplicate members.

* `Access List Items:` List items are indexed and you can access them by referring to the index number
* `Negative Indexing:` Negative indexing means start from the end -1 refers to the last item, -2 refers to the second last item etc.
* `Range of Indexes:` You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new list with the specified items.
* `Range of Negative Indexes:` Specify negative indexes if you want to start the search from the end of the list
* `Check if Item Exists:` To determine if a specified item is present in a list use the in keyword.
* `Change List Items:` To change the value of a specific item, refer to the index number.
* `Change a Range of Item Values:`To change the value of items within a specific range, define a list with the new values, and refer to the range of index numbers where you want to insert the new values.If you insert more items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly. If you insert less items than you replace, the new items will be inserted where you specified, and the remaining items will move accordingly:
* `Insert Items:` To insert a new list item, without replacing any of the existing values, we can use the insert() method. The insert() method inserts an item at the specified index.
* `Add List Items:` To add an item to the end of the list, use the append() method
* `Insert Items:` To insert a list item at a specified index, use the insert() method. The insert() method inserts an item at the specified index.
* `Extend List:` To append elements from another list to the current list, use the extend() method.
* `Add Any Iterable:` The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries etc.).
* `Remove List Items:` The remove() method removes the specified item. If there are more than one item with the specified value, the remove() method removes the first occurance.
* `Remove Specified Index:` The pop() method removes the specified index. If you do not specify the index, the pop() method removes the last item. The del keyword also removes the specified index The del keyword can also delete the list completely.
* `Clear the List:` The clear() method empties the list. The list still remains, but it has no content.
* `Loop Lists:` You can loop through the list items by using a for loop.
* `Loop Through the Index Numbers:` You can also loop through the list items by referring to their index number.Use the range() and len() functions to create a suitable iterable.
* `Using a While Loop:` You can loop through the list items by using a while loop. Use the len() function to determine the length of the list, then start at 0 and loop your way through the list items by referring to their indexes. Remember to increase the index by 1 after each iteration.
* `Looping Using List Comprehension:` List Comprehension offers the shortest syntax for looping through lists
* `List comprehension:` List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.
Example: Based on a list of fruits, you want a new list, containing only the fruits with the letter "a" in the name. Without list comprehension you will have to write a for statement with a conditional test inside. With list comprehension you can do all that with only one line of code.
* `Sort List Alphanumerically:` List objects have a sort() method that will sort the list alphanumerically, ascending, by default.
* `Sort Descending:` To sort descending, use the keyword argument reverse = True
* `Customize Sort Function:` You can also customize your own function by using the keyword argument key = function. The function will return a number that will be used to sort the list (the lowest number first)
* `Case Insensitive Sort:` By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters
* `Reverse Order:` The reverse() method reverses the current sorting order of the elements.
* `Copy Lists:` You cannot copy a list simply by typing list2 = list1, because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2. There are ways to make a copy, one way is to use the built-in List method copy(). Another way to make a copy is to use the built-in method list().\
* `Join Lists:` There are several ways to join, or concatenate, two or more lists in Python. One of the easiest ways are by using the + operator. Another way to join two lists is by appending all the items from list2 into list1, one by one Or you can use the extend() method, where the purpose is to add elements from one list to another list. 
* `List Methods:`Python has a set of built-in methods that you can use on lists.

| Method      | Description                                                      |
|-------------|------------------------------------------------------------------|
| append()    | Adds an element at the end of the list                           |
| clear()     | Removes all the elements from the list                           |
| copy()      | Returns a copy of the list                                       |
| count()     | Returns the number of elements with the specified value          |
| extend()    | Add the elements of a list (or any iterable), to the end of the current list |
| index()     | Returns the index of the first element with the specified value  |
| insert()    | Adds an element at the specified position                        |
| pop()       | Removes the element at the specified position                   |
| remove()    | Removes the item with the specified value                        |
| reverse()   | Reverses the order of the list                                   |
| sort()      | Sorts the list                                                   |

**Python Tuples**

Tuples are used to store multiple items in a single variable. Tuple is one of 4 built-in data types in Python used to store collections of data, the other 3 are List, Set, and Dictionary, all with different qualities and usage. A tuple is a collection which is ordered and unchangeable. Tuples are written with round brackets.  

* `Tuple Items:` Tuple items are ordered, unchangeable, and allow duplicate values. Tuple items are indexed, the first item has index [0], the second item has index [1] etc.
* `Ordered:` When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.
* `Unchangeable:` Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.
* `Allow Duplicates:` Since tuples are indexed, they can have items with the same value
* `Create Tuple With One Item:` To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
* `Access Tuple Items:` You can access tuple items by referring to the index number, inside square brackets
* `Negative Indexing:` Negative indexing means start from the end. -1 refers to the last item, -2 refers to the second last item etc.
* `Range of Indexes:` You can specify a range of indexes by specifying where to start and where to end the range. When specifying a range, the return value will be a new tuple with the specified items.
* `Range of Negative Indexes:` Specify negative indexes if you want to start the search from the end of the tuple
* `Check if Item Exists:` To determine if a specified item is present in a tuple use the in keyword
* `Update Tuples:` Tuples are unchangeable, meaning that you cannot change, add, or remove items once the tuple is created. But there are some workarounds. 
* `Change Tuple Values:` Once a tuple is created, you cannot change its values. Tuples are unchangeable, or immutable as it also is called. But there is a workaround. You can convert the tuple into a list, change the list, and convert the list back into a tuple.
* `Add Items:` Since tuples are immutable, they do not have a built-in append() method, but there are other ways to add items to a tuple.
1. Convert into a list: Just like the workaround for changing a tuple, you can convert it into a list, add your item(s), and convert it back into a tuple.
2. Add tuple to a tuple. You are allowed to add tuples to tuples, so if you want to add one item, (or many), create a new tuple with the item(s), and add it to the existing tuple
* `Remove Items:` Tuples are unchangeable, so you cannot remove items from it, but you can use the same workaround as we used for changing and adding tuple items.
* `Unpack Tuples:` When we create a tuple, we normally assign values to it. This is called "packing" a tuple But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
* `Using Asterisk`*``: If the number of variables is less than the number of values, you can add an * to the variable name and the values will be assigned to the variable as a list If the asterisk is added to another variable name than the last, Python will assign values to the variable until the number of values left matches the number of variables left.

**Python Set**

Sets are used to store multiple items in a single variable. A set is a collection which is unordered, unchangeable*, unindexed, and No duplicate values are allowed. Set is decleared using `{}`.

* `Accessing set items:` You cannot access items in a set by referring to an index or a key. But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.

*  `Add items to the set:` Once a set is created, you cannot change its items, but you can add new items. To add one item to a set use the `add() method`. To add items from another set into the current set, use the `update() method`.

* `Remove set items:` To remove an item in a set, use the remove(), or the discard() method. You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed. The return value of the pop() method is the removed item.

* `Loop Set:`You can loop through the set items by using a for loop.
* `Join Set:` There are several ways to join two or more sets in Python. You can use the union() method that returns a new set containing all items from both sets, or the update() method that inserts all the items from one set into another. The `intersection() method` will return a new set, that only contains the items that are present in both sets.
*  `Set Methods:` Python has a set of built-in methods that you can use on sets.


| Method                      | Description                                                 |
| --------------------------- | ----------------------------------------------------------- |
| `add()`                     | Adds an element to the set                                  |
| `clear()`                   | Removes all the elements from the set                       |
| `copy()`                    | Returns a copy of the set                                   |
| `difference()`              | Returns a set containing the difference between two or more sets |
| `difference_update()`       | Removes the items in this set that are also included in another, specified set |
| `discard()`                 | Remove the specified item                                  |
| `intersection()`            | Returns a set that is the intersection of two other sets   |
| `intersection_update()`     | Removes the items in this set that are not present in other, specified set(s) |
| `isdisjoint()`              | Returns whether two sets have an intersection or not       |
| `issubset()`                | Returns whether another set contains this set or not       |
| `issuperset()`              | Returns whether this set contains another set or not       |
| `pop()`                     | Removes an element from the set                            |
| `remove()`                  | Removes the specified element                              |
| `symmetric_difference()`    | Returns a set with the symmetric differences of two sets   |
| `symmetric_difference_update()` | Inserts the symmetric differences from this set and another |
| `union()`                   | Returns a set containing the union of sets                 |
| `update()`                  | Update the set with the union of this set and others       |


**Python Dictionaries**
Dictionaries are used to store data values in `key:value pairs`. A dictionary is a collection which is ordered*, changeable and do not allow duplicates. Dictionaries are written with curly brackets, and have keys and values

* `Dictionary Items:` Dictionary items are ordered, changeable, and does not allow duplicates. Dictionary items are presented in key:value pairs, and can be referred to by using the key name.

`When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change. Unordered means that the items does not have a defined order, you cannot refer to an item by using an index.` 

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.

* `Accessing Dictionary Items:` You can access the items of a dictionary by referring to its key name, inside square brackets. There is also a method called `get()` that will give you the same result. The `keys()` method will return a list of all the keys in the dictionary. The list of the keys is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the keys list.
* `Get Values:` The `values()` method will return a list of all the values in the dictionary. The list of the values is a view of the dictionary, meaning that any changes done to the dictionary will be reflected in the values list.
* `Get Items:` The items() method will return each item in a dictionary, as tuples in a list. The returned list is a view of the items of the dictionary, meaning that any changes done to the dictionary will be reflected in the items list.
* `Change Dictionary Items:` You can change the value of a specific item by referring to its key name
* `Update Dictionary:` The update() method will update the dictionary with the items from the given argument.
* `Add Dictionary Items:` Adding an item to the dictionary is done by using a new index key and assigning a value to it.
* `Update Dictionary:` The update() method will update the dictionary with the items from a given argument. If the item does not exist, the item will be added.
* `Remove items:`There are several methods to remove items from a dictionary.
* `Loop Through Dictionary:` You can loop through a dictionary by using a for loop. When looping through a dictionary, the return value are the keys of the dictionary, but there are methods to return the values as well.
* `Copy Dictionaries:` You cannot copy a dictionary simply by typing dict2 = dict1, because: dict2 will only be a reference to dict1, and changes made in dict1 will automatically also be made in dict2. There are ways to make a copy, one way is to use the built-in Dictionary method copy().
* `Nested Dictionaries:` A dictionary can contain dictionaries, this is called nested dictionaries.
* `Accessing items in Nested Dictionaries`: To access items from a nested dictionary, you use the name of the dictionaries, starting with the outer dictionary

* `Dictionary Methods:` Python has a set of built-in methods that you can use on dictionaries.

| Method       | Description                                               |
| ------------ | --------------------------------------------------------- |
| `clear()`    | Removes all the elements from the dictionary             |
| `copy()`     | Returns a copy of the dictionary                          |
| `fromkeys()` | Returns a dictionary with the specified keys and value   |
| `get()`      | Returns the value of the specified key                    |
| `items()`    | Returns a list containing a tuple for each key value pair |
| `keys()`     | Returns a list containing the dictionary's keys           |
| `pop()`      | Removes the element with the specified key                |
| `popitem()`  | Removes the last inserted key-value pair                  |
| `setdefault()` | Returns the value of the specified key. If the key does not exist: insert the key, with the specified value |
| `update()`   | Updates the dictionary with the specified key-value pairs |
| `values()`   | Returns a list of all the values in the dictionary        |


**Python IF-ELSE Conditions:**
Python supports the usual logical conditions from mathematics:

| Comparison Type            | Syntax    |
|---------------------------|-----------|
| Equals                    | `a == b`  |
| Not Equals                | `a != b`  |
| Less than                 | `a < b`   |
| Less than or equal to    | `a <= b`  |
| Greater than              | `a > b`   |
| Greater than or equal to | `a >= b`  |


These conditions can be used in several ways, most commonly in "if statements" and loops. An "if statement" is written by using the `if keyword`.

* `Elif:` The elif keyword is Python's way of saying "if the previous conditions were not true, then try this condition".
* `Else:` The else keyword catches anything which isn't caught by the preceding conditions.
* `And`: The and keyword is a logical operator, and is used to combine conditional statements
* `OR:` The or keyword is a logical operator, and is used to combine conditional statements
* `Not:` The not keyword is a logical operator, and is used to reverse the result of the conditional statement
* `Nested If:` You can have if statements inside if statements, this is called nested if statements.
* `The pass Statement:` if statements cannot be empty, but if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error.

**Python Loop**
Python has two primitive loop commands:
* `While Loop:` With the while loop we can execute a set of statements as long as a condition is true.
* `For loop:` A for loop is used for iterating over a sequence (that is either a list, a tuple, a dictionary, a set, or a string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages. With the for loop we can execute a set of statements, once for each item in a list, tuple, set etc.
* `Break:` With the break statement we can stop the loop even if the while condition is true
* `Continue:` With the continue statement we can stop the current iteration, and continue with the next
* `else statements:` With the else statement we can run a block of code once when the condition no longer is true
* `For Looping through the string:` Even strings are iterable objects, they contain a sequence of characters
* `Range:` To loop through a set of code a specified number of times, we can use the range() function, The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and ends at a specified number. The range() function defaults to 0 as a starting value, however it is possible to specify the starting value by adding a parameter: range(2, 6), which means values from 2 to 6 (but not including 6), The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
* else: The else keyword in a for loop specifies a block of code to be executed when the loop is finished
* `Nested Loop:` A nested loop is a loop inside a loop. The "inner loop" will be executed one time for each iteration of the "outer loop"

**Python Functions**

A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.

* `Creating a Function:` In Python a function is defined using the `def keyword`
* `Calling a function:` To call a function, use the function name followed by parenthesis
* `Arguments:` Information can be passed into functions as arguments. Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.
* `Arbitrary Arguments, *args:` If you do not know how many arguments that will be passed into your function, add a * before the parameter name in the function definition. This way the function will receive a tuple of arguments, and can access the items accordingly.
* `Keyword Arguments:` You can also send arguments with the key = value syntax. This way the order of the arguments does not matter.
* `Arbitrary Keyword Arguments, **kwargs:` If you do not know how many keyword arguments that will be passed into your function, add two asterisk: ** before the parameter name in the function definition.
* `Default Parameter Value:` The following example shows how to use a default parameter value.
*  `Passing a List as an Argument:` You can send any data types of argument to a function (string, number, list, dictionary etc.), and it will be treated as the same data type inside the function.
* `Return Value:` To let a function return a value, use the return statement
* `Pass statements:` function definitions cannot be empty, but if you for some reason have a function definition with no content, put in the pass statement to avoid getting an error.
* `Recursion:` Python also accepts function recursion, which means a defined function can call itself. Recursion is a common mathematical and programming concept. It means that a function calls itself. This has the benefit of meaning that you can loop through data to reach a result. The developer should be very careful with recursion as it can be quite easy to slip into writing a function which never terminates, or one that uses excess amounts of memory or processor power. However, when written correctly recursion can be a very efficient and mathematically-elegant approach to programming. In this example, tri_recursion() is a function that we have defined to call itself ("recurse"). We use the k variable as the data, which decrements (-1) every time we recurse. The recursion ends when the condition is not greater than 0 (i.e. when it is 0). To a new developer it can take some time to work out how exactly this works, best way to find out is by testing and modifying it.

**Python Lambda**

A lambda function is a small anonymous function. A lambda function can take any number of arguments, but can only have one expression.

`Why Use Lambda Functions?` --> The power of lambda is better shown when you use them as an anonymous function inside another function. Say you have a function definition that takes one argument, and that argument will be multiplied with an unknown number.




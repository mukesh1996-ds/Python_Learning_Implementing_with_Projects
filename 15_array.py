class MyList:
    def __init__(self):
        self.my_list = []

    def append(self, element):
        """
        Adds an element at the end of the list.
        """
        self.my_list.append(element)

    def clear(self):
        """
        Removes all the elements from the list.
        """
        self.my_list.clear()

    def copy(self):
        """
        Returns a copy of the list.
        """
        return self.my_list.copy()

    def count(self, value):
        """
        Returns the number of elements with the specified value.
        """
        return self.my_list.count(value)

    def extend(self, iterable):
        """
        Add the elements of a list (or any iterable), to the end of the current list.
        """
        self.my_list.extend(iterable)

    def index(self, value):
        """
        Returns the index of the first element with the specified value.
        """
        return self.my_list.index(value)

    def insert(self, index, element):
        """
        Adds an element at the specified position.
        """
        self.my_list.insert(index, element)

    def pop(self, index=-1):
        """
        Removes the element at the specified position (default: last element).
        """
        return self.my_list.pop(index)

    def remove(self, value):
        """
        Removes the first item with the specified value.
        """
        self.my_list.remove(value)

    def reverse(self):
        """
        Reverses the order of the list.
        """
        self.my_list.reverse()

    def sort(self):
        """
        Sorts the list.
        """
        self.my_list.sort()

# Example usage:
if __name__ == "__main__":
    my_list = MyList()
    my_list.append(1)
    my_list.append(2)
    my_list.append(3)

    print("Original List:", my_list.my_list)

    my_list.reverse()
    print("Reversed List:", my_list.my_list)

    my_list.sort()
    print("Sorted List:", my_list.my_list)

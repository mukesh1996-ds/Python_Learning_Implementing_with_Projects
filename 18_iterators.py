class MyRange:
    def __init__(self, start, end, step=1):
        self.start = start
        self.end = end
        self.step = step
        self.current = start

    def __iter__(self):
        return self

    def __next__(self):
        if (self.step > 0 and self.current >= self.end) or (self.step < 0 and self.current <= self.end):
            raise StopIteration
        else:
            result = self.current
            self.current += self.step
            return result

# Create an instance of the custom range class
my_range = MyRange(1, 10, 2)

# Iterate over the range using the iterator
for num in my_range:
    print(num)

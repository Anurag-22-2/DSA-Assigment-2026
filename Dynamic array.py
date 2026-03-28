class DynamicArray:
    def __init__(self):
        self.capacity = 1
        self.size = 0
        self.array = [None] * self.capacity

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity)
        self.array[self.size] = value
        self.size += 1

    def pop(self):
        if self.size == 0:
            raise IndexError("Pop from empty array")
        value = self.array[self.size - 1]
        self.array[self.size - 1] = None
        self.size -= 1
        return value

    def _resize(self, new_capacity):
        new_array = [None] * new_capacity
        for i in range(self.size):
            new_array[i] = self.array[i]
        self.array = new_array
        self.capacity = new_capacity

    def __str__(self):
        return str([self.array[i] for i in range(self.size)])



dyn = DynamicArray()
dyn.append(10)
dyn.append(20)
dyn.append(30)
print("Array after appends:", dyn)
dyn.pop()
print("Array after pop:", dyn)







#  Parentheses 


def check_parentheses(expr):
    stack = []
    for ch in expr:
        if ch in "([{":
            stack.append(ch)
        elif ch in ")]}":
            if not stack:
                return False
            top = stack.pop()
            if (top == "(" and ch != ")") or \
               (top == "[" and ch != "]") or \
               (top == "{" and ch != "}"):
                return False
    return len(stack) == 0



print(check_parentheses("(a+b) * [c-d]"))   # True
print(check_parentheses("(a+b]"))           # False

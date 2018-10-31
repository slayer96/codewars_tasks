"""

Story
You were supposed to implement a node-based calculator. Hopefully for you, a colleague agreed to do the task. When the
management saw the code, they were infuriated with its low quality, and as a punishment told you to shorten it as much
as possible...

Task
You will be given a ready solution passing all the fixed and random tests. Unfortunately for you, it is very long and
overly repetitive. Current code length is 901 characters. Your task is to shorten it to at most 300 characters.

Note/hint: you can modify the implementation any way you want, as long as it is written using only OOP; the sample
tests check solution's functionality the same way as the final tests do - if your solution passes the former,
it will also pass the latter.


class Node:
    def __init__(self, *values):
        self.values = values

class value(Node):
    def compute(self):
        return self.values[0]

class add(Node):
    def compute(self):
        return value(self.values[0].compute() + self.values[1].compute()).compute()

class sub(Node):
    def compute(self):
        return value(self.values[0].compute() - self.values[1].compute()).compute()

class mul(Node):
    def compute(self):
        return value(self.values[0].compute() * self.values[1].compute()).compute()

class truediv(Node):
    def compute(self):
        return value(self.values[0].compute() / self.values[1].compute()).compute()

class mod(Node):
    def compute(self):
        return value(self.values[0].compute() % self.values[1].compute()).compute()

class pow(Node):
    def compute(self):
        return value(self.values[0].compute() ** self.values[1].compute()).compute()


"""


class Node:
    def __init__(self, *values):
        self.values = values

    def compute(self):
        class_name = self.__class__.__name__
        if class_name == 'add':
            return self.values[0].compute() + self.values[1].compute()


class value(Node):
    def compute(self):
        return self.values[0]


class add(Node):
    pass


class sub(Node):
    def compute(self):
        return value(self.values[0].compute() - self.values[1].compute()).compute()


class mul(Node):
    def compute(self):
        return value(self.values[0].compute() * self.values[1].compute()).compute()


class truediv(Node):
    def compute(self):
        return value(self.values[0].compute() / self.values[1].compute()).compute()


class mod(Node):
    def compute(self):
        return value(self.values[0].compute() % self.values[1].compute()).compute()


class pow(Node):
    def compute(self):
        return value(self.values[0].compute() ** self.values[1].compute()).compute()


a, b = value(5), value(2)

assert add(a, b).compute() == 7
assert sub(a, b).compute() == 3
assert mul(a, b).compute() == 10
assert truediv(a, b).compute() == 2.5
assert mod(a, b).compute() == 1
assert pow(a, b).compute() == 25

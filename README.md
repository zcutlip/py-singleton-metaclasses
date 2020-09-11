# Python Singleton Metaclasses

## Description

A package of python metclasses for implementing singleton and related patterns.

### Singleton Class

This implements the traditional singleton pattern. Once an instance of a class is created, all future instantiations result in the same object.

### Memoized Class

This applies the notion of "memoization" to object creation. Multiple calls to a constructor with the same first parameter result in the same object.

Calls to the constructor with a new first parameter result in a new object instance.

This is useful in situations where a singleton is called for if the arguments are the same, but a new instance is called for when new arguments are provided.

For example, if an object parses a file, there may be no need to parse the same file more than once. So all instantiations of the parser on the same file result in the same object instance. But for a new file that has yet to be parsed, a new instance will be created.

## Examples

---

### Singleton Class Example

```python
from pysingleton import PySingleton  # noqa: E402


class MySingleton(metaclass=PySingleton):
    def __init__(self, value):
        self.value = value


# Create first instance and inspect value
my_singleton_1 = MySingleton(1)
print("my_singleton_1.value: {}".format(my_singleton_1.value))

# Create second instance with new constructor param
my_singleton_2 = MySingleton(2)
# Inspect value and see it matches the original
print("my_singleton_2.value: {}".format(my_singleton_2.value))

# First and second instances' values are equal
print("my_singleton_1.value == my_singleton_2.value: {}".format(
    my_singleton_1.value == my_singleton_2.value))

# change second instance's value
my_singleton_2.value = 7

# Inspect first instance's value and see it has changed
print("my_singleton_1.value: {}".format(my_singleton_1.value))

# First and second instance have the same object ID:
print("id(my_singleton_1): {:#x}".format(id(my_singleton_1)))
print("id(my_singleton_2): {:#x}".format(id(my_singleton_2)))
```

```console
$ python ./example.py
my_singleton_1.value: 1
my_singleton_2.value: 1
my_singleton_1.value == my_singleton_2.value: True
my_singleton_1.value: 7
id(my_singleton_1): 0x101c29b80
id(my_singleton_2): 0x101c29b80
```

---

### Memoized Class Example

```python
from pysingleton import PyMemoized  # noqa: E402


class MyMemoized(metaclass=PyMemoized):
    def __init__(self, param1, param2):
        self.value = param2


# Create first instance and inspect value
my_memoized_1 = MyMemoized("arg1", 1)
print("my_memoized_1.value: {}".format(my_memoized_1.value))

# Create second instance with the original param1 but new param2
my_memoized_2 = MyMemoized("arg1", 2)
# Inspect value and see it matches the original
print("my_memoized_2.value: {}".format(my_memoized_2.value))

# First and second instances' values are equal
print("my_memoized_1.value == my_memoized_2.value: {}".format(
    my_memoized_1.value == my_memoized_2.value))

# change second instance's value
my_memoized_2.value = 7

# Inspect first instance's value and see it has changed
print("my_memoized_1.value: {}".format(my_memoized_1.value))

# Create third instance with new param1 & param2, and see
# it takes the new value
my_memoized_3 = MyMemoized("arg3", 3)
print("my_memoized_3.value: {}".format(my_memoized_3.value))

# First and third  instances' values are not equal
print("my_memoized_1.value == my_memoized_3.value: {}".format(
    my_memoized_1.value == my_memoized_3.value))


# First and second instance have the same object ID
print("id(my_memoized_1): {:#x}".format(id(my_memoized_1)))
print("id(my_memoized_2): {:#x}".format(id(my_memoized_2)))

# but third instance's object ID is different
print("id(my_memoized_3): {:#x}".format(id(my_memoized_3)))

```

```console
python3 ./examples/memoized-example.py
my_memoized_1.value: 1
my_memoized_2.value: 1
my_memoized_1.value == my_memoized_2.value: True
my_memoized_1.value: 7
my_memoized_3.value: 3
my_memoized_1.value == my_memoized_3.value: False
id(my_memoized_1): 0x100773b80
id(my_memoized_2): 0x100773b80
id(my_memoized_3): 0x100818340
```

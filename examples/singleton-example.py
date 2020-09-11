import os
import sys
parent_path = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
if parent_path not in sys.path:
    sys.path.append(parent_path)

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

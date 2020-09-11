import os
import sys
parent_path = os.path.dirname(
    os.path.dirname(
        os.path.abspath(__file__)
    )
)
if parent_path not in sys.path:
    sys.path.append(parent_path)

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

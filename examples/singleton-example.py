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
    # Set to True to allow the singleton instance
    # to be deleted when it goes out of scope
    # _PYSINGLETON_WEAKREF = True

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

ms_id_1 = id(my_singleton_1)

# Delete current instances before creating a new one
my_singleton_1 = my_singleton_2 = None

# If MySingleton._PYSINGLETON_WEAKREF is set to True
# or if MySingleton_WEAKREF environment variable is set to 1
# the singleton will be destroyed, and my_singleton_3 will create a new instance
my_singleton_3 = MySingleton(1)

print(f"id(my_singleton_3): {id(my_singleton_3):#x}")
print(f"my_singleton_1 == my_singleton_3 {ms_id_1 == id(my_singleton_3)}")

import os

from weakref import WeakValueDictionary


class PySingleton(type):
    _instances = None

    def __call__(cls, *args, **kwargs):
        if not cls._instances:
            cls._initialize()
        instance = cls._instances.get(cls)
        if not instance:
            instance = super(
                PySingleton, cls
            ).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return instance

    def _initialize(cls):
        use_weakref = getattr(cls, "_PYSINGLETON_WEAKREF", None)
        env_var = f"{cls.__name__}_WEAKREF"
        if use_weakref is None:
            use_weakref = os.getenv(env_var)
            print(env_var)
            print(f"use_weakref: {use_weakref}")
            use_weakref = True if use_weakref == "1" else False
        if use_weakref:
            cls._instances = WeakValueDictionary()
        else:
            cls._instances = {}


class PyMemoized(type):
    _instances = None

    def __call__(cls, memoized_key, *args, **kwargs):
        if not cls._instances:
            cls._initialize()
        instance = cls._instances.get((cls, memoized_key))

        if instance is None:
            instance = super().__call__(memoized_key, *args, **kwargs)
            cls._instances[(cls, memoized_key)] = instance
        return instance

    def _initialize(cls):
        use_weakref = getattr(cls, "_PYMEMOIZED_WEAKREF", None)
        env_var = f"{cls.__name__}_WEAKREF"
        if use_weakref is None:
            use_weakref = os.getenv(env_var)
            print(env_var)
            print(f"use_weakref: {use_weakref}")
            use_weakref = True if use_weakref == "1" else False
        if use_weakref:
            cls._instances = WeakValueDictionary()
        else:
            cls._instances = {}

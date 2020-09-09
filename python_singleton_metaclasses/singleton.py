class PySingleton(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance = cls._instances.get(cls)
        if not instance:
            instance = super(
                PySingleton, cls
            ).__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return instance


class PyMemoized(type):
    _instances = {}

    def __call__(cls, memoized_key, *args, **kwargs):
        instance = cls._instances.get((cls, memoized_key))

        if instance is None:
            instance = super().__call__(memoized_key, *args, **kwargs)
            cls._instances[(cls, memoized_key)] = instance
        return instance

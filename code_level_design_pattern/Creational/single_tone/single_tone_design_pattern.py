"""
Class()
   ↓
__new__()
   ↓
object created
   ↓
__init__()
   ↓
object initialized
"""
from typing import Self

"""
# Simple
class ConfigManager:

    _instance = None

    def __new__(cls):

        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        print("Initializing")

config_1 = ConfigManager()
config_2 = ConfigManager()

print(config_1 is config_2)
"""

# Better
class ConfigManager:
    _instance = None
    _initialized = False

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        print("Initializing Manager")

        self.environment = 'production'

        self._initialized = True


config_1 = ConfigManager()
config_2 = ConfigManager()
config_3 = ConfigManager()

print(config_1 is config_2)
print(config_2 is config_3)
print(config_3 is config_1)


"""
#Singleton using a class method

class Singleton:

    _instance = None

    @classmethod
    def get_instance(cls):

        if cls._instance is None:
            cls._instance = cls()

        return cls._instance

obj1 = Singleton.get_instance()
obj2 = Singleton.get_instance()

print(obj1 is obj2)

"""

"""
# Singleton using a metaclass

class SingletonMeta(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):

        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(
                *args,
                **kwargs
            )

        return cls._instances[cls]

class DatabaseManager(metaclass=SingletonMeta):
    pass
    
db1 = DatabaseManager()
db2 = DatabaseManager()

print(db1 is db2)

"""
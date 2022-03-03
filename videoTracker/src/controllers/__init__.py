import sys
sys.path.append(__file__.replace("\\","/").replace("__init__.py",""))

if __name__ == '__main__':
    from masterController import MasterController

elif __name__ == "controllers":
    from .masterController import MasterController

else:
    raise ImportError(f"unexpected __name__, got:{__name__}")

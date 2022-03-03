import sys
sys.path.append(__file__.replace("\\", "/").replace("__init__.py", ""))

if __name__ == '__main__':
    from mainWindow import MasterView

elif __name__ == "views":
    from .mainWindow import MasterView

else:
    raise ImportError(f"unexpected __name__, got:{__name__}")

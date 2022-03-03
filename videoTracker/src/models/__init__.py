import sys
sys.path.append(__file__.replace("\\", "/").replace("__init__.py", ""))

if __name__ == '__main__':
    from applicationController import ControllerModel
    from fileRepo import FileRepo
    from liste import Liste, Cell
    from point import Point

elif __name__ == "models":
    from .applicationController import ControllerModel
    from .fileRepo import FileRepo
    from .liste import Liste, Cell
    from .point import Point

else:
    raise ImportError(f"unexpected __name__, got:{__name__}")



import unittest
import sys

if '\\' in __file__:
    sys.path.append("\\".join(__file__.split('\\')[:-2])+"\\")
elif '/' in __file__:
    sys.path.append("/".join(__file__.split('/')[:-2])+"/")
else:
    raise EnvironmentError(
        f"their is neither '/' or '\\' in the __file__ const:{__file__}")


from liste import Liste, Cell


class Test_liste(unittest.TestCase):

    def setUp(self) -> None:
        self.__liste = Liste()
        self.__first = Cell("first")
        self.__second = Cell("second")
        self.__third = Cell("third")

    def tearDown(self):
        pass

    def test_isEmpty(self):
        self.assertTrue(self.__liste.isEmpty())

    def test_addFirstWithEmptyList(self):
        self.__liste.addFirst(self.__first)
        self.assertTrue(self.__liste.getFirst() is self.__first)

    def test_addLastWithEmptyList(self):
        self.__liste.addLast(self.__second)
        self.assertTrue(self.__liste.getFirst() is self.__second)

    def test_addFirst(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addFirst(self.__third)
        self.assertTrue(self.__liste.getFirst() is self.__third)
        self.assertTrue(self.__liste.getLast() is self.__first)

    def test_addLast(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addLast(self.__third)
        self.assertTrue(self.__liste.getFirst() is self.__second)
        self.assertTrue(self.__liste.getLast() is self.__third)

    def test_insertionOrder(self):
        self.__liste.addFirst(self.__first)
        self.assertEqual(self.__liste.getFirst(), self.__first)
        self.assertEqual(self.__liste.getLast(), self.__first)
        self.__liste.addFirst(self.__second)
        self.assertEqual(self.__liste.getFirst(), self.__second)
        self.assertEqual(self.__liste.getLast(), self.__first)
        self.__liste.addFirst(self.__third)
        self.assertEqual(self.__liste.getFirst(), self.__third)
        self.assertEqual(self.__liste.getLast(), self.__first)

    def test_str(self):
        self.__liste.addFirst(self.__first)
        self.__liste.addFirst(self.__second)
        self.__liste.addFirst(self.__third)
        self.assertEqual(str(self.__liste), "third -> second -> first -> ")


if __name__ == '__main__':
    unittest.main(verbosity=2)

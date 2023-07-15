import unittest
from models.base import Base
"""unittest for Base class"""


class TestBase(unittest.TestCase):
    """define a TestBase class"""
    def test_init_with_id(self):
        """init with id"""
        base = Base(id=12)
        self.assertEqual(base.id, 12)

    def test_init_without_id(self):
        """init without id"""
        base = Base()
        self.assertEqual(Base.nb_objects(), base.id)

    def test_nb_objects(self):
        """value of nb objects variable"""
        base1 = Base()
        base2 = Base()
        self.assertEqual(Base.nb_objects(), 3)

    def test_invalid_id(self):
        """invalid id"""
        with self.assertRaises(ValueError):
            Base(id=Base.nb_objects())

        with self.assertRaises(ValueError):
            Base(id=Base.nb_objects() - 1)


if __name__ == "__main__":
    unittest.main()

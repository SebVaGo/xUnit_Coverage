import unittest
from main.sorter import sort_numbers

class TestSortNumbers(unittest.TestCase):

    def test_sorted_list(self):
        """Caso de prueba: lista ya ordenada"""
        self.assertEqual(sort_numbers([1, 2, 3]), [1, 2, 3])

    def test_unsorted_list(self):
        """Caso de prueba: lista desordenada"""
        self.assertEqual(sort_numbers([3, 1, 2]), [1, 2, 3])

    def test_with_negative_numbers(self):
        """Caso de prueba: lista con números negativos"""
        self.assertEqual(sort_numbers([-1, -3, 0, 2]), [-3, -1, 0, 2])

    def test_invalid_input(self):
        """Caso de prueba: lista con elementos no enteros"""
        with self.assertRaises(ValueError):
            sort_numbers([1, "a", 3])

if __name__ == "__main__":
    unittest.main()

import unittest
from typing import Any, Dict

def count_occurrences(iterable: Any) -> Dict[Any, int]:
    element_count = {}
    for element in iterable:
        if element in element_count:
            element_count[element] += 1
        else:
            element_count[element] = 1
    return element_count

 
class TestCountOccurrences(unittest.TestCase):

    def test_string_input(self):
        self.assertEqual(count_occurrences("hello"), {'h': 1,'e': 1,'l': 2,'o':1})

    def test_list_of_integers(self):
        self.assertEqual(count_occurrences([1, 2, 2, 3, 1, 1]), {1: 3, 2: 2, 3: 1})

    def test_tuple_input(self):
        self.assertEqual(count_occurrences(('hello', 'hai', 'hello', 'welcome')),
                         {'hello': 2, 'hai': 1, 'welcome': 1})

    def test_set_input(self):
        self.assertEqual(count_occurrences({50, 10, 50, 10, 20}), {50: 1, 10: 1, 20: 1})

    def test_mixed_list_input(self):
        self.assertEqual(count_occurrences([1, 'a', 'a', 2, 1, 'b', 2]), {1: 2, 'a': 2, 2: 2, 'b': 1})

    def test_empty_input(self):
        self.assertEqual(count_occurrences([]), {})

    def test_single_element_list(self):
        self.assertEqual(count_occurrences([10]), {10: 1})

    def test_none_type_input(self):
        with self.assertRaises(TypeError):
            count_occurrences(None)

if __name__ == "__main__":
    unittest.main()

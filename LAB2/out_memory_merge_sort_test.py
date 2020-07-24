import unittest
from out_memory_merge_sort import merge_sort
from out_memory_merge_sort import create

class TestMergeSort(unittest.TestCase):

    def is_sorted(self):
        merge_sort('numbers.txt')
        lst = []
        with open('numbers.txt') as f:
            for line in f:
                lst.append(int(line))
        self.assertTrue(all(b >= a for a, b in zip(lst, lst[1:])))

    def test_for_10_from_minus_20_to_20(self):
        create('numbers.txt', 10, 20)
        self.is_sorted()

    def test_for_100_from_minus_50_to_50(self):
        create('numbers.txt', 100, 50)
        self.is_sorted()

    def test_for_500_from_minus_100_to_100(self):
        create('numbers.txt', 500, 100)
        self.is_sorted()

if __name__ == '__main__':
    unittest.main()

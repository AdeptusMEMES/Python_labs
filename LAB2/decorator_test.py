import unittest
import decorator


class TestDecorator(unittest.TestCase):

    def test_different_args_same_res(self):
        control_lst = []
        sum1 = decorator.tuple_sum((2, 1, 3), control_lst)
        control_lst = []
        sum2 = decorator.tuple_sum((1, 3, 2), control_lst)
        self.assertTrue(control_lst and sum1 == sum2 and sum1 == 6)

    def test_different_args_different_res(self):
        control_lst = []
        sum1 = decorator.tuple_sum((4, 5), control_lst)
        control_lst = []
        sum2 = decorator.tuple_sum((1, 10, 3, 5), control_lst)
        self.assertTrue(control_lst and sum1 == 9 and sum2 == 19)

    def test_same_args_same_res(self):
        control_lst = []
        sum1 = decorator.tuple_sum((7, 3, 9, 11), control_lst)
        control_lst = []
        sum2 = decorator.tuple_sum((7, 3, 9, 11), control_lst)
        self.assertTrue(not control_lst and sum1 == sum2 and sum1 == 30)


if __name__ == '__main__':
    unittest.main()

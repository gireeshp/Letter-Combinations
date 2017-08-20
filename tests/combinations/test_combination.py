import unittest
from combinations import combination as comb


class TestMoveToFirst(unittest.TestCase):

    def test_results(self):
        ret_val = comb.move_to_first('abcdef', 3)
        self.assertEqual(ret_val, 'dabcef')


class TestSwap(unittest.TestCase):

    def test_swap (self):
        ret_val = comb.swap('abcdef', 2, 4)
        self.assertEqual(ret_val, 'abedcf')


class TestCombFn (unittest.TestCase):

    def test_comb_fn (self):
        input_str = "abc"
        comb.comb_fn(input_str, 0, len(input_str)-1)

        expected_output_list = ['abc', 'acb', 'bca', 'bac', 'cab', 'cba']
        self.assertCountEqual(expected_output_list, comb.output_list)

if __name__ == '__main__':
    unittest.main()

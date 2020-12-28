import unittest

from day_18 import eval_expr


class TestDay18(unittest.TestCase):
    def test_eval_expr(self):
        self.assertEqual(eval_expr('1 + 2 * 3 + 4 * 5 + 6'), 71)

    def test_eval_expr_with_parentheses(self):
        self.assertEqual(eval_expr('1 + (2 * 3) + (4 * (5 + 6))'), 51)
        self.assertEqual(eval_expr('2 * 3 + (4 * 5)'), 26)
        self.assertEqual(eval_expr('5 + (8 * 3 + 9 + 3 * 4 * 3)'), 437)
        self.assertEqual(eval_expr('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'), 12_240)
        self.assertEqual(eval_expr('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'), 13_632)

    def test_eval_expr_add_before_mul(self):
        self.assertEqual(eval_expr('1 + 2 * 3 + 4 * 5 + 6', add_before_mul=True), 231)

    def test_eval_expr_with_parentheses_add_before_mul(self):
        self.assertEqual(eval_expr('1 + (2 * 3) + (4 * (5 + 6))', add_before_mul=True), 51)
        self.assertEqual(eval_expr('2 * 3 + (4 * 5)', add_before_mul=True), 46)
        self.assertEqual(eval_expr('5 + (8 * 3 + 9 + 3 * 4 * 3)', add_before_mul=True), 1_445)
        self.assertEqual(eval_expr('5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))', add_before_mul=True), 669_060)
        self.assertEqual(eval_expr('((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2', add_before_mul=True), 23_340)


if __name__ == '__main__':
    unittest.main()

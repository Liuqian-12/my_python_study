import unittest


class AssertTest(unittest.TestCase):
    def test_01(self):
        a = 1
        b = 2
        c = 1
        d = None
        e = [1, 2, 3, 4]
        f = 5
        sum1 = a + b
        self.assertEqual(3, sum1, "两数和为3")
        self.assertNotEqual(4, sum1, "两数之和不是3")
        self.assertIs(a, c, "a is b")
        self.assertIsNot(a, b, "a和b不相等")
        self.assertIsNone(d)
        self.assertIsNotNone(a)
        self.assertIn(a, e, "a in e")
        self.assertNotIn(f, e, "f not in e")

        # with self.assertRaises(Exception) as cm:
        #     do_something()

        # the_exception = cm.exception
        # self.assertEqual(the_exception.error_code, 3)

    
if __name__ == "__main__":
    unittest.main()
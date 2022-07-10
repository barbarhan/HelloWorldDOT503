from re import X
import unittest
import Hello_World


class Test(unittest.TestCase):


    def test_func(self):
        pass

    def test_name(self):
        pass
    def test_upper(self):
        self.assertEqual('foo'.upper(), 'FOo')

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'woorld'])

        with self.assertRaises(TypeError):
            s.split(2)

if __name__== "__main__":
    unittest.main()
import unittest
from zad1 import Operacje
import io
import sys


class Test_Decorator(unittest.TestCase):

    def setUp(self) -> None:
        global op
        op = Operacje()
        return super().setUp()

    def test_normal_sum(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        op.suma(1, 2, 3)                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), '1 + 2 + 3 = 6\n')
        self.assertEqual(op.suma(1, 2, 3), 4)

    def test_sum_with_less_args(self):
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        op.suma(1, 2)                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), '1 + 2 + 4 = 7\n')
        self.assertEqual(op.suma(1, 2), 5)

    def test_operation_error(self):
        with self.assertRaises(TypeError):
            op.suma()

    def test_change_sum(self):
        op['suma'] = [4, 2]
        capturedOutput = io.StringIO()                  # Create StringIO object
        sys.stdout = capturedOutput  # and redirect stdout.
        op.suma(3, 3)                                     # Call function.
        sys.stdout = sys.__stdout__                     # Reset redirect.
        self.assertEqual(capturedOutput.getvalue(), '3 + 3 + 4 = 10\n')


if __name__ == '__main__':
    unittest.main()


op = Operacje()
op.suma(1, 2, 3)  # Wypisze: 1+2+3=6
op.suma(1, 2)  # Wypisze: 1+2+4=7 - 4 jest pobierana z tablicy 'argumentySuma'
op.suma(1)  # Wypisze: 1+4+5=10 - 4 i 5 są pobierane z tablicy 'argumentySuma'
# op.suma()  # TypeError: suma() takes exactly 3 arguments (2 given)
op.roznica(2, 1)  # Wypisze: 2-1=1
op.roznica(2)  # Wypisze: 2-4=-2
wynik = op.roznica()  # Wypisze: 4-5=-1
print(wynik)  # Wypisze: 6

# Zmiana zawartości listy argumentów dekoratora  dla metody 'suma'
op['suma'] = [1, 2]
# oznacza, że   argumentySuma=[1,2]

# Zmiana zawartości listy argumentów dekoratora  dla metody 'roznica'
op['roznica'] = [1, 2, 3]
# oznacza, że   argumentyRoznica=[1,2,3]

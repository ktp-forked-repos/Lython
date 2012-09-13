import unittest
from unittest import TestCase

from lython_compiler import lython_compile

class CompileTests(TestCase):
    def test_assignment(self):
        program = "(= x 3)"
        compiled_program = "x = 3"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_if(self):
        program = "(if True (= x 1))"
        compiled_program = "if True:\n    x = 1"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_symbol(self):
        program = "(if True 1)"
        compiled_program = "if True:\n    1"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_function(self):
        program = "(def foo (x y) 1)"
        compiled_program = "def foo(x, y):\n    1"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_function_multi_statements(self):
        program = "(def foo (x y) 1 2)"
        compiled_program = "def foo(x, y):\n    1\n    2"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_return(self):
        program = "(return 2)"
        compiled_program = "return 2"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_add(self):
        program = "(+ 2 3 4)"
        compiled_program = "2 + 3 + 4"
        self.assertEqual(lython_compile(program), compiled_program)

    def test_multiply(self):
        program = "(* 2 3 4)"
        compiled_program = "2 * 3 * 4"
        self.assertEqual(lython_compile(program), compiled_program)


class LexerTests(TestCase):
    def test_comment(self):
        program = "; foo"
        compiled_program = ""
        self.assertEqual(lython_compile(program), compiled_program)
        


if __name__ == "__main__":
    unittest.main()
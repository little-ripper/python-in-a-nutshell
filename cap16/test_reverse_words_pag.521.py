"""This module tests function reverse_words
provided."""
import unittest
import importlib.util
import sys
from pathlib import Path

file_path = Path("doctest_pag.518.py").resolve()
module_name = "doctest_pag_518"
spec = importlib.util.spec_from_file_location(module_name, str(file_path))
mod = importlib.util.module_from_spec(spec)
sys.modules[module_name] = mod
spec.loader.exec_module(mod)


class ModTest(unittest.TestCase):
    def testNormalCaseWorks(self):
        self.assertEqual(
            'years seven and score four',
            mod.reverse_words('four score and seven years')
        )

    def testArgumentMustBeString(self):
        with self.assertRaises(
                (AttributeError, TypeError)
        ):
            mod.revers_words(1)


if __name__ == '__main__':
    unittest.main()

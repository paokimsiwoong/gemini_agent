# tests.py
import os

import unittest
from functions.get_files_info import get_files_info


class TestCalculator(unittest.TestCase):
    def test_defaultdir(self):
        result = get_files_info("calculator")
        print("Result for current directory:")
        print(result)
        self.assertTrue(f" - main.py: file_size={os.path.getsize("calculator/main.py")} bytes, is_dir=False" in result)
        self.assertTrue(f" - tests.py: file_size={os.path.getsize("calculator/tests.py")} bytes, is_dir=False" in result)
        self.assertTrue(f" - pkg: file_size={os.path.getsize("calculator/pkg")} bytes, is_dir=True" in result)

    def test_subdir(self):
        result = get_files_info("calculator", "pkg")
        print("Result for 'pkg' directory:")
        print(result)
        self.assertTrue(f" - calculator.py: file_size={os.path.getsize("calculator/pkg/calculator.py")} bytes, is_dir=False" in result)
        self.assertTrue(f" - render.py: file_size={os.path.getsize("calculator/pkg/render.py")} bytes, is_dir=False" in result)

    def test_wrongdir(self):
        result = get_files_info("calculator", "/bin")
        print("Result for '/bin' directory:")
        print(result)
        self.assertTrue('Error: Cannot list "/bin" as it is outside the permitted working directory' in result)
    
    def test_outside(self):
        result = get_files_info("calculator", "../")
        print("Result for '../' directory:")
        print(result)
        self.assertTrue('Error: Cannot list "../" as it is outside the permitted working directory' in result)

if __name__ == "__main__":
    unittest.main()
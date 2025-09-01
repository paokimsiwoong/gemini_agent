# tests.py
import os

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from config import MAX_CHARS

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

    def test_file_lorem(self):
        file_path = "lorem.txt"
        result = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        print(result[:20])
        print(f'len: {len(result)}')
        self.assertEqual(len(result), MAX_CHARS + len(f'[...File "{file_path}" truncated at 10000 characters]'))

    def test_file_outside(self):
        file_path = "../main.py"
        result = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        print(result)
        self.assertEqual(result, f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    def test_file_main(self):
        file_path = "main.py"
        result = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        # print(result[:103])
        print(result)
        self.assertTrue("def main():" in result)

    def test_file_cal(self):
        file_path = "pkg/calculator.py"
        result = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        # print(result[:58])
        print(result)
        self.assertTrue("class Calculator:" in result)

    def test_file_abspath(self):
        file_path = "/bin/cat"
        # @@@ /로 시작하면 절대경로로 판단 
        # @@@ @@@ ==> os.path.join은 calculator를 버리고 절대경로인 /bin/cat만을 반환한다 
        result = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        print(result)
        self.assertEqual(result, f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    def test_file_nonexist(self):
        file_path = "pkg/does_not_exist.py"
        result = get_file_content("calculator", file_path)
        print(f"Result for '{file_path}':")
        print(result)
        self.assertEqual(result, f'Error: File not found or is not a regular file: "{file_path}"')

if __name__ == "__main__":
    unittest.main()
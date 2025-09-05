# tests.py
import os

import unittest
from functions.get_files_info import get_files_info
from functions.get_file_content import get_file_content
from functions.write_file import write_file
from functions.run_python_file import run_python_file
from config import MAX_CHARS

class TestCalculator(unittest.TestCase):
    # def test_defaultdir(self):
    #     result = get_files_info("calculator")
    #     print("Result for current directory:")
    #     print(result)
    #     self.assertTrue(f" - main.py: file_size={os.path.getsize("calculator/main.py")} bytes, is_dir=False" in result)
    #     self.assertTrue(f" - tests.py: file_size={os.path.getsize("calculator/tests.py")} bytes, is_dir=False" in result)
    #     self.assertTrue(f" - pkg: file_size={os.path.getsize("calculator/pkg")} bytes, is_dir=True" in result)

    # def test_subdir(self):
    #     result = get_files_info("calculator", "pkg")
    #     print("Result for 'pkg' directory:")
    #     print(result)
    #     self.assertTrue(f" - calculator.py: file_size={os.path.getsize("calculator/pkg/calculator.py")} bytes, is_dir=False" in result)
    #     self.assertTrue(f" - render.py: file_size={os.path.getsize("calculator/pkg/render.py")} bytes, is_dir=False" in result)

    # def test_wrongdir(self):
    #     result = get_files_info("calculator", "/bin")
    #     print("Result for '/bin' directory:")
    #     print(result)
    #     self.assertTrue('Error: Cannot list "/bin" as it is outside the permitted working directory' in result)
    
    # def test_outside(self):
    #     result = get_files_info("calculator", "../")
    #     print("Result for '../' directory:")
    #     print(result)
    #     self.assertTrue('Error: Cannot list "../" as it is outside the permitted working directory' in result)

    # def test_file_lorem(self):
    #     file_path = "lorem_backup.txt"
    #     result = get_file_content("calculator", file_path)
    #     print(f"Result for '{file_path}':")
    #     print(result[:20])
    #     print(f'len: {len(result)}')
    #     self.assertEqual(len(result), MAX_CHARS + len(f'[...File "{file_path}" truncated at 10000 characters]'))

    # def test_file_outside(self):
    #     file_path = "../main.py"
    #     result = get_file_content("calculator", file_path)
    #     print(f"Result for '{file_path}':")
    #     print(result)
    #     self.assertEqual(result, f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    # def test_file_main(self):
    #     file_path = "main.py"
    #     result = get_file_content("calculator", file_path)
    #     print(f"Result for '{file_path}':")
    #     # print(result[:103])
    #     print(result)
    #     self.assertTrue("def main():" in result)

    # def test_file_cal(self):
    #     file_path = "pkg/calculator.py"
    #     result = get_file_content("calculator", file_path)
    #     print(f"Result for '{file_path}':")
    #     # print(result[:58])
    #     print(result)
    #     self.assertTrue("class Calculator:" in result)

    # def test_file_abspath(self):
    #     file_path = "/bin/cat"
    #     # @@@ /로 시작하면 절대경로로 판단 
    #     # @@@ @@@ ==> os.path.join은 calculator를 버리고 절대경로인 /bin/cat만을 반환한다 
    #     result = get_file_content("calculator", file_path)
    #     print(f"Result for '{file_path}':")
    #     print(result)
    #     self.assertEqual(result, f'Error: Cannot read "{file_path}" as it is outside the permitted working directory')

    # def test_file_nonexist(self):
    #     file_path = "pkg/does_not_exist.py"
    #     result = get_file_content("calculator", file_path)
    #     print(f"Result for '{file_path}':")
    #     print(result)
    #     self.assertEqual(result, f'Error: File not found or is not a regular file: "{file_path}"')

    # def test_write_overwrite(self):
    #     file_path = "lorem.txt"
    #     content = "wait, this isn't lorem ipsum"
    #     result = write_file("calculator", file_path=file_path, content=content)
    #     print(result)
    #     self.assertEqual(result, f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
    # def test_write_file(self):
    #     file_path = "pkg/morelorem.txt"
    #     content = "lorem ipsum dolor sit amet"
    #     result = write_file("calculator", file_path=file_path, content=content)
    #     print(result)
    #     self.assertEqual(result, f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
    # def test_write_fileanddirs(self):
    #     file_path = "pkg/test/morelorem.txt"
    #     content = "lorem ipsum dolor sit amet"
    #     result = write_file("calculator", file_path=file_path, content=content)
    #     print(result)
    #     self.assertEqual(result, f'Successfully wrote to "{file_path}" ({len(content)} characters written)')
    
    # def test_write_outside(self):
    #     file_path = "/tmp/temp.txt"
    #     content = "this should not be allowed"
    #     result = write_file("calculator", file_path=file_path, content=content)
    #     print(result)
    #     self.assertEqual(result, f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory')
    
    # def test_write_dir(self):
    #     file_path = "pkg/test"
    #     content = "this should not be allowed"
    #     result = write_file("calculator", file_path=file_path, content=content)
    #     print(result)
    #     self.assertEqual(result, f'Error: "{file_path}" is a directory, not a file')

    def test_run_default(self):
        file_path = "main.py"
        result = run_python_file("calculator", file_path=file_path)
        print(result)
        self.assertTrue('Usage: python main.py "<expression>"' in result)

    def test_run_addition(self):
        file_path = "main.py"
        result = run_python_file("calculator", file_path=file_path, args=["3 + 5"])
        print(result)
        self.assertTrue('=' in result)
        self.assertTrue('8' in result)

    def test_run_tests(self):
        file_path = "tests.py"
        result = run_python_file("calculator", file_path=file_path)
        print(result)
        self.assertTrue("Ran" in result)
        self.assertTrue("OK" in result)

    def test_run_outside(self):
        file_path = "../main.py"
        result = run_python_file("calculator", file_path=file_path)
        print(result)
        self.assertEqual(result, f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory')

    def test_run_nonexistent(self):
        file_path = "nonexistent.py"
        result = run_python_file("calculator", file_path=file_path)
        print(result)
        self.assertEqual(result, f'Error: File "{file_path}" not found.')

if __name__ == "__main__":
    unittest.main()
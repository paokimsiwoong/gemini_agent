import os

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    '''
    주어진 경로의 파일 내용을 스트링으로 반환하는 함수
    '''
    
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
  

    # 지정한 working directory를 벗어나는 경우를 차단하기
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
    
    # 파일 여부 확인
    if not os.path.isfile(abs_full_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'
    
    try:
        with open(abs_full_path, "r") as f:
            content = f.read(MAX_CHARS)

        if len(content) == MAX_CHARS:
            content += f'[...File "{file_path}" truncated at 10000 characters]'

    except Exception as e:
        return f'Error: {e}'
    
    return content
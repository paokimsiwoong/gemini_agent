import os

def write_file(working_directory, file_path, content):
    '''
    주어진 경로에 파일을 생성하는 함수 
    '''
    
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
  

    # 지정한 working directory를 벗어나는 경우를 차단하기
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot write to "{file_path}" as it is outside the permitted working directory'
    
    # 파일 경로 디렉토리 다 있는지 확인
    # file_name = file_path.split("/")[-1]
    # if not os.path.exists(abs_full_path[:-len(file_name)]):
    #     try:
    #         os.makedirs(abs_full_path[:-len(file_name)])
    #     except Exception as e:
    #         return f'Error: {e}'
    # @@@ os.path.dirname 활용하기
    if not os.path.exists(abs_full_path):
        try:
            os.makedirs(os.path.dirname(abs_full_path), exist_ok=True)
        except Exception as e:
            return f'Error: {e}'
    
    # @@@ 경로가 이미 존재해서 os.path.exists(abs_full_path)는 통과했지만
    # @@@ 파일이 아니라 디렉토리일 경우 예외처리를 하지 않으면 open에서 에러 발생
    if os.path.exists(abs_full_path) and os.path.isdir(abs_full_path):
        return f'Error: "{file_path}" is a directory, not a file'

    # 파일에 content 내용 쓰기
    try:
        with open(abs_full_path, "w") as f:
            # open mode 기본값은 "r"이므로 쓰기를 하려면 "w" 명시 필수
            f.write(content)
    except Exception as e:
        return f'Error: {e}'


    return f'Successfully wrote to "{file_path}" ({len(content)} characters written)'
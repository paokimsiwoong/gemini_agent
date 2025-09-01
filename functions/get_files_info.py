import os

def get_files_info(working_directory, directory="."):
    '''
    주어진 경로에 있는 파일이나 폴더의 정보를 리스트로 담은 스트링을 반환하는 함수
    '''
    # @@@ TODO: try - except로 raise된 에러 잡고 에러를 string으로 반환하기
    result = []

    full_path = os.path.join(working_directory, directory)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
  

    # 지정한 working directory를 벗어나는 경우를 차단하기
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot list "{directory}" as it is outside the permitted working directory'
    
    if not os.path.isdir(abs_full_path):
        return f'Error: "{directory}" is not a directory'
    


    try:
        for d in os.listdir(abs_full_path):
            d_path = os.path.join(abs_full_path, d)

            r = f" - {d}: file_size={os.path.getsize(d_path)} bytes, is_dir={os.path.isdir(d_path)}"
            result.append(r)
    except Exception as e:
        return f'Error: {e}'

    return "\n".join(result)

    
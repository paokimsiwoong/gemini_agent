import os
import subprocess

def run_python_file(working_directory, file_path, args=[]):
    '''
    주어진 경로의 파이썬 파일을 실행하는 함수
    '''
    
    full_path = os.path.join(working_directory, file_path)
    abs_working_directory = os.path.abspath(working_directory)
    abs_full_path = os.path.abspath(full_path)
  

    # 지정한 working directory를 벗어나는 경우를 차단하기
    if not abs_full_path.startswith(abs_working_directory):
        return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'
    
    # 파일 존재 여부 확인
    if not os.path.exists(abs_full_path):
        return f'Error: File "{file_path}" not found.'
    
    # .py 파일인지 확인
    if not abs_full_path.endswith(".py"):
        return f'Error: "{file_path}" is not a Python file.'

    # .py 파일 실행
    try:
        completed_process = subprocess.run(
            args=(['uv', 'run', abs_full_path] + args), 
            capture_output=True, 
            text=True, 
            timeout=30.0,
            cwd=abs_working_directory, # @@@ cwd는 이 서브 프로세스가 실행되는 디렉토리를 지정
            )
    except Exception as e:
        return f'Error: {e}'


    return_string = ""
    # @@@ stdout과 stderr이 공백이 아닐때만 추가하기. 둘다 공백일 경우 "No output produced\n"
    if len(completed_process.stdout) != 0: # len 쓰는 대신 if completed_process.stdout: 만 사용해도 문제 없음
        return_string += f'STDOUT:\n{completed_process.stdout}\n'
    if len(completed_process.stderr) != 0:
        return_string += f'STDERR:\n{completed_process.stderr}\n'
    
    # exit code가 0이 아니면 추가 문구
    if completed_process.returncode != 0:
        return_string += f"Process exited with code {completed_process.returncode}"

    # 결과 반환
    return return_string if return_string else "No output produced."
    
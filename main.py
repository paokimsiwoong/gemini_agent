import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types

from config import SYSTEM_PROMPT
from call_function import AVAILABLE_FUNCTIONS, call_function


def main():
    print("Hello from gemini-agent!")

    # .env 파일 불러와 환경변수에 등록
    load_dotenv()
    
    # verbose_flag = False

    # if "--verbose" in sys.argv:
    #     verbose_flag = True

    # @@@ verbose_flag 에 바로 조건문 입력하면 됨
    verbose_flag = "--verbose" in sys.argv

    # args = sys.argv[1:] # sys.argv[0]은 실행 스크립트의 이름 (main.py)
    # @@@ flag를 제외한 argument들만 args에 저장
    args = []
    for arg in sys.argv[1:]:
        if not arg.startswith("--"):
            args.append(arg)


    if not args:
        raise Exception("the prompt is not provided")
        # @@@ sys.exit(1)도 exit code 1 과 함께 종료 가능
    
    
    user_prompt = " ".join(args)

    # GEMINI_API_KEY 값 저장
    api_key = os.environ.get("GEMINI_API_KEY")

    # gemini client 생성
    client = genai.Client(api_key=api_key)

    if verbose_flag:
        print("User prompt: " + user_prompt)

    messages = [
        types.Content(role="user", parts=[types.Part(text=user_prompt)]),
    ]

    for i in range(20):
        try:
            response_text = generate_content(client=client, messages=messages, verbose_flag=verbose_flag)

            if response_text is not None:
                break

        except Exception as e:
            raise e

    print("Final response:")
    print(response_text)

# 유저 메세지 입력과 그 답변, 토큰 개수 출력은 계속 반복 사용될 코드이므로 함수로 만들기
def generate_content(client: genai.Client, messages: list[types.Content], verbose_flag: bool):


    # 모델을 선택하고 프롬프트 입력해 답변 받기
    response = client.models.generate_content(
        model="gemini-2.0-flash-001", 
        contents=messages,
        config= types.GenerateContentConfig(
            system_instruction=SYSTEM_PROMPT,
            tools=[AVAILABLE_FUNCTIONS], # tools 인자에는 types.Tool을 담은 list 제공
            ),
        )
    # response는 GenerateContentResponse 타입


    if verbose_flag:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")
    
    if response.candidates: # @@@ list가 비어있는지 여부 반드시 확인
        for candidate in response.candidates:
            # candidate의 contetn필드는 types.Content 
            messages.append(candidate.content)


    # 함수 호출이 없이 단순 텍스트 답변이면 바로 반환
    if not response.function_calls:
        return response.text

    # 함수 호출이 있는 경우 함수 호출
    function_responses = []
    for function_call_part in response.function_calls:
        function_call_result = call_function(function_call_part=function_call_part, verbose=verbose_flag)

        # types.Content.parts는 types.Part의 리스트 => 빈 리스트인지 확인
        # 빈 리스트가 아니면 그 안의 types.FunctionResponse의 response 필드(dict)가 비어있는지 확인
        if not function_call_result.parts or not function_call_result.parts[0].function_response.response:
            raise Exception("No function response found")

        if verbose_flag:
            print(f"-> {function_call_result.parts[0].function_response.response}")

        function_responses.append(function_call_result)

    # call_function으로 함수들을 실행했는데도 함수 실행 결과가 없으면 raise
    if not function_responses:
        raise Exception("No function response found")
    
    # 함수 결과들을 messages에 추가
    for f_response in function_responses:
        messages.append(f_response)

if __name__ == "__main__":
    main()

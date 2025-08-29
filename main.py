import os
import sys
from dotenv import load_dotenv
from google import genai
from google.genai import types


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

    generate_content(client=client, messages=messages, verbose_flag=verbose_flag)


# 유저 메세지 입력과 그 답변, 토큰 개수 출력은 계속 반복 사용될 코드이므로 함수로 만들기
def generate_content(client, messages, verbose_flag):
    # 모델을 선택하고 프롬프트 입력해 답변 받기
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=messages)
    # response는 GenerateContentResponse 타입


    if verbose_flag:
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}")

    print("Response: " + response.text)

if __name__ == "__main__":
    main()

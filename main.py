import os
from dotenv import load_dotenv
from google import genai



def main():
    print("Hello from gemini-agent!")

    # .env 파일 불러와 환경변수에 등록
    load_dotenv()
    # GEMINI_API_KEY 값 저장
    api_key = os.environ.get("GEMINI_API_KEY")

    # gemini client 생성
    client = genai.Client(api_key=api_key)

    prompt = "Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."

    print("Prompt: " + prompt)

    # 모델을 선택하고 프롬프트 입력해 답변 받기
    response = client.models.generate_content(model="gemini-2.0-flash-001", contents=prompt)
    # response는 GenerateContentResponse 타입

    print("Response: " + response.text)

    print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
    print(f"Response tokens: {response.usage_metadata.candidates_token_count}")


if __name__ == "__main__":
    main()

# render.py

# 계산식과 계산 결과를 보기 좋게 만든 스트링을 반환하는 함수
def render(expression, result):
    # 결과값이 정수인 경우
    if isinstance(result, float) and result.is_integer():
        # int로 변환해 .0 제거 후 str로 변환
        result_str = str(int(result))
    # 정수가 아닌 경우
    else:
        # float 그대로 str 변환
        result_str = str(result)

    # 계산식과 결과값을 둘러 쌀 박스의 테두리를 제외한 내부 길이 설정
    box_width = max(len(expression), len(result_str)) + 4

    box = []
    # 박스 최상단(뚜껑)
    box.append("┌" + "─" * box_width + "┐")
    # 계산식
    box.append(
        "│" + " " * 2 + expression + " " * (box_width - len(expression) - 2) + "│"
    )
    # 중간 공백
    box.append("│" + " " * box_width + "│")
    # =
    box.append("│" + " " * 2 + "=" + " " * (box_width - 3) + "│")
    # 중간 공백
    box.append("│" + " " * box_width + "│")
    # 결과값
    box.append(
        "│" + " " * 2 + result_str + " " * (box_width - len(result_str) - 2) + "│"
    )
    # 박스 최하단(바닥)
    box.append("└" + "─" * box_width + "┘")

    # "\n"(줄바꾸기)로 join 후 반환
    return "\n".join(box)
# calculator.py

class Calculator:
    def __init__(self):
        self.operators = {
            "+": lambda a, b: a + b,
            "-": lambda a, b: a - b,
            "*": lambda a, b: a * b,
            "/": lambda a, b: a / b,
        }
        self.precedence = {
            "+": 1,
            "-": 1,
            "*": 2,
            "/": 2,
        }

    # 들어온 계산식을 공백 기준으로 나누어 tokens를 만들고 tokens로 _evaluate_infix를 실행한 결과를 반환
    def evaluate(self, expression):
        if not expression or expression.isspace():
            return None
        tokens = expression.strip().split()
        return self._evaluate_infix(tokens)

    # 들어온 tokens를 값과 연산자로 구분해 연산을 진행
    def _evaluate_infix(self, tokens):
        # 값들을 저장하는 리스트
        values = []
        # 연산자들을 저장하는 리스트
        operators = []

        for token in tokens:
            # 이번 토큰이 연산자일 경우
            if token in self.operators:
                # operators에 연산자가 들어 있고, 현재 토큰보다 우선 순위가 높거나 같은 연산자가 들어있을 경우 
                # 이번 토큰을 append 하기 전에 연산을 먼저 한번 진행하고 append
                while (
                    operators
                    and operators[-1] in self.operators
                    and self.precedence[operators[-1]] >= self.precedence[token]
                ):
                    self._apply_operator(operators, values)
                operators.append(token)
            # 이번 토큰이 값일 경우
            else:
                try:
                    # values에 append
                    values.append(float(token))
                except ValueError:
                    raise ValueError(f"invalid token: {token}")

        while operators:
            self._apply_operator(operators, values)

        if len(values) != 1:
            raise ValueError("invalid expression")

        return values[0]

    # operators[-1] 연산자로 values[-2], values[-1]을 연산하는 함수
    def _apply_operator(self, operators, values):
        if not operators:
            return

        operator = operators.pop()
        if len(values) < 2:
            raise ValueError(f"not enough operands for operator {operator}")

        b = values.pop()
        a = values.pop()
        values.append(self.operators[operator](a, b))
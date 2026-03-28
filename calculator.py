def calculator():
    print("=== 간단한 계산기 ===")
    print("종료하려면 'q'를 입력하세요.\n")

    while True:
        num1 = input("첫 번째 숫자: ")
        if num1 == 'q':
            break

        operator = input("연산자 (+, -, *, /): ")
        if operator == 'q':
            break

        num2 = input("두 번째 숫자: ")
        if num2 == 'q':
            break

        try:
            num1 = float(num1)
            num2 = float(num2)
        except ValueError:
            print("숫자를 올바르게 입력해주세요.\n")
            continue

        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num2 == 0:
                print("0으로 나눌 수 없습니다.\n")
                continue
            result = num1 / num2
        else:
            print("올바른 연산자를 입력해주세요.\n")
            continue

        print(f"결과: {num1} {operator} {num2} = {result}\n")

    print("계산기를 종료합니다.")


if __name__ == "__main__":
    calculator()

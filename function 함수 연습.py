def cal(num1, num2, op) :
    if op == "+":
        result = num1 + num2
    else :
        num1 - num2
    return result
num1 = int(input("첫 번째 정수 입력: "))
num2 = int(input("두 번째 정수 입력: "))
op = input("연산자 입력(+, -): ")
result = cal(num1, num2, op)
print("결과: {} ".format(result))
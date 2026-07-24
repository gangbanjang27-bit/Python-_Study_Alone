#사용자 입력: input()
#input() 함수로 사용자 입력받기
input("입력하세요: ")
#문자열이 뜨고 프로그램이 종료되지 않은 상태에서 대기
#이렇게 프로그램이 실행 도중에 잠시 멈추는 것을 블록block이라고 함
string = input("입력하세요: ")
print(string)
#사용자가 입력한 내용은 input함수의 결과로 나오는데, 이 값은 변수에 대입해서 사용 가능
#input함수의 결과로 나오는 값을 리턴값이라고 함

#input() 함수의 자료형
print(type(string)) #<class 'str'>

number = input("숫자를 입력하세요: ")
print(type(number)) #<class 'str'>
#input()함수는 사용자가 무엇을 입력해도 결과는 무조건 문자열 자료형
#True나 False와 같은 boolean값을 입력해도 마찬가지

#직접 해보는 손코딩: 입력 자료형 확인하기
string = input("입력: ")
print("자료:", string)
print("자료형:", type(string))

#직접 해보는 손코딩: 입력받고 더하기
string = input("입력: ")
print("입력 + 100:", string + 100) #TypeError: can only concatenate str (not "int") to str
#input으로 입력받은 자료는 모두 문자열로 저장되므로 만약 300을 입력했다면 "300" + 100이 되어
#문자열과 숫자는 더할 수 없어 오류 발생

#문자열을 숫자로 바꾸기: int(), float()
#int(): 문자열을 int 자료형으로 변환
#float(): 문자열을 float 자료형으로 변환

#직접 해보는 손코딩: int()함수 활용하기
string_a = input("입력A: ")
int_a = int(string_a)

string_b = input("입력B: ")
int_b = int(string_b)

print("문자열 자료:", string_a + string_b)
print("숫자 자료:", int_a + int_b)

#직접 해보는 손코딩: int()함수와 float()함수 활용하기
output_a = int("52")
output_b = float("52.273")

print(type(output_a), output_a) #<class 'int'> 52
print(type(output_b), output_b) #<class 'float'> 52.273

#직접 해보는 손코딩: int()함수와 float()함수 조합하기
input_a = float(input("첫 번째 숫자: ")) #273
input_b = float(input("두 번째 숫자: ")) #52

print("덧셈 결과:", input_a + input_b) #325.0
print("뺄셈 결과:", input_a - input_b) #221.0
print("곱셈 결과:", input_a * input_b) #14196.0
print("나눗셈 결과:", input_a / input_b) #5.25

#ValueError예외

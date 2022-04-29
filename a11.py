print("###########################")
print("# 짝수와 홀수 판별 앱 #")
print("###########################")

x = int(input("x값 정수를 입력하시오:"))
if (x % 2) ! = 0 :
    print ("홀수입니다.")
else:
    print("짝수입니다.")


print("정수를 입력하시오")
x = int(input("정수값 x를 입력하시오.: "))
y = int(input("정수값 y를 입력하시오.: "))
if x > y : 
    print(x)
else:
    print(y)



print("####################")
print("# 이름, 나이, 답변 앱 #")
print("####################")

yu_name = str(input(이름: "))
yu_age = int(input("나이"))

if yu_age <= 25 : 
    print("와우!!! 프로그래밍을 완벽히 배울 수 있는 나이입니다.! ")

else:
    print("포기하기에는 아직 늦지 않았습니다.")
print("/n")



price = int(input("상품의 가격을 입력하세요.: "))

if price > 100000 : 
    shipping_cost = 3000
else:
    shipping_cost = 5000

print("배송료는", shipping_cost, 입니다."")
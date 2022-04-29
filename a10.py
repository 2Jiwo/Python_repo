print("#########################")
print(" 배송료 계산 프로그램 #")
print("#########################")
price= int(input("상품의 가격을 입력하세요: "))
if price > 2000:
    shipping_cost = 0
else:
    shipping_cost = 3000
print(shipping_cost)



print("########################")
print("# 합격 불합격 프로그램 #")
print("########################")

grade = int(input("성적을 입력하시오: "))
if grade >= 60 : 
    print("합격")
else : 
    print("불합격")



print("근무 시간을 입력하시오")
work_hour=int(input("근무시간 입력: "))

if work_hour > 72 : 
    print("초과근무 하셨습니다")
else:
    print("정상근무하셨습니다")
    
# num1, num2 = map(int, input().split(' '))
# print(num1+num2)
# if num1 < 100 and num2 < 100:
#     print(num2 + 112)
# else

get_date = input()

zodiac = { "Водолей": [f"1 {i}" for i in range(20,32)] + [f"2 {i}" for i in range(1,19)] }

for name, days in zodiac.items():
    if get_date in days:
        print(name)

        exit()
print("некорректная дата")
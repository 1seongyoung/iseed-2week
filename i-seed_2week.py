#Question 1
print('----------------')
print("문제 1번 풀이")
print("100")
print(100)
print(50+50)
print("50+50")

#Question 2
print('----------------')
print("문제 2번 풀이")
print('%d / %d = %d' % (5, 10, 5/10))

#Question 3
print('----------------')
print("문제 3번 풀이")
print("%04d"%876)
print("%5s"%"CookBook")
print("%1.1f"%123.45)

#Question 4
print('----------------')
print("문제 4번 풀이")
print("{2:d} {0:d} {1:d}".format(111,222,333))

#Question 11
print('----------------')
print("문제 11번 풀이")
first_number = int('1011', 2)
second_number = int('1A',16)
print(first_number, second_number)

#Question 13
#print('----------------')
#print("문제 13번 풀이")
#int('1002',2)
#int('1008',8)
#int('AAFG',16)

#Question 15
print('----------------')
print("문제 15번 풀이")
num = 12345678

hex_num = hex(num)
oct_num = oct(num)
bin_num = bin(num)

print("10진수 ==> ", num)
print("16진수 ==> ", hex_num)
print("8진수 ==> ", oct_num)
print("2진수 ==> ", bin_num)

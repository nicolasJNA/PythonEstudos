num = 20
num2 = 30

print(num < num2 and num2 > 0)
print(num == num2 or num2 is num)
print(not num < num2)

num = num2
print(not (num == num2 or num2 == 30))
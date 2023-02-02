num =int(input("how many numbers : "))

total_sum=0

for n in range(num):
    numbers=float(input("input Your numbers : "))
    total_sum=total_sum+numbers

print("num ",num)
avg = total_sum/num

print("avg is : ",avg)
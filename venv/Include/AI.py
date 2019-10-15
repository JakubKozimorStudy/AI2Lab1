sum=0
for i in range(1,41):
    if i%3 == 0 or i%5==0:
        print(i)
        sum += i

print("Suma do 41: ")
print (sum)

sum=0
for i in range(1,1001):
    if i%3 == 0 or i%5==0:
        sum += i
print("Suma do 1001: ")
print (sum)
n = int(input("Enter the value of n: "))
a = []
for i in range(1, n+1):
    value = i**2 + 2*i + 1
    a.append(value)
print("Sequence:", a)
print("Sum:", sum(a))
print("Average:", sum(a)/n)
print("Maximum:", max(a))
print("Minimum:", min(a))
count = 0
for value in a:
    if value % 2 == 0 and value % 3 == 0:
        count += 1
print("Count divisible by both 2 and 3:", count)   
print("Sequence in reverse:", ends=" ")
for i in range (len(a) -1, -1, -1):
    print(a[i], ends=" ")


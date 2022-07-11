# Prime-number-from-1-to-100
lower = 1
upper = 100
print("The is the Num_Prime from lower to Upper:");
for num in range (lower,upper+1):
  if all(num%i!=0 for i in range(2,num)):
    print(num)


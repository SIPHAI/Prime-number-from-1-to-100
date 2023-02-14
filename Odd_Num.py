lower = 1;
upper = 100;
print("The range of numbers started from lower = 1 and upper = 100:");
for num in range (lower, upper+1):
      if all(num%i!=0 for i in range(1,num+1)):
        print(num);

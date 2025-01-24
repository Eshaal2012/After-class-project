# Get input no
num=int(input("Enter a number :"))  

# define varibles for use in code 
dgts, temp, ctr, sum = 0, num, 0, 0

# Find number of digits in num and store in dgts
while temp != 0:
   dgts = dgts+1
   temp = int(temp / 10)

# Loop for dgts times and store value to sum
temp = num
for i in range(dgts):
   temp2 = int(temp % 10)
   temp = int(temp / 10)
   sum = sum + (temp2**dgts)

# Check if sum = num and print result
if sum == num:
   print(f"The number is Armstrong")
else:
   print(f"The number is NOT Armstrong")

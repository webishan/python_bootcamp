# =============================================================================
# Ask the user for two numbers between 1 and 100. Then count from the lower number to the higher number. Print the results in the screen.
# =============================================================================

num_1 = int(input('Please enter a number between 1-100:> '))
num_2 = int(input('Please enter a number between 1-100:> '))

while num_1 < 0 or num_2 < 0 or num_1 > 100 or num_2 > 100 or num_1 == num_2:
    print('Numbers must be different values between 1 and 100, try again:> ')
    num_1 = int(input('Please enter a number between 1-100:> '))
    num_2 = int(input('Please enter a number between 1-100:> '))
    
    
if num_1 < num_2:
    for i in range(num_1,num_2+1):
        print(i,end=' ')
        
else:
    for i in range(num_2,num_1+1):
        print(i, end=' ')
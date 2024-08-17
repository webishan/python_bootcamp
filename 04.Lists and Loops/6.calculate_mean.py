# =============================================================================
# Ask the user to input a sequence of numbers. Then calculate the mean and print the result
# =============================================================================

user_input = input('Please enter a number type exit to stop:> ')
numbers = []

while user_input.lower() != 'exit':
    while not user_input.isdigit():
        print('That is not a number! Numbers only please:> ')
        user_input = input('Try again:> ')
        
    numbers.append(int(user_input))
    user_input = input('Please enter the next number:> ')
    
total = 0
for number in numbers:
    total += number
    
print(f'Mean is {total/len(numbers)}')
print(sum(numbers)/len(numbers))
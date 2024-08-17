# =============================================================================
# Print out a times table between 1 and 12 (No need to ask user for input)
# =============================================================================

for i in range(1,13):
    print('============================')
    print()
    print(f'This is the {i} times table')
    print()
    
    for j in range(1,13):
        print(f'{j} * {i} = {j*i}')
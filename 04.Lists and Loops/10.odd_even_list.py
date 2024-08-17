# =============================================================================
# Write some code that will determine all odd and even numbers between 1 and 100. Put the odds in a list named odd and the evens in a list named even.
# =============================================================================


n = 100

#instantiate empty lists
evens = []
odds = []

for i in range(n+1):
    if not i % 2:
        evens.append(i)
        
    else:
        odds.append(i)
        
print(f'The evens are {evens}')
print(f'The odds are {odds}')
        
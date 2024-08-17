
capitals = {'France':'Paris','Spain':'Madrid','United Kingdom':'London','India':'New Delhi','United States':'Washington DC','Italy':'Rome','Denmark':'Copenhagen','Germany':'Berlin','Greece':'Athens','Bulgaria':'Sofia','Ireland':'Dublin','Mexico':'Mexico City'}


# =============================================================================
# capitals['Germany']
# 
# capitals.get('Germany')
# 
# capitals['South Korea'] = 'Seoul'
# 
# print(capitals)
# 
# print(capitals.items())
# 
# =============================================================================


# =============================================================================
# for country in capitals:
#     print(country)
# =============================================================================


# =============================================================================
# for country,city in capitals.items():
#     print(f'The capital of {country}, is {city}')
# =============================================================================
    

# =============================================================================
# print(capitals.keys())
# 
# print(capitals.values())
# =============================================================================


# =============================================================================
# if 'France' in capitals:
#     print('It contains France')
# =============================================================================


# =============================================================================
# L = [1,2,3,4,5]
# print(7 in L)
# =============================================================================


sherlock = '''  Mr. SherlockHolmes, who was usually
 very late in the mornings, save upon
 those not infrequent occasions when he
 was up all night, was seated at the break
fast table. I stood upon the hearth-rug and picked
 up the stick which our visitor had left behind him
 the night before. It was a fine, thick piece of wood,
 bulbous-headed, of the sort which is known as a
 “Penang lawyer.” Just under the head was a broad
 silver band nearly an inch across. “To James Mor
timer, M.R.C.S., from his friends of the C.C.H.,” was
 engraved upon it, with the date “1884.” It was just
 such a stick as the old-fashioned family practitioner
 used to carry—dignified, solid, and reassuring.
 “Well, Watson, what do you make of it?”
 Holmes was sitting with his back to me, and I
 had given him no sign of my occupation.
 “HowdidyouknowwhatIwasdoing? Ibelieve
 you have eyes in the back of your head.”   '''
 
 
 
letter_count = {}
for letter in sherlock:
    letter_count[letter.lower()] = letter_count.get(letter,0) + 1
     
print(letter_count)


import matplotlib.pyplot as plt

x,y = zip(*letter_count.items())

plt.bar(x,y)
plt.show()




letter_count_clean = {}

for k,v in letter_count.items():
    if k.isalpha():
        letter_count_clean[k] = v
        
print(letter_count_clean)

x,y = zip(*letter_count_clean.items())

plt.bar(x,y)
plt.show()